#!/usr/bin/env python
from sense_hat import SenseHat
sense = SenseHat()
O = (0, 255, 0) # green
X = (0, 0, 0) # black
creeper_pixels = [
 X, X, X, X, X, X, X, X,
 X, X, X, X, X, X, X, X,
 X, X, X, X, X, X, X, X,
 X, X, X, X, X, X, X, X,
 X, X, X, X, X, X, X, X,
 X, X, X, X, X, X, X, X,
 X, X, X, X, X, X, X, X,
 X, X, X, X, X, X, X, X
]
sense.set_pixels(creeper_pixels)
