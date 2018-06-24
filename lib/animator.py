import unicornhathd as unicorn
import time

class Projector:
    def __init__(self, movie):
        self.movie = movie
        unicorn.brightness(0.2)
        unicorn.rotation = movie.rotation()

    def animate(self):
        while finished == False:
            pixels = self.movie.step()
            for i in pixels:
                unicorn.set_pixel(i["x"], i["y"], i["r"], i["g"], i["b"])
            unicorn.show()
            time.sleep(self.movie.refresh_rate())
            finished = movie.finished()
        unicorn.off()

    def off(self):
        unicorn.off()
