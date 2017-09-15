from distutils.dir_util import copy_tree
import schedule
from time import sleep


directories = {r"C:\Users\Stormtrooper\AppData\LocalLow\Ludeon Studios\RimWorld by Ludeon Studios":
               r"C:\Users\Stormtrooper\Dropbox\Saves\RimWorld",
               r"C:\Users\Stormtrooper\Documents\Klei\OxygenNotIncluded":
               r"C:\Users\Stormtrooper\Dropbox\Saves\ONI"}


def toremote():
    for location in list(directories.items()):
        print("Copying saves...")
        print("From " + location[0])
        print("To " + location[1])

        copy_tree(location[0], location[1])


def fromremote():
    for location in list(directories.items()):
        print("Copying saves...")
        print("From " + location[1])
        print("To " + location[0])

        copy_tree(location[1], location[0])


def activitycheck():
    print("Active...")


schedule.every().day.at("17:45").do(toremote)

schedule.every().monday.at("04:20").do(fromremote)
schedule.every().thursday.at("04:20").do(fromremote)
schedule.every().friday.at("04:20").do(fromremote)

schedule.every().hour.do(activitycheck)


def main():
    while True:
        try:
            while True:
                schedule.run_pending()
                sleep(60)
        except:
            print("****************")
            print("Exception thrown")
            print("****************")
            sleep(60)
        else:
            break


if __name__ == '__main__':
    main()
