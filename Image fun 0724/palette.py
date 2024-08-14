import numpy as np
class Palette:
    def __init__(self,colors = [],distances = [], smallest_dist = 255):
        self.colors = colors
        self.distances = distances
        self.smallest_dist = smallest_dist

    def add_color(self, new_col, i, isLower):
        #what if i+1 extends beyond length¨
        if isLower == None:
            self.colors = self.colors + []


        new_dist_l = self.colors[i] - new_col 
        new_dist_u = new_col - self.colors[i+1]
        if i+1 >= len(self.colors) and isLower == False:
            self.colors = self.colors[:i-isLower] + [new_col]
            self.distances = self.distances[:i-isLower] + [new_dist_l]
        #what if i = 0
        elif i == 0 and isLower:
            self.colors = self.colors[:i] + [new_col] + self.colors[1:]
            self.distances = [new_dist_u] + self.distances[1:] 
        else:
            self.colors = self.colors[:i-isLower] + [new_col] + self.colors[i+2-isLower:]
            self.distances = self.distances[:i-isLower] +[new_dist_l,new_dist_u] + self.distances[i+2-isLower:] 
        
        for dist in self.distances:
            if self.smallest_dist < dist:
                self.smallest_dist = dist

    def __str__(self):
        return str(self.colors)
