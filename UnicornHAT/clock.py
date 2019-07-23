#!/usr/bin/env python

import colorsys
import time
from sys import exit


try:
    from PIL import Image, ImageDraw, ImageFont
except ImportError:
    exit('This script requires the pillow module\nInstall with: sudo pip install pillow')
FONT = ('/usr/share/fonts/truetype/freefont/FreeSansBold.ttf', 12)

unicornhathd.rotation(270)
unicornhathd.brightness(0.8)

width, height = unicornhathd.get_shape()

text_x = width
text_y = height

font_file, font_size = FONT

font = ImageFont.truetype(font_file, font_size)

text_width, text_height = width, 0


except KeyboardInterrupt:
    unicornhathd.off()
