from __future__ import division
import time
from i2c import PCA9685

class servoMG996R:
    def __init__(self, channel=0, pulse=1):
        self.min = 150
        self.max = 600
        self.pwm = PCA9685.PCA9685()
        self.channel = channel
        pulse_length = 1000000
        pulse_length //= 60
        pulse_length //= 4096
        pulse *= 1000
        pulse //= pulse_length
        self.pwm.set_pwm_freq(60)

    def rotate(self, value):
        print("servo: rotate {}".format(value))
        self.pwm.set_pwm(self.channel, 0, ((int)((self.max - self.min) * value) + self.min))
        time.sleep(1)
