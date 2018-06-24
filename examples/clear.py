import unicornhathd as unicorn
import time, colorsys
import numpy

unicorn.brightness(1)

for y in range(16):
  for x in range(16):
    h = 0.0
    s = 1.0
    v = 0
    rgb = colorsys.hsv_to_rgb(h, s, v)
    r = int(rgb[0]*255.0)
    g = int(rgb[1]*255.0)
    b = int(rgb[2]*255.0)
    unicorn.set_pixel(x, y, r, g, b)
unicorn.show()
