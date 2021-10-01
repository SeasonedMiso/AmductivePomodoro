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
pomoBool = False
inBreak = False
auto = False

# userData
longBreak = 3
breakTime = 5
longBreakTime = 10
longBreakCount = longBreak
# Each catergory is formated as: time for catergory then items, where each item is prefixed by its weighting
catergories = {
    "work": [25, "[10]study"],
    "lit": [20, "[5]book", "[5]vn"],
    "hobby": [15, "[7]music", "[2]draw", "[4]skate"],
    "fun": [20, "[2]non texty game", "[5]texty game", "[5]youtube", "[2]anime"],
}


def work():
    pomoBool = True
    workList = ["work", "lit", "work", "hobby", "work", "fun"]
    pomo(workList)


def go():
    pomoBool = True
    goList = ["lit", "hobby", "lit", "fun"]
    pomo(goList)


def night():
    pomoBool = True
    goList = ["lit", "fun"]
    pomo(goList)

# Non-user data


def getItem(cat):
    item = random.choice(catergories[cat][1::])
    acti = re.sub("[\(\[].*?[\)\]]", "", item)
    time = catergories[cat][0]
    return [acti, time]


def pomoStart(item):
    global count
    global longBreakCount
    timeLeft = item[1]*60
    while timeLeft > 0:
        # print(timeLeft)
        sys.stdout.write("\r")
        sys.stdout.write(str(datetime.timedelta(seconds=timeLeft)))
        sys.stdout.flush()
        time.sleep(1)
        timeLeft -= 1
    count += 1
    longBreakCount -= 1

    notification.notify(
        title="Good work!",
        message="\nTake a break! You have completed " +
        str(count) + " pomodoros so far. " +
        str(longBreakCount) + " until long break"
    )
    if longBreakCount > 0:
        print("\nTake a break! You have completed " + str(count) +
              " pomodoros so far. " + str(longBreakCount) + " until long break")
        timeLeft = breakTime*60

        while timeLeft > 0:
            # print(timeLeft)
            sys.stdout.write("\r")
            sys.stdout.write(str(datetime.timedelta(seconds=timeLeft)))
            sys.stdout.flush()
            time.sleep(1)
            timeLeft -= 1

        notification.notify(
            title="Back to work!",
            message="Check next task",
        )
        print("\nBreak Over!\n")
    else:
        print("\nLONG BREAK! You have completed " +
              str(count) + " pomodoros so far\n")
        timeLeft = longBreakTime*60
        longBreakCount = longBreak
        while timeLeft > 0:
            sys.stdout.write("\r")
            sys.stdout.write(str(datetime.timedelta(seconds=timeLeft)))
            sys.stdout.flush()
            time.sleep(1)
            timeLeft -= 1

        notification.notify(
            title="Back to work!",
            message="Try doing another pomodoro...",
        )


def pomo(list):
    while pomo:
        for i in range(len(list)):
            item = getItem(list[i])
            # print("\n"+item[0])
            inBreak = True
            while inBreak:
                if auto == False:
                    inputObj = input("\nNext up is: " +
                                     item[0]+". Enter to start\n")
                    if inputObj == "":
                        inBreak = False
                        pomoStart(item)
                    elif inputObj == "skip":
                        break
                    elif inputObj == "pass":
                        newItem = getItem(list[i])
                        while newItem == item and len(catergories[list[i]]) > 2:
                            newItem = getItem(list[i])
                        item = newItem
                    elif inputObj == "menu":
                        menu()
                        break
                    else:
                        print("unknown input")
                else:
                    pomoStart(item)


def menu():
    global auto
    pomoBool = False
    inputObj = input("Enter command (h for help):\n")
    if input == "h":
        print("work: starts pomodoro with study as focus\n go: starts normal pomodoro\n menu: return to menu\n p: pauses timer\n reset: resets timer\n")
    elif inputObj == "work":
        work()
    elif inputObj == "go":
        go()
    elif inputObj == "night":
        night()
    elif inputObj == "auto":
        if auto == False:
            auto = True
            print("auto=true")
            menu()
        else:
            auto = False
            print("auto=false")
            menu()
    # elif inputObj == "p":
    #     pause()
    # elif inputObj == "reset":
    #     reset()
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
