# 9th May 21 314 notify vaccine availability
# to install dependencies on mac run -> pip3 install tabulate
# to start the script python3 nameOfFile.py

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from tabulate import tabulate
import time
import sched
import datetime
import requests
import json
import os

emailFrom = 'ridammj@yahoo.com'
emailFromPassword = 'xx'
emailTo = ['ridammj@gmail.com']

emailNotificationEnabled = True
macNotificationEnabled = True
tableHeaders = ['Name', 'Address', 'Date', 'Vaccine type','Available capacity', 'Slots', 'Min age']
style1 = 'fancy_grid'
style2 = 'html'
notificationStrSuccess = f" osascript -e 'display notification \"Check terminal\" with title \"Vaccine Slot Alert\" subtitle \"Success!!!\" sound name \"Submarine\"'"
notificationStrFailure = f" osascript -e 'display notification \"Check terminal\" with title \"Script Failure\" subtitle \"Error!!!\" sound name \"Submarine\"'"

indoreDistrictId = 314
minAgeLimit = 18
eventLoopIntervalInSeconds = 360

################################################################

s = sched.scheduler(time.time, time.sleep)

def sendEmail(fromMail,fromMailPassword,toMail,data):
    if(emailNotificationEnabled == False):
         print("email notification disabled")
         return
    try:
        msg = MIMEMultipart('alternative')
        msg['Subject'] = 'Covid Vaccine Availability Alert!!'
        msg['From'] = emailFrom
        msg['To'] = emailTo[0]
        text = "\n\n"
        html = f'<html><head></head><body><p>Hi!<br>Please find below available centers<br><br>{data}</p></body></html>'
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

def actionItem(case, url, data):
    if(case == 1):
        # success with non empty data
        if(macNotificationEnabled == False):
            print("email notification disabled")
        else:
            os.system(notificationStrSuccess)
        print(url)
        print(tabulate(data, headers=tableHeaders, tablefmt=style1))
        sendEmail(emailFrom, emailFromPassword, emailTo, tabulate(data, headers=tableHeaders, tablefmt=style2))
    elif(case == 2):
        # success with empty data
        print(url)
        print(data)
    else:
        # failure
        if(macNotificationEnabled == False):
            print("email notification disabled")
        else:
            os.system(notificationStrFailure)
        print(url)
        print(data)
        sendEmail(emailFrom, emailFromPassword, emailTo, data)

def getAvailableSlots(districtId, date, minAge):

    requestURL = f'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id={districtId}&date={date}'
    requestHeaders = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'}

    r = requests.get(requestURL, headers=requestHeaders)
    pyJson = r.json()
    if(r.status_code != 200):
        actionItem(3, requestURL,f'unable to fetch, statusCode:{r.status_code}')
        return
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
            if(covidCenterSessionsAvailableCapacity > 0 and covidCenterSessionsMinAgeLimit == minAge):
                row = [covidCenterName, covidCenterAddress, covidCenterSessionsDate, covidCenterSessionsVaccine,
                       covidCenterSessionsAvailableCapacity, ','.join(covidCenterSessionsSlots), covidCenterSessionsMinAgeLimit]
                notifyList.append(row)

    if(len(notifyList)):
        actionItem(1, requestURL, notifyList)
    else:
        actionItem(2, requestURL, 'no-data')

def eventLoop():
    try:
        currentTime = datetime.datetime.now()
        nextDayTime = currentTime + datetime.timedelta(days=1)
        todaysDate = f'{currentTime.day}-{currentTime.month}-{currentTime.year}'
        tomorrowsDate = f'{nextDayTime.day}-{nextDayTime.month}-{nextDayTime.year}'
        # make call for today
        getAvailableSlots(indoreDistrictId, todaysDate, minAgeLimit)
        # and for tomorrow
        getAvailableSlots(indoreDistrictId, tomorrowsDate, minAgeLimit)
    except:
        actionItem(3, 'unknown-url', 'unable to fetch')
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
