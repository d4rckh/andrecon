from banner import banner as printBanner
from getdevices import getdevices
from getinfo import getinfo
import sys


printBanner()

if sys.argv[1] == "devices":
    print("Connected devices:")
    print(getdevices())
    exit()

if sys.argv[1] == "device":
    if sys.argv[3] == "placeholder":
        pass
    else:
        dev = sys.argv[2]
        i = getinfo(dev)
        print("")
        print("Fingerprint: " + i["fingerprint"])
        print("Manufacturer: " + i["manufacturer"])
        print("Model: " + i["model"])
        print("Codename: " + i["codename"])
        print("")
        print(i["battery"])
        