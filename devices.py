from random import choice
import string
from tabulate import tabulate
from operator import itemgetter
from pprint import pprint

devices = []  # create empty list for holding devices

# For loop to create large number of devices
for index in range(5):

    device = dict()  # Create device dictionary

    # Generating random devices names
    device["Name"] = (
        choice(["R2", "R3", "R7", "R9", "R21"])
        + choice(["K", "S"])
        + choice(string.ascii_letters)
    )

    # Generating random vendor using choice, choices of "cisco", "juniper" and "artista"
    device["Vendor"] = choice(["Cisco", "Juniper", "Artista"])

    if device["Vendor"] == "Cisco":
        device["OS"] = choice(["iOS", "iOSXR", "iOSXE", "NEXUS"])
        device["Version"] = choice(["12.34(S).01", "14.001T", "9.12.56"])

    elif device["Vendor"] == "Juniper":
        device["OS"] = choice(["JUNOS"])
        device["Version"] = choice(["1.56.89", "12.45.656", "J12.35.4"])

    elif device["Vendor"] == "Artista":
        device["OS"] = "EOS"
        device["Version"] = choice(["2.45", "11.56.73", "J90.234"])

    device["I.P."] = "192.168.10." + str(index)

    # nicely formatted print of this one device
    print()
    for key, value in device.items():
        print(f"{key:>15s} : {value}")

    # add this device to the list of devices
    devices.append(device)

# Use pprint to print data as it is
print("\n-------------DEVICES AS LIST OF DICTIONARY----------------\n")
pprint(devices)

# use "Tabulate" to print table of devices
print("\n-----------------SORTED DEVICES IN TABULAR FORMAT--------------------\n")

print(tabulate(sorted(devices, key=itemgetter("Vendor", "OS", "Version")), headers="keys"))
print("\n")
