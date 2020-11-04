import win32gui as win

prevWindow = None

while True:
    currWindow = win.GetWindowText(win.GetForegroundWindow())
    currWindow = currWindow.split('-')[-1].lstrip(' ')

    if prevWindow != currWindow and currWindow != " ":
        prevWindow = currWindow        
        print(currWindow)