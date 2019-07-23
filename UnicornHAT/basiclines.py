#!/usr/bin/env python

import time
import unicornhathd

print("""Unicorn HAT HD: Lines

Demonstrates how to draw lines on Unicorn HAT HD.

Press Ctrl+C to exit!
""")

unicornhathd.brightness(0.6)
for x in range(1, 16):
    unicornhathd.set_pixel(x, 16-x, 255, 0, 0)
    unicornhathd.set_pixel(x, x, 255, 0, 0)
    unicornhathd.show()
    time.sleep(0.5 / 16)
