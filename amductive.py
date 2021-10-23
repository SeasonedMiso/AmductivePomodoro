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
    "stnd": [20, ""],
}
cat2 = {
    "work": {
        "time": 25
    }
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


def stnd():
    pomoBool = True
    stndList = ["stnd"]
    timeIn = input("Pomo Time?\n")
    catergories["stnd"][0] = eval(timeIn)
    pomo(stndList)


def sett():
    global breakTime
    global longBreak
    global longBreakTime
    global longBreakCount
    breakTime = eval(input("Break Time?\n"))
    longBreakTime = eval(input("Long Break Time?\n"))
    longBreak = eval(input("Pomos before long break?\n"))
    longBreakCount = longBreak
    menu()

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
                if auto:
                    pomoStart(item)
                    continue
                inputObj = input("\nNext up is: " +
                                 item[0]+". Enter to start\n")
                match inputObj:
                    case "":
                        inBreak = False
                        pomoStart(item)
                    case "skip":
                        break
                    case "pass":
                        newItem = getItem(list[i])
                        while newItem == item and len(catergories[list[i]]) > 2:
                            newItem = getItem(list[i])
                        item = newItem
                    case "menu":
                        menu()
                        break
                    case "set":
                        sett()
                    case _:
                        print("unknown input")


def menu():
    global auto
    pomoBool = False
    inputObj = input("Enter command (h for help):\n")
    match inputObj:
        case "h":
            print(" work: starts pomodoro with study as focus\n go: starts normal pomodoro\n stnd:no flares, no playlists \n set: settings \n menu: return to menu\n p: pauses timer\n reset: resets timer\n")
            menu()
        case "work":
            work()
        case "go":
            go()
        case "night":
            night()
        case "stnd":
            stnd()
        case "set":
            sett()
        case "auto":
            auto = True if not auto else False
            print("auto = "+str(auto))
            menu()
        # elif inputObj == "p":
        #     pause()
        # elif inputObj == "reset":
        #     reset()
        case _:
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
