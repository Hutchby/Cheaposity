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
        self.pwmmean = (self.pwmmax + self.pwmmin) / 2
        self.pwmwide = self.pwmmax - self.pwmmin
        self.coeff = coeff
        return

    def algo(self, speed):
        if speed == 0:
            return 0
        sign = 1
        if speed < 0:
            sign = -1
        return sign * 20 + speed * 4 / 5


    def topwm(self, speed):
        return self.pwmmean + self.pwmwide * speed / 200

    #var: speed = +-100%
    def pwm(self, speed):
        #speed = self.algo(speed)
        speed = self.topwm(speed)
        self.speed = speed * self.coeff
        self.adapwm.set_pwm(self.pin, 0, int(self.speed)) # * self.coeff
        print("pin: ", self.pin, " pwm:", self.speed, "(", speed, ")")
        return


    def start(self, speed):
        self.pwm(speed)
        return


    def stop(self):
        self.start(0)
        return


    def run(self, speed):
        self.start(speed)
        return


if __name__ == '__main__':
    print("Demo: Motor test")

    M1=Motor(pin=14, coeff=1)
    M2=Motor(pin=15, coeff=1)

    #'''
    while True:
        #rot = int(input("rotation : "))
        speed1 = int(input("M1 : "))
        speed2 = int(input("M2 : "))

        M1.pwm(speed1)
        M2.pwm(speed2)
