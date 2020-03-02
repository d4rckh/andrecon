import os

def runcmd(cmd, dev, dontremovenewlines):
    stream = os.popen("adb -s " + dev + " " + cmd)
    output = stream.read()
    if dontremovenewlines:
        pass
    else:
        output = output.replace('\n', '')
    return output

def getinfo(dev):
    data = {}
    
    data["fingerprint"] = runcmd("shell getprop ro.system.build.fingerprint", dev, False)
    data["codename"] = runcmd("shell getprop ro.product.vendor.name", dev, False)
    data["manufacturer"] = runcmd("shell getprop ro.product.vendor.manufacturer", dev, False)
    data["model"] = runcmd("shell getprop ro.product.vendor.model", dev, False)

    data["battery"] = runcmd("shell dumpsys battery", dev, True)
    return data