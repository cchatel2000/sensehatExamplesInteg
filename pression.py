#!/usr/bin/python

from sense_hat import SenseHat
import os
import time
import datetime
import locale
import sys
import enterMod
from pytz import timezone

sense = SenseHat()

sense.low_light = True
sense.set_rotation(180)
sense.clear()

inky=[]
for nbr in range(1, 15):
        inky.append(sense.load_image("/home/pi/sensehat-examples/sprites/inky"+str(nbr)+".png", redraw=False))
clyde=[]
for nbr in range(1, 15):
        clyde.append(sense.load_image("/home/pi/sensehat-examples/sprites/clyde"+str(nbr)+".png", redraw=False))

pinky=[]
for nbr in range(1, 15):
        pinky.append(sense.load_image("/home/pi/sensehat-examples/sprites/pinky"+str(nbr)+".png", redraw=False))

blinky=[]
for nbr in range(1, 15):
        blinky.append(sense.load_image("/home/pi/sensehat-examples/sprites/blinky"+str(nbr)+".png", redraw=False))

deadghost=[]
for nbr in range(1, 15):
        deadghost.append(sense.load_image("/home/pi/sensehat-examples/sprites/deadghost"+str(nbr)+".png", redraw=False))

pacman=[]
for nbr in range(1, 15):
	pacman.append(sense.load_image("/home/pi/sensehat-examples/sprites/pacman"+str(nbr)+".png", redraw=False))

pacmanb=[]
for nbr in range(1, 15):
	pacmanb.append(sense.load_image("/home/pi/sensehat-examples/sprites/pacmanb"+str(nbr)+".png", redraw=False))


def Move(sprites, direction):
        if direction:
                animation = sprites
        else:
                animation = reversed(sprites)
        for sprite in animation:
                sense.set_pixels(sprite)
                time.sleep(0.1) # delays for 100 miliseconds

# Let's set a non-US locale
locale.setlocale(locale.LC_TIME, "fr_FR.UTF8")
print("Setting time")
bashCommand = "sudo service ntp stop; sudo ntpdate 193.50.119.254; sudo service ntp start"
os.system(bashCommand)
now = datetime.datetime.now(timezone('Europe/Paris'))

print(now.strftime("Date : %d %B %Y Heure : %H:%M"))

while (True):
        now = datetime.datetime.now(timezone('Europe/Paris'))
	pressure = sense.get_pressure()
	temp = sense.get_temperature()
	humidity = sense.get_humidity() 
        print pressure, temp, humidity
        sense.show_message(now.strftime("Date : %d %B %Y "), text_colour=[0, 255, 255])
        sense.show_message(now.strftime("Heure : %H:%M"), text_colour=[255, 0, 0])
        sense.show_message("Temperature : "+"{0:.1f}".format(temp)+" C", text_colour=[255, 102, 0])
        sense.show_message("Pression : "+"{0:.0f}".format(pressure)+" mB", text_colour=[255, 0, 255])
        sense.show_message("Hygrometrie : "+"{0:.0f}".format(humidity)+"%", text_colour=[255, 255, 0])
        if enterMod.getKey()==1:
           sense.clear()
           sys.exit()
        break

