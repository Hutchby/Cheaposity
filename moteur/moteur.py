import RPi.GPIO as GPIO
import time
import signal
import sys


GPIO.setmode(GPIO.BCM)

pinM1=17
pinM2=27


def close(signal, frame):
        print("\nTurning off ultrasonic distance detection...\n")
        p.stop()
        GPIO.cleanup()
        sys.exit(0)


signal.signal(signal.SIGINT, close)
GPIO.setup(pinM1, GPIO.OUT)
#GPIO.setup(pinM2, GPIO.OUT)


p = GPIO.PWM(pinM1, 10)
p.start(100) #ici, rapport_cyclique vaut entre 0.0 et 100.0

while True:
        continue
