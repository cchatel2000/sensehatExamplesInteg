#!/usr/bin/python
"""
Original code modified by Claude Pageau pageauc@gmail.com
This code was originally posted 
here http://www.suppertime.co.uk/blogmywiki/2015/12/raspberrypi-dice-project/
Not sure who the original author is.
I had a Raspberry pi sense-hat and decided to do some improvements.
This code is designed to run on a raspberry pi with a sense hat installed and
working per instructions here https://www.raspberrypi.org/documentation/hardware/sense-hat/

"""
# User Settings
debug = True
accel_thresh = 0.4
shake_timer = 3  # seconds to show die before cleaing display

print("Settings dice.py ver 1.1")
print("------------------------")
print("debug = %s" % debug)
print("accel_thresh = %0.3f (delta)" % accel_thresh)
print("shake_timer = %i sec (show die)" % shake_timer)
print("------------------------")
print("Loading .....")

from sense_hat import SenseHat
import time
import sys
import enterMod
from random import randint
sense = SenseHat() # initialize 
sense.low_light = True
sense.set_rotation(180)

# Setup dice display variables

b = [0, 0, 0]
g = [0, 255, 0]
r = [255, 0, 0]

one = [
b,b,b,b,b,b,b,b,
b,b,b,b,b,b,b,b,
b,b,b,b,b,b,b,b,
b,b,b,g,g,b,b,b,
b,b,b,g,g,b,b,b,
b,b,b,b,b,b,b,b,
b,b,b,b,b,b,b,b,
b,b,b,b,b,b,b,b,
]

two = [
b,b,b,b,b,b,b,b,
b,g,g,b,b,b,b,b,
b,g,g,b,b,b,b,b,
b,b,b,b,b,b,b,b,
b,b,b,b,b,b,b,b,
b,b,b,b,b,g,g,b,
b,b,b,b,b,g,g,b,
b,b,b,b,b,b,b,b,
]

three = [
g,g,b,b,b,b,b,b,
g,g,b,b,b,b,b,b,
b,b,b,b,b,b,b,b,
b,b,b,g,g,b,b,b,
b,b,b,g,g,b,b,b,
b,b,b,b,b,b,b,b,
b,b,b,b,b,b,g,g,
b,b,b,b,b,b,g,g,
]

four = [
b,b,b,b,b,b,b,b,
b,g,g,b,b,g,g,b,
b,g,g,b,b,g,g,b,
b,b,b,b,b,b,b,b,
b,b,b,b,b,b,b,b,
b,g,g,b,b,g,g,b,
b,g,g,b,b,g,g,b,
b,b,b,b,b,b,b,b,
]

five = [
g,g,b,b,b,b,g,g,
g,g,b,b,b,b,g,g,
b,b,b,b,b,b,b,b,
b,b,b,g,g,b,b,b,
b,b,b,g,g,b,b,b,
b,b,b,b,b,b,b,b,
g,g,b,b,b,b,g,g,
g,g,b,b,b,b,g,g,
]

six = [
r,r,b,b,b,b,r,r,
r,r,b,b,b,b,r,r,
b,b,b,b,b,b,b,b,
r,r,b,b,b,b,r,r,
r,r,b,b,b,b,r,r,
b,b,b,b,b,b,b,b,
r,r,b,b,b,b,r,r,
r,r,b,b,b,b,r,r,
]

def roll_dice():
    global one, two, three, four, five, six
    global b, g, r
    ran = randint(1,6)
    if ran == 1:
        sense.set_pixels(one)
    elif ran == 2:
        sense.set_pixels(two)
    elif ran == 3:
        sense.set_pixels(three)
    elif ran == 4:
        sense.set_pixels(four)
    elif ran == 5:
        sense.set_pixels(five)
    elif ran == 6:
        sense.set_pixels(six)      
        
try:
    sense.clear()
    sense.show_message("Shake...")
    print("Shake to Roll the Die")
    start_time = time.time()
    next_roll = True
    while True:
        x, y, z = sense.get_accelerometer_raw().values()
        x1 = abs(x)
        y1 = abs(y)
        z1 = abs(z)
        time.sleep(0.1)
        x, y, z = sense.get_accelerometer_raw().values()
        dx = abs(abs(x1) - abs(x))
        dy = abs(abs(y1) - abs(y))
        dz = abs(abs(z1) - abs(z))
        if dx > accel_thresh or dy > accel_thresh or dz > accel_thresh:
            if next_roll:
                roll_dice()
                next_roll = False
                start_time = time.time()
                if debug:
                    print("accel base  x1=%0.3f y1=%0.3f z1=%0.3f" %( x1, y1, z1 ))
                    print("accel delta dx=%0.3f dy=%0.3f dz=%0.3f" %( dx, dy, dz ))
                print("Shake ...")
        if time.time() - start_time > shake_timer:
            next_roll = True
            sense.clear()           
        c=enterMod.getKey()
        if c==1:
            sense.clear()
            sys.exit()
except Exception as inst:
   print(type(inst))
   print (inst.args)
   print(inst)
   print("Unexpected error:", sys.exc_info()[0])
   print("Bye")
   sense.clear()
