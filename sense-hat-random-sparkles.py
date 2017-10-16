#!/usr/bin/env python
'''
URL https://www.raspberrypi.org/learning/sense-hat-random-sparkles/worksheet/
'''
from sense_hat import SenseHat
import sys
import enterMod
from random import randint
from time import sleep

sense = SenseHat()

sense.low_light = True
sense.clear (0,0,0)
while (True):
    x = randint(0, 7)
    y = randint(0, 7)
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    sense.set_pixel(x, y, r, g, b)
    sleep(0.1)
    c=enterMod.getKey()
    if c == 1:
       sense.clear (0,0,0)
       sys.exit()

