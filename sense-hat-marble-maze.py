#!/usr/bin/env python
'''
https://www.raspberrypi.org/learning/sense-hat-marble-maze/worksheet/
URL 
'''
from sense_hat import SenseHat
from time import sleep
from random import randint

sense = SenseHat()
sense.clear()

r = (255,0,0)
g = (0,255,0)
b = (0,0,0)
w = (255,255,255)

sense.low_light = True
x = 1
y = 1

mazeTab = [[[r,r,r,r,r,r,r,r],
	[r,b,b,b,b,b,b,r],
	[r,r,r,b,r,r,b,r],
	[r,b,r,b,b,b,b,r],
	[r,b,b,b,b,r,b,r],
	[r,b,r,r,b,r,r,r],
	[r,b,b,r,g,b,b,r],
	[r,r,r,r,r,r,r,r]], #fin 0
        [[r,r,r,r,r,r,r,r],
	[r,b,b,b,b,b,b,r],
	[r,r,r,r,r,r,b,r],
	[r,b,b,b,b,r,b,r],
	[r,b,b,b,b,b,b,r],
	[r,b,r,b,r,r,r,r],
	[r,b,r,b,b,b,g,r],
	[r,r,r,r,r,r,r,r]], #fin 1
	[[r,r,r,r,r,r,r,r],
	[r,b,b,b,b,b,b,r],
	[r,r,r,b,r,r,b,r],
	[r,g,r,b,r,r,b,r],
	[r,b,r,b,b,b,b,r],
	[r,b,r,r,b,r,r,r],
	[r,b,b,b,b,b,b,r],
	[r,r,r,r,r,r,r,r]],  #fin 2
        [[r,r,r,r,r,r,r,r],
	[r,b,r,b,b,b,b,r],
	[r,b,r,b,r,b,b,r],
	[r,b,r,b,r,b,r,r],
	[r,b,b,b,r,b,b,r],
	[r,r,r,r,r,r,b,r],
	[r,g,b,b,b,b,b,r],
	[r,r,r,r,r,r,r,r]],   #fin 3
	[[r,r,r,r,r,r,r,r],
	[r,b,r,g,b,r,b,r],
	[r,b,r,r,b,b,b,r],
	[r,b,r,b,r,r,b,r],
	[r,b,r,b,b,b,b,r],
	[r,b,r,b,r,r,b,r],
	[r,b,b,b,r,b,b,r],
	[r,r,r,r,r,r,r,r]],   #fin 4
	[[r,r,r,r,r,r,r,r],
	[r,b,b,b,b,b,b,r],
	[r,r,r,r,r,b,b,r],
	[r,g,r,b,r,b,r,r],
	[r,b,r,b,b,b,b,r],
	[r,b,r,r,b,r,r,r],
	[r,b,b,b,b,b,b,r],
	[r,r,r,r,r,r,r,r]],  #fin 5
	[[r,r,r,r,r,r,r,r],
	[r,b,b,b,r,b,g,r],
	[r,r,r,b,r,b,b,r],
	[r,b,b,b,r,b,r,r],
	[r,b,r,b,r,b,b,r],
	[r,b,r,r,r,r,b,r],
	[r,b,b,b,b,b,b,r],
	[r,r,r,r,r,r,r,r]],  #fin 6
	[[r,r,r,r,r,r,r,r],
	[r,b,b,b,b,b,b,r],
	[r,r,r,b,r,r,r,r],
	[r,b,b,b,b,b,b,r],
	[r,b,r,b,b,b,b,r],
	[r,b,r,r,r,r,b,r],
	[r,b,b,r,g,b,b,r],
	[r,r,r,r,r,r,r,r]],   #fin 7
	[[r,r,r,r,r,r,r,r],
	[r,b,b,b,b,b,b,r],
	[r,b,r,r,r,r,b,r],
	[r,b,r,b,b,r,b,r],
	[r,b,r,b,g,r,b,r],
	[r,b,r,b,r,r,b,r],
	[r,b,b,b,b,b,b,r],
	[r,r,r,r,r,r,r,r]]]   # fin 8

def move_marble(pitch,roll,x,y):
	new_x = x
	new_y = y
	if 1 < pitch < 179 and x != 0:
		new_x -= 1
	elif 359 > pitch > 179 and x != 7 :
		new_x += 1
	if 1 < roll < 179 and y != 7:
		new_y += 1
	elif 359 > roll > 179 and y != 0 :
		new_y -= 1
	x,y = check_wall(x,y,new_x,new_y)
	return x,y

def check_wall(x,y,new_x,new_y):
	if maze[new_y][new_x] != r:
		return new_x, new_y
	elif maze[new_y][x] != r:
		return x, new_y
	elif maze[y][new_x] != r:
		return new_x, y
	return x,y

game_over = False

def check_win(x,y):
	global game_over
	if maze[y][x] == g:
		game_over = True
                sense.set_rotation(180)
		sense.show_message('You Win')

maze=mazeTab[randint(0,8)]
while not game_over:
	pitch = sense.get_orientation()['pitch']
	roll = sense.get_orientation()['roll']
	x,y = move_marble(pitch,roll,x,y)
	check_win(x,y)
        if not game_over:
	    maze[y][x] = w
	    sense.set_pixels(sum(maze,[]))
	    sleep(0.05)
	    maze[y][x] = b
