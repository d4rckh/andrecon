from banner import banner as printBanner
from getdevices import getdevices
import sys


printBanner()

if sys.argv[1] == "devices":
    print("Connected devices:")
    print(getdevices())
elif sys.argv[1] == "info":
    