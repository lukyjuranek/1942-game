from Classes.shot import Shot
from random import randint
from math import sin, cos, pi
import pyxel

class Enemy:
    def __init__(self, x: float, y: float, angle: int, health: int, speed: int):
        self.x = x
        self.y = y
        self.angle = angle
        self.health = health
        self.speed = speed
        self.width = 10
        self.height = 9
        self.gainedScore = 100 # TODO: Change this varibale name
        self.shots = []

    @property
    def angle(self):
        return self.__angle

    @angle.setter
    def angle(self, value):
        self.__angle = value

    def update(self):
        # Randomly changes the angle of the plane
        # if randint(0, 20) == 1:
        #     self.angle += pi * randint(-1, 1)

        # Destroys the plane if it goes out of the screen by more than 30 pixels
        # TODO: Make this a constant and review the value
        if self.x < -30 or self.x > pyxel.width + 30 or self.y < -30 or self.y > pyxel.height + 30:
            self.health = 0

        self.x += self.speed * cos(self.angle)
        self.y += self.speed * sin(self.angle)
        if randint(0, 50) == 1:
            self.shoot()

    def draw(self):
        if self.angle == pi/2:
            pyxel.blt(self.x, self.y, 0, 3, 28, self.width, self.height, 0)
        elif self.angle == 3*pi/2:
            pass
        else:
            raise Exception("The angle of the enemy is not supported")
            

    def shoot(self):
        # Creates an instance of the shot class
        self.shots.append(Shot(self.x, self.y, 3, self.angle))