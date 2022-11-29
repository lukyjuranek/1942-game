import pyxel
from math import sin, cos

class Shot:
    def __init__(self, x: float, y: float, health: int, speed: int, angle):
        self.x = x
        self.y = y
        self.health = health
        self.speed = speed
        self.angle = angle
        self.width = 4
        self.height = 4

    def update(self):
        self.x += self.speed * cos(self.angle)
        self.y += self.speed * sin(self.angle)

    def draw(self):
        pyxel.blt(self.x, self.y, 0, 0, 16, 4, 15+self.height, 0)