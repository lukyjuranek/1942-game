import pyxel
import main
from math import sin, cos, radians

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
        self.x += self.speed * cos(radians(self.angle)) * main.DELTA_TIME
        self.y += self.speed * sin(radians(self.angle)) * main.DELTA_TIME


    def draw(self):
        '''Draws the shot'''
        pyxel.blt(self.x, self.y, 0, 0, 16, self.width, self.height, 0)