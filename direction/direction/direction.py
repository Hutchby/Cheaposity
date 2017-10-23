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

def signal_handler(signal, frame):
    print('You pressed Ctrl+C!')
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
    '''
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
    # '''


if __name__ == '__main__':
    print("test")
    rover=Direction(M1=Motor(21, 20, 16), M4=Motor(24, 12, 25), config=0)
    
    '''
    print("rover._run(10,1)")
    rover._run(10,1)
    time.sleep(5)
    print("rover._run(10,-1)")
    rover._run(10,-1)
    time.sleep(5)
    print("rover._rotate(10,1)")
    rover._rotate(10,1)
    time.sleep(5)
    rover._run(0, 1)
    #   '''

    # '''
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
                    speed+=10
                elif event.code == select:
                    print("Select")
                    speed-=10
                elif event.code == Trig:
                    print("Bumper")
                    rover._run(0, 1)
#'''
    GPIO.cleanup()
