#!/usr/bin/env python3

import unicornhathd
import sys
import time
import colorsys
import itertools
import PIL

unicornhathd.rotation(90)



unicornhathd.brightness(1.0)

try:
    while True:
        for iteration in range(5):
            filename = sys.argv[1] + "-00" + str(iteration) + ".png" 
            print(filename)
            from PIL import Image
            with Image.open(filename) as im:
                src = im.load()
                for x in range(16):
                    for y in range(16):
                        srcPx = src[x, y]
                        red = srcPx[0]
                        green = srcPx[1]
                        blue = srcPx[2]
                        unicornhathd.set_pixel(x, y, red, green, blue)
                unicornhathd.show()                            
                time.sleep(0.2)
        for iteration in range(4, 1, -1):
            filename = sys.argv[1] + "-00" + str(iteration) + ".png" 
            print(filename)
            from PIL import Image
            with Image.open(filename) as im:
                src = im.load()
                for x in range(16):
                    for y in range(16):
                        srcPx = src[x, y]
                        red = srcPx[0]
                        green = srcPx[1]
                        blue = srcPx[2]
                        unicornhathd.set_pixel(x, y, red, green, blue)
                unicornhathd.show()                            
                time.sleep(0.2)

except KeyboardInterrupt:
    unicornhathd.off()
