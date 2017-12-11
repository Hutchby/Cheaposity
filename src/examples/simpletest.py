# Simple demo of of the PCA9685 PWM servo/LED controller library.
# This will move channel 0 from min to max position repeatedly.
# Author: Tony DiCola
# License: Public Domain

# Import the PCA9685 module.
from pwm import servo

servo = servo.servoMG996R()

print('Moving servo on channel 0, press Ctrl-C to quit...')
while True:
    # Move servo on channel O between extremes.
    servo.rotate(1)
    servo.rotate(3/4)
    servo.rotate(1/2)
    servo.rotate(1/4)
    servo.rotate(0)
