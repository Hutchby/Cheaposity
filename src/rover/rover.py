from pwm import apimotor, servo
from gpio import sonar
from i2c import gyrodriver, lcddriver
import time

class Rover:

    def __init__(self):
        print("init rover")
        self.sonar = sonar.Sonar()
        self.servo = servo.servoMG996R()
        self.lcd =  lcddriver.lcd()
        self.gyroaccel = gyrodriver.MPU9250()
        self.magneto = gyrodriver.AK8963()
        self.left_motor = apimotor.Motor(channel=15, coeff=0.5)
        self.right_motor = apimotor.Motor(channel=7, coeff=0.8)

    def do_scan(self):
        print("do_scan()")
        tab = [0, 0, 0, 0, 0]
        for i in range(5):
            self.servo.rotate(i / 4)
            time.sleep(0.5)
            tab[i] = self.sonar.measure_average()
        return tab

    def turn(self, angle):
        return 0
    def forward(self, dist):
        return 0
    def backward(self, dist):
        return 0

    def run(self):
        print("rover running...")
        while True:
            print(self.do_scan())
            print("tick")
            self.left_motor.pwm(100)
            self.right_motor.pwm(100)


