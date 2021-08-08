#!/usr/bin/env python

import unicornhathd
import sys
import time
import random
import colorsys
import itertools
import PIL

unicornhathd.rotation(270)


from PIL import Image
with Image.open(sys.argv[1]) as im:
    src = im.load()
    xsize, ysize = im.size

    if xsize != ysize:
        print("Not a square image, cropping")
        if xsize > ysize:
            maxsize = ysize
        else:
            maxsize = xsize
        box = (0, 0, maxsize, maxsize)
        src = im.crop(box)
        print("cropping complete")
    else:
        maxsize = xsize

    if maxsize > 16:
        print("image too large, resizing")
        im.thumbnail([16, 16])
        src = im.load()


unicornhathd.brightness(0.5)
unique_pixels = []
for x in range(16):
    for y in range(16):
        unique_pixels.append([x, y])
random.shuffle(unique_pixels)        
for x1, y1 in unique_pixels:
    srcPx = src[x1, y1]
    red = srcPx[0]
    green = srcPx[1]
    blue = srcPx[2]
    unicornhathd.set_pixel(x1, y1, red, green, blue)
    unicornhathd.show()                            
    time.sleep(0.01)

try:
    while True:
        time.sleep(1)

except KeyboardInterrupt:
    unicornhathd.off()