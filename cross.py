#!/usr/bin/env python

import unicornhathd as unicorn
from random import randint
import math
import time
import itertools
unicorn.rotation(180)
unicorn.brightness(1.0)
width,height=unicorn.get_shape()

start_range = [245, 230, 255]
end_range = [8, 0, 18]


colour_range = []
steps = 8
step_red = round((start_range[0]-end_range[0])/steps)
step_green = round((start_range[1]-end_range[1])/steps)
step_blue = round((start_range[2]-end_range[2])/steps)
for x in range(0, steps):
    actual_red = start_range[0] - (step_red * x)
    actual_green = start_range[1] - (step_green * x)
    actual_blue = start_range[2] - (step_blue * x)
    colour_range.append([actual_red, actual_green, actual_blue])


for step in range(8):
    lx = 8 + step
    ly = 8 + step
    colour = step
    rx = 8 - step
    ry = 8 - step
    unicorn.set_pixel(rx, ry, colour_range[colour][0], colour_range[colour][1], colour_range[colour][2])
    unicorn.set_pixel(lx, ly, colour_range[colour][0], colour_range[colour][1], colour_range[colour][2])
    unicorn.set_pixel(rx, ly, colour_range[colour][0], colour_range[colour][1], colour_range[colour][2])
    unicorn.set_pixel(lx, ry, colour_range[colour][0], colour_range[colour][1], colour_range[colour][2])
    unicorn.show()                            

try:
    while True:
        time.sleep(1)

except KeyboardInterrupt:
    unicorn.off()