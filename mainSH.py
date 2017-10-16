#!/usr/bin/python
import sys
import os
import time
import subprocess

from sense_hat import SenseHat
from evdev import InputDevice, list_devices, ecodes

BLACK = [0, 0, 0]
WHITE = [255, 255, 255]
BLEU  = [0, 0, 255]
ROUGE = [255, 0, 0]
VERT  = [0, 255, 0]
FGC = WHITE
BGC = BLACK

print("Press Ctrl-C to quit")
time.sleep(1)
x=0; y=0;
enter = 0

sense = SenseHat()
sense.clear()  # Blank the LED matrix
sense.low_light = True

found = False;
devices = [InputDevice(fn) for fn in list_devices()]
for dev in devices:
    if dev.name == 'Raspberry Pi Sense HAT Joystick':
        found = True;
        break

if not(found):
    print('Raspberry Pi Sense HAT Joystick not found. Aborting ...')
    sys.exit()

# 0, 0 = Top left
# 7, 7 = Bottom right
UP_PIXELS = [[3, 0], [4, 0]]
DOWN_PIXELS = [[3, 7], [4, 7]]
LEFT_PIXELS = [[0, 3], [0, 4]]
RIGHT_PIXELS = [[7, 3], [7, 4]]
CENTRE_PIXELS = [[3, 3], [4, 3], [3, 4], [4, 4]]

def set_pixels(pixels, col):
    for p in pixels:
        sense.set_pixel(p[0], p[1], col[0], col[1], col[2])

def handle_code(code):
    global x,y,enter
    global BGC, WHITE, BLACK, FGC
    sense.set_pixel( x, y, BGC[0], BGC[1], BGC[2])
    if code == ecodes.KEY_DOWN:
        #deplace la led vers le bas
        #set_pixels(DOWN_PIXELS, colour)
        if (y < 7):
           y+=1
    elif code == ecodes.KEY_UP:
        #deplace la led vers le haut
        #set_pixels(UP_PIXELS, colour)
        if (y > 0):
           y-=1
    elif code == ecodes.KEY_LEFT:
        #deplace la led vers la gauche
        #set_pixels(LEFT_PIXELS, colour)
        if (x > 0):
            x-=1
    elif code == ecodes.KEY_RIGHT:
        #deplace la led vers la droite
        #set_pixels(RIGHT_PIXELS, colour)
        if (x < 7):
           x+=1
    elif code == ecodes.KEY_ENTER:
        #selectionne l'application qui correspond a l'emplacement courant
        #set_pixels(CENTRE_PIXELS, colour)
        #print "Touche enter" 
        if (enter == 0):
           subprocess.call([sys.executable, 'white.py'])
           FGC=BLACK ; BGC=WHITE
           enter = 1
           if (x==0):
              if (y==0):
                 subprocess.call([sys.executable, 'sense-hat-marble-maze.py'])
              if (y==1):
                 subprocess.call([sys.executable, 'shutdown.py'])
              elif (y==2):
                 subprocess.call([sys.executable, 'dice.py'])
              elif (y==3):
                 subprocess.call([sys.executable, 'demo_pacman.py'])
              elif (y==4):
                 subprocess.call([sys.executable, 'demo_sense.py'])
              elif (y==5):
                 subprocess.call([sys.executable, 'dmdclock.py'])
              elif (y==6):
                 subprocess.call([sys.executable, 'cross_sense.py'])
              elif (y==7):
                 subprocess.call([sys.executable, 'game_of_life_sense.py'])
           if (x==1):
              if (y==0):
                 subprocess.call([sys.executable, 'black.py'])
              if (y==1):
                 subprocess.call([sys.executable, 'black.py'])
              elif (y==2):
                 subprocess.call([sys.executable, 'writeMessage.py'])
              elif (y==3):
                 subprocess.call([sys.executable, 'sense-hat-marble-maze.py'])
              elif (y==4):
                 subprocess.call([sys.executable, 'compass.py'])
              elif (y==5):
                 subprocess.call([sys.executable, 'binary_clock_uni.py'])
              elif (y==6):
                 subprocess.call([sys.executable, 'pression.py'])
              elif (y==7):
                 subprocess.call([sys.executable, 'lifecycle.py'])
           if (x==2) and (y==2):
              subprocess.call([sys.executable, 'rainbow.py'])
           if (x==3) and (y==3):
              subprocess.call([sys.executable, 'colour_cycle.py'])
           if (x==4) and (y==4):
              subprocess.call([sys.executable, 'sense-hat-pong.py'])
           if (x==5) and (y==5):
              subprocess.call([sys.executable, 'sense-hat-random-sparkles.py'])
           if (x==6) and (y==6):
              subprocess.call([sys.executable, 'sense-hat-reaction_game.py'])
           if (x==7) and (y==7):
              subprocess.call([sys.executable, 'text_scroll.py'])
        else:
	   subprocess.call([sys.executable, 'black.py'])
           FGC=WHITE ; BGC=BLACK
           enter = 0
           if (x==1) and (y==1):
	      subprocess.call([sys.executable, 'black.py'])
    sense.set_pixel( x, y, FGC[0], FGC[1], FGC[2])


# allume en FGC le top left
sense.set_pixel( x, y, FGC[0], FGC[1], FGC[2])

try:
    for event in dev.read_loop():
        if event.type == ecodes.EV_KEY:
            if event.value == 1:  # key down
                handle_code(event.code)
            #if event.value == 0:  # key up
                #handle_code(event.code, BLACK)
except KeyboardInterrupt:
    sys.exit()

