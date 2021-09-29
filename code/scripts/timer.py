import os
import sys
import time
import sched



def notificationStr(localtime, interval):
    return f" osascript -e 'display notification \"{localtime.tm_hour}:{localtime.tm_min}\" with title \"Ping\" subtitle \"next alert in {(interval)} mins\" sound name \"Submarine\"'"


def notificationStr2(localtime):
    return f" osascript -e 'display notification \"{localtime.tm_hour}:{localtime.tm_min}\" with title \"Ping\" subtitle \"all timers complete\" sound name \"Submarine\"'"


s = sched.scheduler(time.time, time.sleep)


def eventLoop(index,x):
    
    if(len(sys.argv) <= index):
        print("timers complete")
        os.system(notificationStr2(time.localtime()))
        sys.exit()

    interval = (int)(sys.argv[index])
    
    try:
        print(f"Alert time : {time.ctime()}. Next Alert in {interval} mins")
        os.system(notificationStr(time.localtime(), interval))
    except:
        print("graceful shutdown")
        sys.exit()
    
    s.enter(interval*60, 1, eventLoop,(index+1,x))

#######################################################################


def main():
    s.enter(0, 1, eventLoop,(1,2))
    s.run()


if __name__ == "__main__":
    main()


#######################################################################
# i don't know python                                                 #
# use the following command to run script                             #
# python3 timer.py 1 5 20 1 5 20 5                                    #
# script will alert with time interval provided as command line args  #
#######################################################################