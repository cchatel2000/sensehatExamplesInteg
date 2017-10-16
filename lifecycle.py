#!/usr/bin/python
print("life_cycles.py ver 1.1")

"""
Original program Conway.py modified by
Claude Pageau    pageauc@gmail.com
01-Dec-2016
Added shake to restart new Life Cycle

"""

from itertools import product
from random import choice, randint
from time import sleep
from sense_hat import SenseHat
import sys
import enterMod

sense = SenseHat()
accel_thresh = 0.4
sense.low_light = True
sense.set_rotation(180)

#-----------------------------------------------------------------------------------------------  
class GameOfLife(object):
    def __init__(self, width, height, gl_color):
        self.size = (width, height)
        self.gl_color = gl_color
        self.random_world()

    def __str__(self):
        width, height = self.size
        return '\n'.join(
            ' '.join(
                self.draw_cell(x, y) for x in range(width)
            )
            for y in range(height)
        )

    def __iter__(self):
        return self

    def __next__(self):
        self.evolve_world()
        return self

    next = __next__

    def evolve_cell(self, cell):
        alive = cell in self.live_cells
        neighbours = self.count_neighbours(cell)
        return neighbours == 3 or (alive and neighbours == 2)

    def count_neighbours(self, cell):
        x, y = cell
        deltas = set(product([-1, 0, 1], repeat=2)) - set([(0, 0)])
        neighbours = ((x + dx, y + dy) for (dx, dy) in deltas)
        return sum(neighbour in self.live_cells for neighbour in neighbours)

    def evolve_world(self):
        width, height = self.size
        world = product(range(width), range(height))
        self.live_cells = {cell for cell in world if self.evolve_cell(cell)}

    def random_world(self):
        width, height = self.size
        world = product(range(width), range(height))
        self.live_cells = {cell for cell in world if choice([0, 1])}

    def draw_cell(self, x, y):
        cell = (x, y)
        return 'O' if cell in self.live_cells else ' '

    def get_cell_color(self, x, y):
        cell = (x, y)
        #red = (255, 0, 0)
        black = (0, 0, 0)
        return self.gl_color if cell in self.live_cells else black

    def update(self):
        width, height = self.size
        for x in range(width):
            for y in range(height):
                color = self.get_cell_color(x, y)
                sense.set_pixel(x, y, color)
                
#-----------------------------------------------------------------------------------------------                  
def detect_shake(thresh):
    restart = False
    x, y, z = sense.get_accelerometer_raw().values()
    x1 = abs(x)
    y1 = abs(y)
    z1 = abs(z)
    sleep(0.1)
    x, y, z = sense.get_accelerometer_raw().values()
    dx = abs(abs(x1) - abs(x))
    dy = abs(abs(y1) - abs(y))
    dz = abs(abs(z1) - abs(z))
    if dx > thresh or dy > thresh or dz > thresh:
        restart = True
    return  restart    
                
#-----------------------------------------------------------------------------------------------               
def main():
    print("Shake Pi to Restart Life Cycle")
    print("    or ctrl-c to Quit")
    #sense.show_message("Shake Restarts")
    life_cycles = 1
    while (True):
        gl_color = (randint (1,255), randint (1,255), randint(1,255))
        msg = str(life_cycles)
        sense.show_message(msg)
        game = GameOfLife(8, 8, gl_color)
        for i in game:
            sleep(0.5)
            game.update()
            if detect_shake(accel_thresh):
                life_cycles += 1
                break      
	    c=enterMod.getKey()
	    if c==1:
	        sense.clear(0,0,0)
	        sys.exit()

if __name__ == '__main__':
    try:
        main()
    except Exception as inst:
        print(type(inst))
        print (inst.args)
        print(inst)
        print("Unexpected error:", sys.exc_info()[0])

        print("Thanks for the Life Cycles")
        print("Bye")
        sense.show_message("Thanks for the Life Cycles .. Bye")
        sense.clear()
