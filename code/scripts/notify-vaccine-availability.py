# 9th May 21 314 notify vaccine availability
# to install dependencies on mac run -> pip3 install tabulate && pip3 install requests
# to start the script python3 nameOfFile.py

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from tabulate import tabulate
import time
import sched
import datetime
import requests
import os

emailFrom = 'ridammj@yahoo.com'
emailFromPassword = 'x'

locationMailList2 = [
    [['cse170001037@iiti.ac.in', 'ridammj@gmail.com', 'nikhilbarodiya@gmail.com'], 314], 
    [['Pravin.vinayakia@gmail.com', 'imaartijain@gmail.com'], 322],
]

locationMailListTest = [
    [['ridammj@gmail.com'], 314] 
]

locationMailList = [
    [['cse170001037@iiti.ac.in', 'ridammj@gmail.com', 'nikhilbarodiya@gmail.com'], 314],
    [['Pravin.vinayakia@gmail.com', 'imaartijain@gmail.com'], 322],
    [['nishithj7@gmail.com', 'yashlukkad@gmail.com'], 318],
    [['sawanlukked@gmail.com'], 571]
]
emailNotificationEnabled = True
macNotificationEnabled = True
tableHeaders = ['Name', 'Address', 'Date', 'Vaccine type','Available capacity', 'Slots', 'Min age']
style1 = 'fancy_grid'
style2 = 'html'
notificationStrSuccess = f"echo -en '\a\a\a'"
notificationStrFailure = f"echo -en '\a\a\a'"

capacityFilter = 0
indoreDistrictId = 314
minAgeLimit = 18
eventLoopIntervalInSeconds = 60*2

################################################################

s = sched.scheduler(time.time, time.sleep)

def sendEmail(fromMail,fromMailPassword,toMail,data):
    if(emailNotificationEnabled == False):
         print("email notification disabled")
         return
    try:
        msg = MIMEMultipart('alternative')
        msg['Subject'] = f'Covid Vaccine Availability Alert!! at {datetime.datetime.now()}'
        msg['From'] = emailFrom
        msg['To'] = ','.join(toMail)
        text = "\n\n"
        html = f'<html><head></head><body><p>Hi!<br>Please find below available centers<br><br>{data}<br><br><br>Regards,<br>Ridam</p></body></html>'
        part1 = MIMEText(text, 'plain')
        part2 = MIMEText(html, 'html')
        msg.attach(part1)
        msg.attach(part2)
        smtpObj = smtplib.SMTP_SSL('smtp.mail.yahoo.com', 465)
        smtpObj.login(fromMail, fromMailPassword)
        smtpObj.sendmail(fromMail, toMail, msg.as_string())
        print("email send")
        smtpObj.quit()
    except Exception as e:
        print(e)
        print("unable to send email")

def actionItem(case, url, data, emailList):
    if(case == 1):
        # success with non empty data
        if(macNotificationEnabled == False):
            print("system notification disabled")
        else:
            os.system(notificationStrSuccess)
        print(url)
        print(tabulate(data, headers=tableHeaders, tablefmt=style1))
        sendEmail(emailFrom, emailFromPassword, emailList, tabulate(data, headers=tableHeaders, tablefmt=style2))
    elif(case == 2):
        # success with empty data
        print(url)
        print(data)
    else:
        # failure
        if(macNotificationEnabled == False):
            print("system notification disabled")
        else:
            os.system(notificationStrFailure)
        print(url)
        print(data)
        # sendEmail(emailFrom, emailFromPassword, emailList, data)

def getAvailableSlots(districtId, date, minAge, emailList):

    requestURL = f'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id={districtId}&date={date}'
    requestHeaders = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'}
    print( 'fetching')
    r = requests.get(requestURL, headers=requestHeaders)
    if(r.status_code != 200):
        print(r)
        actionItem(3, requestURL,
                   f'unable to fetch, statusCode:{r.status_code}', emailList)
        return
    print('fetching complete')
    pyJson = r.json()
    covidCenters = pyJson['centers']
    notifyList = []
    for covidCenter in covidCenters:
        covidCenterName = covidCenter['name']
        covidCenterAddress = covidCenter['address']
        covidCenterSessions = covidCenter['sessions']
        for sessions in covidCenterSessions:
            covidCenterSessionsMinAgeLimit = sessions['min_age_limit']
            covidCenterSessionsAvailableCapacity = sessions['available_capacity']
            covidCenterSessionsDate = sessions['date']
            covidCenterSessionsSlots = sessions['slots']
            covidCenterSessionsVaccine = sessions['vaccine']
            if(covidCenterSessionsAvailableCapacity > capacityFilter and covidCenterSessionsMinAgeLimit == minAge and covidCenterSessionsVaccine == 'COVAXIN'):
                row = [covidCenterName, covidCenterAddress, covidCenterSessionsDate, covidCenterSessionsVaccine,
                       covidCenterSessionsAvailableCapacity, ','.join(covidCenterSessionsSlots), covidCenterSessionsMinAgeLimit]
                notifyList.append(row)

    if(len(notifyList)):
        actionItem(1, requestURL, notifyList, emailList)
    else:
        actionItem(2, requestURL, 'nothing-available', emailList)

def eventLoop():
    try:
        currentTime = datetime.datetime.now()
        nextDayTime = currentTime + datetime.timedelta(days=1)
        todaysDate = f'{currentTime.day}-{currentTime.month}-{currentTime.year}'
        tomorrowsDate = f'{nextDayTime.day}-{nextDayTime.month}-{nextDayTime.year}'
        # make call for today
        for location in locationMailList:
            getAvailableSlots(location[1], todaysDate, minAgeLimit, location[0])
        
    except:
        actionItem(3, 'unknown-url', 'unable to fetch', emailFrom)
    print(time.ctime())
    s.enter(eventLoopIntervalInSeconds, 1, eventLoop)

################################################################

def main():
    eventLoop()
    s.enter(eventLoopIntervalInSeconds, 1, eventLoop)
    s.run()

if __name__ == "__main__":
    main()

################################################################
