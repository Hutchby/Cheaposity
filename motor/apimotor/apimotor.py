import RPi.GPIO as GPIO
import time
import signal
import sys

class Motor:
    def __init__(self, pin_speed, pin_pos_mot, pin_neg_mot,
                 polarity=False, pullpos=0, pullneg=0, pullspeed=0, coeff=1):
        #pins
        if GPIO.getmode() == None:
            GPIO.setmode(GPIO.BCM)
        self.pinspeed = pin_speed
        self.posmot = pin_pos_mot
        self.negmot = pin_neg_mot
        GPIO.setup(self.posmot,   GPIO.OUT)
        GPIO.setup(self.negmot,   GPIO.OUT)
        GPIO.setup(self.pinspeed, GPIO.OUT)
        self.pwmspeed = GPIO.PWM(pin_speed, 1)
        # default rotation direction
        self.polarity = polarity
        # if a motor is slower or faster than other,
        # set a coeff to reduce the stronger one
        self.coeff = coeff
        # to regulate pull up/down on relay input
        self.pullp = pullpos
        self.pulln = pullneg
        self.pulls = pullspeed
        return

    def polarity(pol):
        if pol:
            GPIO.output(self.negmot, GPIO.LOW)
            GPIO.output(self.posmot, GPIO.HIGH)
        else:
            GPIO.output(self.negmot, GPIO.LOW)
            GPIO.output(self.posmot, GPIO.HIGH)
        return

    def run(self, speed, pol):
        self.polarity(pol)
        self.pwmspeed.start(speed * coeff)
        return

    def stop():
        self.pwmspeed.stop()
        return

    def start():
        self.pwmspeed.start(speed)
        return

    def reset():
        self.stop()

        return
