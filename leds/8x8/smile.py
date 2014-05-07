#!/usr/bin/python
#
# Simple smiley for Adafruit 8x8 LED Backpack
#
# (C) 2014 PiClass - BSD License
#
from Adafruit_8x8 import EightByEight
grid = EightByEight(address=0x70)
 
# Clear the grid
grid.clear()
 
# Switch on leds line by line
grid.setPixel(0, 2)
grid.setPixel(0, 3)
grid.setPixel(0, 4)
grid.setPixel(0, 5)

grid.setPixel(1, 1)
grid.setPixel(1, 6)

grid.setPixel(2, 0)
grid.setPixel(2, 2)
grid.setPixel(2, 4)
grid.setPixel(2, 7)

grid.setPixel(3, 0)
grid.setPixel(3, 5)
grid.setPixel(3, 7)

grid.setPixel(4, 0)
grid.setPixel(4, 5)
grid.setPixel(4, 7)

grid.setPixel(5, 0)
grid.setPixel(5, 2)
grid.setPixel(5, 4)
grid.setPixel(5, 7)

grid.setPixel(6, 1)
grid.setPixel(6, 6)

grid.setPixel(7, 2)
grid.setPixel(7, 3)
grid.setPixel(7, 4)
grid.setPixel(7, 5)
