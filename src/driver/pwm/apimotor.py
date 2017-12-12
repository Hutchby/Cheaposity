from __future__ import division
import time
import signal
import sys

# Import the PCA9685 module.
from i2c import PCA9685

class Motor:
    def __init__(self, channel, polarity=False, pullspeed=0, coeff=1):
        self.channel = channel
        self.adapwm = PCA9685.PCA9685()
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

    def pwm(self, speed):
        speed = self.topwm(speed)
        self.speed = speed * self.coeff
        self.adapwm.set_pwm(self.channel, 0, int(self.speed)) # * self.coeff
        print("channel: ", self.channel, " pwm:", self.speed, "(", speed, ")")
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
