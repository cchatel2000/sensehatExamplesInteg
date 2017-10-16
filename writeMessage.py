#!/usr/bin/env python
from sense_hat import SenseHat
sense = SenseHat()
sense.low_light = True
sense.set_rotation(180)
#while True:
sense.show_message("Spaaaaaaace!!",scroll_speed=0.1,text_colour=[255,255,0],back_colour=[0,0,255])
sense.clear()
