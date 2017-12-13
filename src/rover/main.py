import rover
import signal
import time
import sys
import RPi.GPIO as GPIO
from threading import Thread

def signal_handler(signal, frame):
    print("CLEAN UP GPIO")
    time.sleep(1) # waiting the end of rover thread
    rover.left_motor.stop()
    time.sleep(1) # waiting the end of rover thread
    rover.right_motor.stop()
    GPIO.cleanup()
    print("EXIT")
    sys.exit(0)

if __name__ == '__main__':
    rover = rover.Rover()
    signal.signal(signal.SIGINT, signal_handler)
    thread = Thread(target=rover.run())
    thread.start()
    signal.pause()
