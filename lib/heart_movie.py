class HeartMovie:
    def __init__(self):
        self.refresh_rate = 0.005
        self.finished = False
        self.rotation = 90
        self.frame    = 0
        self.heart    = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                         0,0,0,1,1,0,0,0,0,0,0,1,1,0,0,0,
                         0,0,1,1,1,1,0,0,0,0,1,1,1,1,0,0,
                         0,1,1,1,1,1,1,0,0,1,1,1,1,1,1,0,
                         1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
                         1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
                         1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
                         1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
                         0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,
                         0,0,1,1,1,1,1,1,1,1,1,1,1,1,0,0,
                         0,0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,
                         0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0,
                         0,0,0,0,0,1,1,1,1,1,1,0,0,0,0,0,
                         0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,
                         0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,
                         0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

    def step(self):
        pixels = []
        for index, item in enumerate(self.heart):
            x = index % 16
            y = ((index - x) / 16) % 16

            if item == 0:
                r = 0.0
            else:
                r = 255.0 / ((self.frame % 20) + 1)
            pixels.append({"x": x, "y": y, "r": r, "g": 0, "b": 0})

        self.frame = self.frame + 1
        return pixels

