#!/usr/bin/env python
import signal
import time
from sys import exit
from sense_hat import SenseHat

try:
    from PIL import Image
except ImportError:
    exit("This script requires the pillow module\nInstall with: sudo pip install pillow")

def readSprites(filename):
	img = Image.open(filename)
	sprites_list = []
	for o_x in range(int(img.size[0]/8)):
	    for o_y in range(int(img.size[1]/8)):
	        sprite=[]
	        for x in range(8):
        	    for y in range(8):
                	pixel = img.getpixel(((o_x*8)+y,(o_y*8)+x))
        	        r, g, b = int(pixel[0]),int(pixel[1]),int(pixel[2])
                	sprite.append([r,g,b])
	        sprites_list.append(sprite)
	return sprites_list

def animateSprite(sprite,delay=0.1):
	for index,spr in enumerate(sprite):
	        sense.clear()
        	sense.set_pixels(spr)
	        time.sleep(delay)
	sense.clear()

def animateBackSprite(sprite,delay=0.1):
	for index,spr in enumerate(sprite):
	        sense.clear()
		flipped = []
	        for i in range(8):
	            offset = i * 8
        	    flipped.extend(reversed(spr[offset:offset + 8]))
        	sense.set_pixels(flipped)
		#sense.flip_h(redraw=False)
	        time.sleep(delay)
	sense.clear()

def animateSpriteFB(sprite,delay,direction):
#	print(len(sprite), delay, direction)
	if (len(sprite)!=0):
		for index,spr in enumerate(sprite):
		        sense.clear()
			if direction=='b':
				flipped = []
		       	        for i in range(8):
                		    offset = i * 8
				    flipped.extend(reversed(spr[offset:offset + 8]))
		                sense.set_pixels(flipped)
			else:
	       			sense.set_pixels(spr)
			time.sleep(delay)
	else:
	        time.sleep(delay)
	sense.clear()

sense = SenseHat()
sense.low_light = True

sense.set_rotation(180)

none=[]
skulls = readSprites('./sprites/skulls.png')
orange = readSprites('./sprites/clyde-sheet.png')
red = readSprites('./sprites/blinky-sheet.png')
blue = readSprites('./sprites/inky-sheet.png')
blueghost = readSprites('./sprites/deadghost-sheet.png')
pink = readSprites('./sprites/pinky-sheet.png')
pacman = readSprites('./sprites/pacman-sheet.png')

animation_orderTest = [[pacman, 0.03, 'b'], [none,0.5,'f'], [blueghost, 0.03, 'b'], [none,0.8,'f'], [orange,0.1,'f'], [none,0.8,'f'] ,[pacman, 0.12, 'f']]
animation_order = [orange, blue, pink, red , pacman ]
animation2_order = [pacman, blueghost, blueghost, blueghost, blueghost ]

#animateSprite(orange)
#sense.clear()
#time.sleep(0.5)
#animateBackSprite(orange, 0.05)
#sense.clear()

sense.low_light = True
for i in range (len(animation_orderTest)):
	[animation,delay,direction] = animation_orderTest.pop()
	animateSpriteFB(animation,delay,direction)
	animation_order.insert(0, animation)


for i in range (len(animation_order)):
	animation = animation_order.pop()
	#animateSprite(animation)
	animation_order.insert(0, animation)

for i in range (len(animation2_order)):
	animation = animation2_order.pop()
	#animateBackSprite(animation)
	animation_order.insert(0, animation)
