#!/usr/bin/python
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#|R|a|s|p|b|e|r|r|y|P|i|-|S|p|y|.|c|o|.|u|k|
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#
# ultrasonic_2.py
# Measure distance using an ultrasonic module
# in a loop.
#
# Author : Matt Hawkins
# Date   : 28/01/2013

# -----------------------
# Import required Python libraries
# -----------------------
import time
import RPi.GPIO as GPIO

class Sonar:
    def __init__(self):
        self.trigger = 18
        self.echo    = 23
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.trigger,GPIO.OUT)  # Trigger
        GPIO.setup(self.echo,GPIO.IN)      # Echo
        GPIO.output(self.trigger, False)
 
    def measure(self):
        # This function measures a distance
        GPIO.output(self.trigger, True)
        time.sleep(0.00001)
        GPIO.output(self.trigger, False)
        start = time.time()
        stop = start

        while GPIO.input(self.echo)==0:
            start = time.time()

        while GPIO.input(self.echo)==1:
            stop = time.time()

        elapsed = stop-start
        distance = (elapsed * 34300) / 2

        return distance

    def measure_average(self):
        # This function takes 3 measurements and
        # returns the average.
        print("sonar: measure 1")
        distance1 = self.measure()
        time.sleep(0.1)
        print("sonar: measure 2")
        distance2 = self.measure()
        time.sleep(0.1)
        print("sonar: measure 3")
        distance3 = self.measure()
        distance = distance1 + distance2 + distance3
        distance = distance / 3
        return distance
