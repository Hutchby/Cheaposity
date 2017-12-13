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
        self.stop()

    # Apply an algo to correct ignore a death zone around zero
    def algo(self, speed):
        if speed == 0:
            return 0
        sign = 1
        if speed < 0:
            sign = -1
        return sign * 20 + speed * 4 / 5

    # Convert speed (+-100) to a pwm value for motor)
    def topwm(self, speed):
        return self.pwmmean + self.pwmwide * speed / 200

    # Apply the desire speed to the motor
    def run(self, speed):
        speed = speed * self.coeff
        speed = self.algo(speed)
        pwm   = self.topwm(speed)
        self.adapwm.set_pwm(self.channel, 0, int(pwm))
        print("channel: ", self.channel, " speed:", speed, " pwm:", pwm)
        return

    def start(self, speed):
        self.start(speed)
        return

    # Apply the null speed rotation
    def stop(self):
        self.adapwm.set_pwm(self.channel, 0, int (self.pwmmean))
        print("channel: ", self.channel, " stop!")


# Some Tests.
if __name__ == "__main__":
    print("Demo: Motor test")
    M1 = Motor(channel=14, coeff=1)
    M2 = Motor(channel=15, coeff=1)
    #rot = int(input("rotation : "))
    M1.run(50)
    M2.run(50)
    time.sleep(10)
    M1.stop()
    M2.stop()
