# Simple demo of of the PCA9685 PWM servo/LED controller library.
# This will move channel 0 from min to max position repeatedly.
# Author: Tony DiCola
# License: Public Domain

# Import the PCA9685 module.
from pwm import servo
from gpio import sonar
import time

servo = servo.servoMG996R()
sonar = sonar.Sonar()

print('Moving servo on channel 0, press Ctrl-C to quit...')
while True:
    # Move servo on channel O between extremes.
    servo.rotate(1)
    time.sleep(0.5)
    print(sonar.measure_average())

    servo.rotate(3/4)
    time.sleep(0.5)
    print(sonar.measure_average())
    servo.rotate(1/2)
    time.sleep(0.5)
    print(sonar.measure_average())
    servo.rotate(1/4)
    time.sleep(0.5)
    print(sonar.measure_average())
    servo.rotate(0)
    time.sleep(0.5)
    print(sonar.measure_average())


