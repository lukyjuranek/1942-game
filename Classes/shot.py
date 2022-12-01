import pyxel
from math import sin, cos

class Shot:
    def __init__(self, x: float, y: float, speed: int, angle: float):
        self.x = x
        self.y = y
        self.speed = speed
        self.angle = angle
        self.width = 4
        self.height = 4

    def update(self):
        '''Updates the shot position'''
        self.x += self.speed * cos(self.angle)
        self.y += self.speed * sin(self.angle)

    def draw(self):
        '''Draws the shot'''
        pyxel.blt(self.x, self.y, 0, 0, 16, self.width, self.height, 0)