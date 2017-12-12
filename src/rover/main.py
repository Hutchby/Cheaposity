import rover
import signal
import sys
import RPi.GPIO as GPIO
from threading import Thread

def signal_handler(signal, frame):
    print("CLEAN UP GPIO")
    GPIO.cleanup()
    print("EXIT")
    sys.exit(0)

if __name__ == '__main__':
    rover = rover.Rover()
    signal.signal(signal.SIGINT, signal_handler)
    thread = Thread(target=rover.run())
    thread.start()
    signal.pause()
