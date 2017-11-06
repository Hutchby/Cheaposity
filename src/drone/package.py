from i2c import gyrodriver
import json
import time
import http

def get_MPU(mpu):
    return {'accel': mpu.readAccel(), 'gyro': mpu.readGyro(), 'magneto': {"x": 0, "y":0, "z":0}}

def get_GPS():
    return 0
def get_MULT():
    return 0

def craft_package():
    mpu = gyrodriver.MPU9250()
    package = {'mpu': get_MPU(mpu), 'gps': {'lat': 0, 'lon': 0}, 'bat': 0}
    return package

