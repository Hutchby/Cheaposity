from i2c import gyrodriver
import math
import time

def norme(vect):
    x2 = math.pow(vect['x'], 2)
    y2 = math.pow(vect['y'], 2)
    z2 = math.pow(vect['z'], 2)
    return math.sqrt(x2 + y2 + z2)

def azimuth(vect):
    return (180 / math.pi) * math.atan2(vect['y'], vect['x'])

def altitude(vect):
    h = math.hypot(y, x)
    return 180 / math.pi * math.atan2(z, h)

def pitch(vect):
    return math.asin(-a['y'] / norme(a))

def roll(vect):
    return math.asin(a['x'] / norme(a))
