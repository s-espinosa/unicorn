import unicornhathd as unicorn
import time, colorsys
import numpy

class Heart:

    def setup(self):
        """Set unicorn values"""

        unicorn.brightness(1)
        unicorn.rotation(90)

        self.heart = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                     [0,0,0,1,1,0,0,0,0,0,0,1,1,0,0,0],
                     [0,0,1,1,1,1,0,0,0,0,1,1,1,1,0,0],
                     [0,1,1,1,1,1,1,0,0,1,1,1,1,1,1,0],
                     [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                     [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                     [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                     [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                     [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
                     [0,0,1,1,1,1,1,1,1,1,1,1,1,1,0,0],
                     [0,0,0,1,1,1,1,1,1,1,1,1,1,0,0,0],
                     [0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0],
                     [0,0,0,0,0,1,1,1,1,1,1,0,0,0,0,0],
                     [0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]

        self.heart = numpy.array(self.heart)

    def animate(self):
        while True:
            for i in 2*(range(1,6)[::-1]+range(1,5)):
                for y in range(16):
                    for x in range(16):
                        h = 0.0
                        s = 1.0
                        v = self.heart[x,y] / float(i)
                        rgb = colorsys.hsv_to_rgb(h, s, v)
                        r = int(rgb[0]*255.0)
                        g = int(rgb[1]*255.0)
                        b = int(rgb[2]*255.0)
                        unicorn.set_pixel(x, y, r, g, b)
                unicorn.show()
                time.sleep(0.005)
            time.sleep(0.8)

    def clear(self):
        """docstring for clear"""
        for y in range(16):
           for x in range(16):
                unicorn.set_pixel(x, y, 0, 0, 0)
        unicorn.show()
