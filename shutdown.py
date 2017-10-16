#!/usr/bin/python
import sys
import os
from sense_hat import SenseHat
sense = SenseHat()

sense.set_rotation(180)
sense.show_message("Shutdown!!",scroll_speed=0.1,text_colour=[255,255,0],back_colour=[0,0,255])
sense.clear()
os.system('sudo halt');

