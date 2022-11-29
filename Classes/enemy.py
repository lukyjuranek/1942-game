from Classes.shot import Shot
from random import randint
from math import sin, cos
import pyxel

class Enemy:
    def __init__(self, x: float, y: float, angle: int, health: int, speed: int):
        self.x = x
        self.y = y
        self.angle = angle
        self.health = health
        self.speed = speed
        self.width = 16
        self.height = 16
        # self.shots = []

    @property
    def angle(self):
        return self.__angle

    @angle.setter
    def angle(self, value):
        if type(value) != int:
            raise TypeError("Angle must be an integer")
        if value < 0:
            value = 360 * value
        self.__angle = value

    def update(self):
        # Randomly changes the angle of the plane
        if randint(0, 20) == 1:
            self.angle += 45 * randint(-1, 1)

        
        self.x += self.speed * cos(self.angle)
        self.y += self.speed * sin(self.angle)

    def draw(self):
        pyxel.blt(self.x, self.y, 0, 0, 0, self.width, self.height, 0)

    # def shoot(self):
    #     # Creates an instance of the shot class
    #     self.shots.append(Shot(self.x, self.y, 100, 3, self.angle, self.pyxel))