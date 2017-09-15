## Synopsis
This runs a script at work and home to automate save game backups to and from dropbox.

## Code Example
```
directories = {localpath0:remotepath0,localpath1:remotepath1,}

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

schedule.every().day.at("09:00").do(fromremote)
schedule.every().day.at("17:00").do(toremote)
```
## Motivation

I grew tired of manually moving a bunch of save game files to and from my dropbox on a daily basis.  This should eliminate much of that hassle, as a copy has been placed in the windows startup folder.

## Installation

You'll need to install schedule, a python module designed to run functions at specific times.

## License

Savesync is open source; it is licensed under GPLv3.

