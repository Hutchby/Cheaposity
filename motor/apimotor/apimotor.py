from __future__ import division
import RPi.GPIO as GPIO
import time
import signal
import sys

# Import the PCA9685 module.
import Adafruit_PCA9685

class Motor:
    def __init__(self, pin, polarity=False, pullspeed=0, coeff=1):
        if GPIO.getmode() == None:
            GPIO.setmode(GPIO.BCM)
        self.pin = pin
        self.adapwm = Adafruit_PCA9685.PCA9685()
        self.adapwm.set_pwm_freq(60)
        self.pwmmin = 250
        self.pwmmax = 500
        self.pwmmean = int((self.pwmmax + self.pwmmin) / 2)
        self.coeff = coeff
        return

    
    def convert(self, speed):
        return self.pwmmean + int((self.pwmmax - self.pwmmin) * speed / 200)

    
    def pwm(self, speed):
        self.speed = speed
        self.adapwm.set_pwm(self.pin, 0, self.convert(speed)) # * self.coeff
        return

    
    def start(self, speed):
        self.pwm(speed)
        #print("pin: ", self.pin, " pwm:", self.convert(speed), "(", speed, ")")
        return

    
    def stop(self):
        self.start(0)
        return

    
    def run(self, speed):
        self.start(speed)
        return
