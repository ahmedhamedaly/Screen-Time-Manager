import sys
import time
import json

if sys.platform in ['Windows', 'win32', 'cygwin']:
    import win32gui
    windows = True
elif sys.platform in ['Mac', 'darwin', 'os2', 'os2emx']:
    from AppKit import NSWorkspace
    mac = True
else:
    print("No Support for your current OS")


def getCurrentWindow():
    if windows:
        c = win32gui.GetWindowText(win32gui.GetForegroundWindow())
        return c.split('-')[-1].lstrip(' ')
    elif mac:
        return (NSWorkspace.sharedWorkspace().activeApplication()['NSApplicationName'])
    else:
        return None


def existingApp(window):
    with open('usage.json') as f:
        jDict = json.loads(f.read())
        
        for i in jDict:
            if i['name'] == window:
                return True
        return False


def openUsage():
    with open('usage.json') as f:
        jDict = json.loads(f.read())
        f.close()
    return jDict

def newApp(currentWindow, lastOpened, timeSpent):
    with open('usage.json') as f:
        jDict = json.loads(f.read())

def newEntry(currentWindow, lastOpened, timeSpent):
    usage = openUsage()

    with open('usage.json', "w") as f:
        usage.append({
            "name": currentWindow,
            "time": {
                "last_opened": lastOpened,
                "time_spent": timeSpent
            }
        })

        json.dump(usage, f)
        f.close()
    

def log(currentWindow, lastOpened, timeSpent):
    if existingApp(currentWindow):
        newApp(currentWindow, lastOpened, timeSpent)
    else:
        newEntry(currentWindow, lastOpened, timeSpent)


def main():
    prevWindow = None
    prevTime = None

    while True:
        
        currWindow = getCurrentWindow()

        if prevWindow != currWindow:
            if prevTime != None:
                timeSpent = time.time() - prevTime

                #print(timeSpent)  
                #print(currWindow)

                if timeSpent > 1:
                    log(prevWindow, time.time(), timeSpent)

                prevTime = time.time()
                prevWindow = currWindow
            else:
                prevTime = time.time()


if __name__ == "__main__":
    main()