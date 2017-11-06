from i2c import gyrodriver
from time import *

if __name__ == "__main__":
    mpu = gyrodriver.MPU9250()
    ak  = gyrodriver.AK8963()

    try:
        while True:
            accel   = mpu.readAccel()
            gyro    = mpu.readGyro()
            magneto = ak.readMagnet()
            print("accel {}".format(accel))
            print("gyro {}".format(gyro))
            print("magnet {}".format(magneto))

            sleep(0.5)
    except KeyboardInterrupt:
        sys.exit()
