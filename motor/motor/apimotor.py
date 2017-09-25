import RPi.GPIO as GPIO
import time
import signal
import sys

class Motor:
    def __init__(self, pin_speed, pin_pos_mot, pin_neg_mot,
                 polarity=False, pullpos=0, pullneg=0, pullspeed=0, coeff=1)
        #pins
        self.pinspeed = pin_speed
        self.pwmspeed = GPIO.PWM(pin_speed, 1)
        self.posmot = pin_pos_mot
        self.negmot = pin_neg_mot
        # default rotation direction
        self.polarity = polarity
        # if a motor is slower or faster than other,
        # set a coeff to reduce the stronger one
        self.coeff = coeff
        # to regulate pull up/down on relay input
        self.pullp = pullpos
        self.pulln = pullneg
        self.pulls = pullspeed
        GPIO.setup(self.pinspeed, GPIO.OUT)
        GPIO.setup(self.posmot, GPIO.OUT)
        GPIO.setup(self.negmot, GPIO.OUT)
        return

    def stop():
        self.pwmspeed.stop()
        return

    def start():
        self.pwmspeed.start(speed)
        return

    def reverse():
        if polarity:
            GPIO.output(self.negmot, GPIO.LOW)
            GPIO.output(self.posmot, GPIO.HIGH)
        else:
            GPIO.output(self.negmot, GPIO.LOW)
            GPIO.output(self.posmot, GPIO.HIGH)

        return

    def direction

    def reset():
        self.stop()

        return
