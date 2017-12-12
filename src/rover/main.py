import rover
import signal
import time
import sys
import RPi.GPIO as GPIO
from threading import Thread

def signal_handler(signal, frame):
    print("CLEAN UP GPIO")
    GPIO.cleanup()
    rover.left_motor.pwm(0)
    rover.right_motor.pwm(0)
    time.sleep(1)
    print("EXIT")
    sys.exit(0)

if __name__ == '__main__':
    rover = rover.Rover()
    signal.signal(signal.SIGINT, signal_handler)
    thread = Thread(target=rover.run())
    thread.start()
    signal.pause()
