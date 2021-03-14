#!/usr/bin/env python

import unicornhathd
import sys
import time
import colorsys
import itertools
import PIL

unicornhathd.rotation(270)
unicornhathd.brightness(0.8)

def scroll_in(src, steps, wait):
    for fade in range(steps):
        for x in range(16):
            for y in range(16):
                srcPx = src[x, y]
                red = srcPx[0] / steps * fade
                green = srcPx[1] / steps * fade
                blue = srcPx[2] / steps * fade
                unicornhathd.set_pixel(x, y, red, green, blue)
        unicornhathd.show() 
        time.sleep(wait)                           

def fade_out(src, steps, wait):
    for fade in range(steps):
        for x in range(16):
            for y in range(16):
                srcPx = src[x, y]
                red = srcPx[0] - (srcPx[0] / steps * fade)
                green = srcPx[1] - (srcPx[1] / steps * fade)
                blue = srcPx[2] - (srcPx[2] / steps * fade)
                unicornhathd.set_pixel(x, y, red, green, blue)
        unicornhathd.show() 
        time.sleep(wait)                           

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

scroll_in(src, 16, 0)
time.sleep(2)
scroll_out(src, 16, 0.04)
unicornhathd.off()



