import sys

if sys.platform in ['Windows', 'win32', 'cygwin']:
    import win32gui
    windows = True
elif sys.platform in ['Mac', 'darwin', 'os2', 'os2emx']:
    from AppKit import NSWorkspace
    mac = True
elif sys.platform in ['linux', 'linux2']:
    import linux
    linux = True
else:
    print("No Support for your current OS")

prevWindow = None

def getCurrentWindow():
    if windows:
        c = win32gui.GetWindowText(win32gui.GetForegroundWindow())
        return c.split('-')[-1].lstrip(' ')
    elif mac:
        return (NSWorkspace.sharedWorkspace().activeApplication()['NSApplicationName'])
    elif linux:
        return linux.get_active_window_x()
    else:
        return None

while True:
    
    currWindow = getCurrentWindow()

    if prevWindow != currWindow:
        prevWindow = currWindow        
        print(currWindow)