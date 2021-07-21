import subprocess

def screenshot(name, dir = ""):
    if(dir != ""):
        dir = dir + "/"
    cmd = "adb exec-out screencap -p > " + dir  + name + ".png"
    lis = subprocess.run(cmd, shell=True, capture_output=True)
    if(lis.returncode == 1):
        print(lis.stderr)
    return lis.returncode

def create_dir(parent = "", child = ""):
    '''If child is empty then only base directory is created, else child directory'''
    if(child == ""):
        lis = subprocess.run('md '+ parent, shell=True, capture_output=True)
    else:
        lis = subprocess.run('md '+ parent + '\\'+ child , shell=True, capture_output=True)
    if (lis.returncode == 1):
        print(lis.stderr)
    return lis.returncode

def event(keyevent):
    cmd = "adb shell input keyevent " + str(keyevent)
    lis = subprocess.run(cmd, shell=True, capture_output=True)
    if (lis.returncode == 1):
        print(lis.stderr)
    return lis.returncode

def wake_up():
    event(224)

def tab(times = 1):
    for x in range(0, times):
        event(61)

def enter(times = 1):
    for x in range(0, times):
        event(66)

def back(times = 1):
    for x in range(0, times):
        event(4)

def clear(times = 1):
    for x in range(0, times):
        event(28)


def input_text(text):
    cmd = "adb shell input text " + text
    lis = subprocess.run(cmd, shell=True, capture_output=True)
    if (lis.returncode == 1):
        print(lis.stderr)
    return lis.returncode

def swipe_coord(intx = 0, inty = 500, finx = 500, finy = 500, time = 100):
    '''Default is Swipe Left'''
    cmd = "adb shell input swipe " + str(intx) + " " + str(inty) + " " + str(finx) + " " + str(finy) + " " + str(time)
    lis = subprocess.run(cmd, shell=True, capture_output=True)
    if (lis.returncode == 1):
        print(lis.stderr)
    return lis.returncode

def swipe(typ):
    if(typ == "left"):
        swipe_coord()
    elif(typ == "right"):
        swipe_coord(500, 500, 0, 500, 100)
    elif(typ == "up"):
        swipe_coord(500, 1000, 500, 0, 100)
    else:
        swipe_coord(500, 0, 500, 1200, 100)

def tap(x, y):
    cmd = "adb shell input tap " + str(x) + " " + str(y)
    lis = subprocess.run(cmd, shell=True, capture_output=True)
    if (lis.returncode == 1):
        print(lis.stderr)
    return lis.returncode

def openapp(packagename):
    cmd = "adb shell monkey -p " +  packagename + " -c android.intent.category.LAUNCHER 1"
    lis = subprocess.run(cmd, shell=True, capture_output=True)
    if (lis.returncode == 1):
        print(lis.stderr)
    return lis.returncode

def checkdevice():
    cmd = "adb devices"
    lis = subprocess.run(cmd, shell=True, capture_output=True)
    if (lis.returncode == 1):
        print(lis.stderr)
    else:
        print(lis.stdout)
    return lis.returncode

# input_text("Hello")
# clear()