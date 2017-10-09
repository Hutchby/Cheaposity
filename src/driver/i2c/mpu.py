import gyrodriver
from time import *

mpu = gyrodriver.MPU9250()

try:
    while True:
        accel = mpu.readAccel()
        print("ax = ", (accel['x']))
        print("ay = ", (accel['y']))
        print("az = ", (accel['z']))

        sleep(0.5)
except KeyboardInterrupt:
    sys.exit()
