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

        self.x += self.speed * cos(self.angle)
        self.y += self.speed * sin(self.angle)

        if self.pyxel.btn(self.pyxel.KEY_LEFT):
            self.x -= 1

        if self.pyxel.btn(self.pyxel.KEY_RIGHT):
            self.x += 1

        if self.pyxel.btn(self.pyxel.KEY_UP):
            self.y -= 1
        
        if self.pyxel.btn(self.pyxel.KEY_DOWN):
            self.y += 1

        if self.pyxel.btn(self.pyxel.KEY_SPACE):
            self.shoot()

    def draw(self):
        pyxel.blt(self.x, self.y, 0, 0, 0, 16, 16)

    def shoot(self):
        # Creates an instance of the shot class
        self.shots.append(Shot(self.x, self.y, 100, 3, self.angle, self.pyxel))