#!/usr/bin/python
#
# Tiny boat for Adafruit 8x8 LED Backpack
#
# (C) 2014 PiClass - BSD License
#
from Adafruit_8x8 import EightByEight
grid = EightByEight(address=0x70)
 
# Clear the grid
grid.clear()

# Switch on leds
grid.setPixel(0, 5)
grid.setPixel(1, 5)
grid.setPixel(1, 6)
grid.setPixel(2, 5)
grid.setPixel(2, 6)
grid.setPixel(2, 7)
grid.setPixel(3, 5)
grid.setPixel(3, 6)
grid.setPixel(3, 7)
grid.setPixel(4, 5)
grid.setPixel(4, 6)
grid.setPixel(4, 7)
grid.setPixel(5, 5)
grid.setPixel(5, 6)
grid.setPixel(5, 7)
grid.setPixel(6, 5)
grid.setPixel(6, 6)
grid.setPixel(7, 5)

grid.setPixel(3, 4)
grid.setPixel(3, 3)
grid.setPixel(3, 2)
grid.setPixel(3, 1)
grid.setPixel(3, 0)
grid.setPixel(4, 3)
grid.setPixel(4, 2)
grid.setPixel(4, 1)
grid.setPixel(5, 3)
grid.setPixel(5, 2)
grid.setPixel(6, 3)
