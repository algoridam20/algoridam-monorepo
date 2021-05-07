# 9th May 21 452001 notify vaccine availability
# to install dependencies on mac run -> pip3 install tabulate
# to start the script python3 nameOfFile.py



from tabulate import tabulate
import time
import sched
import datetime
import requests
import json
import os

# district codes https://github.com/bhattbhavesh91/cowin-vaccination-slot-availability/blob/main/district_mapping.csv
notificationStrSuccess = f" osascript -e 'display notification \"Check terminal\" with title \"Vaccine Slot Alert\" subtitle \"Success!!!\" sound name \"Submarine\"'"
notificationStrFailure = f" osascript -e 'display notification \"Check terminal\" with title \"Script Failure\" subtitle \"Error!!!\" sound name \"Submarine\"'"
indoreDistrictId = 314
minAgeLimit = 18
eventLoopIntervalInSeconds = 60

s = sched.scheduler(time.time, time.sleep)


def actionItem(case, url, data):
    if(case == 1):
        # success with non empty data
        os.system(notificationStrSuccess)
        print(url)
        print(data)
    elif(case == 2):
        # success with empty data
        print(url)
        print(data)
    else:
        # failure
        os.system(notificationStrFailure)
        print(url)
        print(data)


def getAvailableSlots(districtId, date, minAge):

    requestURL = f'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id={districtId}&date={date}'
    requestHeaders = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'}

    r = requests.get(requestURL, headers=requestHeaders)
    pyJson = r.json()
    if(r.status_code != 200):
        actionItem(3, requestURL,f"unable to fetch, statusCode:{r.status_code}")
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
            if(covidCenterSessionsAvailableCapacity >= 0 and covidCenterSessionsMinAgeLimit == minAge):
                row = [covidCenterName, covidCenterAddress, covidCenterSessionsDate, covidCenterSessionsVaccine,
                       covidCenterSessionsAvailableCapacity, ','.join(covidCenterSessionsSlots), covidCenterSessionsMinAgeLimit]
                notifyList.append(row)

    if(len(notifyList)):
        table = tabulate(notifyList, headers=['Name', 'Address', 'Date', 'Vaccine type', 'Available capacity', 'Slots', 'Min age'], tablefmt='fancy_grid')
        actionItem(1, requestURL, table)
    else:
        actionItem(2, requestURL, "no-data")


def eventLoop():
    try:
        currentTime = datetime.datetime.now()
        currentDay = currentTime.day
        currentMonth = currentTime.month
        currentYear = currentTime.year
        todaysDate = f'{currentDay}-{currentMonth}-{currentYear}'
        tomorrowsDate = f'{currentDay+1}-{currentMonth}-{currentYear}'
        # make call for today
        getAvailableSlots(indoreDistrictId, todaysDate, minAgeLimit)
        # and for tomorrow
        getAvailableSlots(indoreDistrictId, tomorrowsDate, minAgeLimit)
    except:
        actionItem(3, "unknown-url", "unable to fetch")
    print(time.ctime())
    s.enter(eventLoopIntervalInSeconds, 1, eventLoop)


def main():
    s.enter(eventLoopIntervalInSeconds, 1, eventLoop, ())
    s.run()


if __name__ == "__main__":
    main()
