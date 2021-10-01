#! python3
import random
import re
import time
from plyer import notification
import sys
import datetime

global count
count = 0
workMode = False
longBreak = 3
longBreakCount=longBreak
pomoBool = False
breakTime = 5
longBreakTime = 20

# Each catergory is formated as: time for catergory then items, where each item is prefixed by its weighting
catergories={
"work" : [25,"[10]study"],
"lit" : [10,"[5]book","[5]vn"],
"hobby" : [30,"[7]music","[2]draw","[4]skate"],
"fun" : [30,"[2]non texty game", "[5]texty game", "[5]youtube", "[2]anime"],
}
def getItem(cat):
    item = random.choice(catergories[cat][1::])
    acti = re.sub("[\(\[].*?[\)\]]", "", item)
    time = catergories[cat][0]
    return [acti, time]    

def pomo(list):
    global count
    global longBreakCount
    while pomo:

        for i in range(longBreak):
            item = getItem(list[i])
            timeLeft = item[1]*60
            print("\n"+item[0])

            while timeLeft>0:
                # print(timeLeft)
                sys.stdout.write("\r")
                sys.stdout.write(str(datetime.timedelta(seconds=timeLeft))) 
                sys.stdout.flush()
                time.sleep(1)
                timeLeft-=1
            count += 1
            longBreakCount -= 1

            notification.notify(
                title = "Good work!",
                message = "\nTake a break! You have completed " + str(count) + " pomodoros so far. " + str(longBreakCount)+ " until long break"
            )
            if longBreakCount>0:
                print("\nTake a break! You have completed " + str(count) + " pomodoros so far. " + str(longBreakCount)+ " until long break")
                timeLeft=breakTime*60

                while timeLeft>0:
                    # print(timeLeft)
                    sys.stdout.write("\r")
                    sys.stdout.write(str(datetime.timedelta(seconds=timeLeft))) 
                    sys.stdout.flush()
                    time.sleep(1)
                    timeLeft-=1

                notification.notify(
                    title = "Back to work!",
                    message = "Try doing another pomodoro...",
                )
                print("\nBreak Over!\n")
            else: 
                print("\nLONG BREAK! You have completed " + str(count) + " pomodoros so far\n")
                timeLeft=longBreakTime*60
                longBreakCount=longBreak

                while timeLeft>0:
                    # print(timeLeft)
                    sys.stdout.write("\r")
                    sys.stdout.write(str(datetime.timedelta(seconds=timeLeft))) 
                    sys.stdout.flush()
                    time.sleep(1)
                    timeLeft-=1

                notification.notify(
                    title = "Back to work!",
                    message = "Try doing another pomodoro...",
                )

def work():
    pomoBool = True
    workList = ["work", "lit", "work", "hobby", "work", "fun"]
    pomo(workList)

def go():
    pomoBool = True
    goList = ["lit", "hobby", "lit", "fun"]
    pomo(goList)

def menu():
    inputObj = input("Enter command (h for help):\n")
    if input == "h":
        print("work: starts pomodoro with study as focus\n go: starts normal pomodoro\n menu: return to menu\n p: pauses timer\n reset: resets timer\n")
    elif inputObj == "work":
        work()
    elif inputObj == "go":
        go()
    # elif input == "menu":
    #     menu()
    elif inputObj == "p":
        pause()
    elif inputObj == "reset":
        reset()
    else:
        print("unknown command")
        menu()

def pause():
    print(" ")

def reset():
    print(" ")

if __name__ == "__main__":
    menu()
    while True:
        pass