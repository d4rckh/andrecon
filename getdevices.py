import os

def getdevices():
    stream = os.popen('adb devices')
    output = stream.read()
    lines = output.split('\n')
    devices = []
    for line in lines:
        if line == "\n" or line == "" or line == " " or line == "List of devices attached":
            pass
        else:
            devices.append(line.split('\t')[0])
    return devices