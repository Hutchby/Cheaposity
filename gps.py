#!/usr/bin/env python3

import serial

""" The GPS transmits the following datas:
    - GNGLL
    - GNRMC
    - GNVTG
    - GNGGA
    - GNGSA
    - GPGSV
    - GLGSV

    We will use the GNRMC to get our position.
"""

class GPS:

    def __init__(self, serial_device):
        self.__serial = serial.Serial(serial_device)
        self.latitude = {}
        self.latitude["degrees"] = 0
        self.latitude["minutes"] = 0.0
        self.latitude["indicator"] = "N"
        self.longitude = {}
        self.longitude["degrees"] = 0
        self.longitude["minutes"] = 0.0
        self.longitude["indicator"] = "E"

    def __str__(self):
        return "{} | {}".format(self.get_latitude_str(),
                                self.get_longitude_str())

    def get_latitude_str(self):
        return "{}{}°{:.4f}".format(self.latitude["indicator"],
                                self.latitude["degrees"],
                                self.latitude["minutes"])

    def get_longitude_str(self):
        return "{}{}°{:.4f}".format(self.longitude["indicator"],
                                self.longitude["degrees"],
                                self.longitude["minutes"])

    def coordinate_decode(self, coordinate, attribute):
        degrees = int(coordinate / 100)
        minutes = coordinate % 100
        attribute["degrees"] = degrees
        attribute["minutes"] = minutes


    def gnrmc_decode(self, fields):
        if fields[2] == "V":
            print("Unable to get GPS data")
            return;
        self.coordinate_decode(float(fields[3]), self.latitude)
        self.latitude["indicator"] = fields[4]
        self.coordinate_decode(float(fields[5]), self.longitude)
        self.longitude["indicator"] = fields[6]

    def update(self):
        line = ""
        while not(line.startswith("$GNRMC")):
            line = bytes.decode(self.__serial.readline())
        self.gnrmc_decode(line.split(','))


if __name__ == "__main__":
    gps = GPS("/dev/ttyUSB0")
    while True:
        gps.update()
        print(gps)
