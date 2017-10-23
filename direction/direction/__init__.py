import sys
from apimotor import *
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

sign = lambda x: math.copysign(1, x)

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
        if mconf == 0 or mconf == 2:
            self.m1.run(s1)
            self.m4.run(s4)
        if mconf == 1 or mconf == 2:
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

    # stop the rover, not just stop motor but try to stop the rover's speed
    def stop(self):
        self.clean()
        return

    #use clockwise +-180
    def rotate(self, speed, angle):
        self._rotate(speed, sign(angle))
        while(true):
            break #continue
        self.stop()
        return

    #direction +-1, exclude 0
    def run(self, speed, direction):
        self._run(speed, direction)
        while(true):
            break #continue
        self.stop()
        return



if __name__ == '__main__':
    print("test")
    rover=Direction(M1=Motor(21, 20, 16), M4=Motor(24, 12, 25), config=0)
    print("rover._run(10,1)")
    rover._run(10,1)
    time.sleep(5)
    print("rover._run(10,1)")
    rover._run(10,-1)
    print("rover._rotate(10,1)")
    rover._rotate(10,1)

    '''
    gamepad = InputDevice('/dev/input/event0')
    aBtn = 315
    bBtn = 311
    xBtn = 307
    yBtn = 308
    start = 305
    select = 314
    Trig = 313

    for event in gamepad.read_loop():
        #filters by event type
        speed=50
        if event.type == ecodes.EV_KEY:
            print(event)
            if event.value == 1:
                if event.code == xBtn:
                    print("X")
                    _run(speed, 1)
                elif event.code == yBtn:
                    print("Y")
                    _rotate(speed, -1)
                elif event.code == bBtn:
                    print("B")
                    _run(speed, -1)
                elif event.code == aBtn:
                    print("A")
                    _rotate(speed, -1)

                elif event.code == start:
                    print("Start")
                    speed+=10
                elif event.code == select:
                    print("Select")
                    speed-=10
                elif event.code == Trig:
                    print("Bumper")
                    self.clean()
'''
