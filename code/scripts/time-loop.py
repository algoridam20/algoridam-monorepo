import os
import sys
import time
import sched
import datetime


eventLoopIntervalInMins = 21


def notificationStr(localtime, interval):
    return f" osascript -e 'display notification \"{localtime.tm_hour}:{localtime.tm_min}\" with title \"Ping\" subtitle \"next alert in {(int)(interval)}mins\" sound name \"Submarine\"'"


s = sched.scheduler(time.time, time.sleep)


def eventLoop(a,b):
    interval = a
    if(a >= eventLoopIntervalInMins):
         interval = eventLoopIntervalInMins
    
    try:
        print(f"{time.ctime()}  {interval}")
        os.system(notificationStr(time.localtime(), interval))
    except:
        print("graceful shutdown")
        sys.exit()
    s.enter(interval*60, 1, eventLoop, (b, a+b))

################################################################


def main():
    s.enter(0, 1, eventLoop, (0, 1))
    s.run()


if __name__ == "__main__":
    main()


################################################################
