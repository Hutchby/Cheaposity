import sys
import time
import apimotor
import signal
from pathlib import Path
from evdev import InputDevice, categorize, ecodes

"""
Motor's disposition for rover's wheel
    Front
M1 ------- M2
|           |
|     ^     |
|     |     |
|           |
M3 ------- M4
    Back

mconf is the number of motor used
0: M1 & M4 (default)
1: M2 & M3
2: all motors
"""

def signal_handler(signal, frame):
    print('You pressed Ctrl+C!')
    rover._run(0, 1)
    GPIO.cleanup()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)


class Direction:

    def __init__(self, M1=None, M4=None, M2=None, M3=None,
                 config=2, speed=0, direction=0):
        self.direction = direction
        self.speed = speed
        self.mconf = config
        self.rotate = 0
        #type motor
        self.m1 = M1
        self.m2 = M2
        self.m3 = M3
        self.m4 = M4
        return


    def apply(self, s1, s2, s3, s4):
        if self.mconf == 0 or self.mconf == 2:
            self.m1.run(s1)
            self.m4.run(s4)
        if self.mconf == 1 or self.mconf == 2:
            self.m2.run(s2)
            self.m3.run(s3)
        return

    #use clockwise +-1, exclude 0
    def _rotate(self, speed, clock):
        self.apply(speed * clock, speed *-clock,
                   speed * clock, speed *-clock)
        return

    #direction +-1, exclude 0
    def _run(self, speed, direction):
        self.apply(speed * direction, speed * direction,
                   speed * direction, speed * direction)
        return

    def clean(self):
        self.apply(0, 0, 0, 0)
        return

    def stop(self):
        self.clean()
        return


if __name__ == '__main__':
    print("Demo: Motor test")

    if not Path("/dev/input/event0").is_file():
        print('No Bluetooth Controler for test')
        sys.exit(0)

    rover=Direction(M1=apimotor.Motor(0), M4=apimotor.Motor(1), config=0)
    gamepad = InputDevice('/dev/input/event0')        
    aBtn = 315
    bBtn = 311
    xBtn = 307
    yBtn = 308
    start = 305
    select = 314
    Trig = 313
    speed=1

    for event in gamepad.read_loop():
        #filters by event type
        if event.type == ecodes.EV_KEY:
            #print(event)
            if event.value == 1:
                if event.code == xBtn:
                    print("X")
                    rover._run(speed, 1)
                elif event.code == yBtn:
                    print("Y")
                    rover._rotate(speed, -1)
                elif event.code == bBtn:
                    print("B")
                    rover._run(speed, -1)
                elif event.code == aBtn:
                    print("A")
                    rover._rotate(speed, 1)

                elif event.code == start:
                    print("Start")
                    speed = speed + 5
                    print("Speed: ", speed)
                elif event.code == select:
                    print("Select")
                    speed = speed - 5
                    print("Speed: ", speed)
                elif event.code == Trig:
                    print("Bumper")
                    rover._run(0, 1)
    GPIO.cleanup()
