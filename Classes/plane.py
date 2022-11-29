from math import sin, cos
from Classes.shot import Shot
from random import randint
import pyxel

class Plane:
    def __init__(self, x: float, y: float, health: int, speed: int):
        self.x = x
        self.y = y
        self.health = health
        self.speed = speed

    @property
    def angle(self):
        pass

    def update(self):
        # Randomly changes the angle of the plane
        if randint(0, 20) == 1:
            self.angle += 45 * randint(-1, 1)

    def draw(self):
        pyxel.blt(self.x, self.y, 0, 0, 0, 16, 16)

    def shoot(self):
        # Creates an instance of the shot class
        self.shots.append(Shot(self.x, self.y, 100, 3, self.angle, self.pyxel))