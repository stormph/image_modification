import numpy as np
class Floater:
    def __init__(self,location,rotation):
        self.location = location
        self.rotation = rotation

    def move(self, length):
        self.location = np.add(self.location, (np.cos(self.rotation)*length, np.sin(self.rotation)*length))
    def rotate(self, angle):
        self.rotation = np.mod(self.rotation + angle, 2* np.pi)

    def __str__(self):
        return str(self.location)
