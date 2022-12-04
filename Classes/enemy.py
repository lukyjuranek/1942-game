from Classes.shot import Shot
import constants
from random import randint
from math import sin, cos, pi, radians
import pyxel


class Enemy:
    """Enemy class"""
    def __init__(self, x: float, y: float, angle: float):
        self.x = x
        self.y = y
        self.angle = angle
        # self.speed = 60
        # self.width = 10
        # self.height = 9
        self.health = 1
        self.gained_score = 100  # TODO: Change this variable name
        self.shots = []

    @property
    def angle(self):
        return self.__angle

    @angle.setter
    def angle(self, value):
        if type(value) != float and type(value) != int:
            raise TypeError("The angle must be a float")
        else:
            self.__angle = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, val):
        if type(val) != float and type(val) != int:
            raise TypeError("The coordinate must be an integer")
        else:
            self.__x = val

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, val):
        if type(val) != float and type(val) != int:
            raise TypeError("The coordinate must be an integer")
        else:
            self.__y = val

    def update(self):
        """Updates the enemy position and shoots"""
        # Randomly changes the angle of the plane
        # if randint(0, 20) == 1:
        #     self.angle += pi * randint(-1, 1)

        # Destroys the plane if it goes out of the screen by more than 30 pixels
        # TODO: Make this a constant and review the value
        if self.x - self.width < -30 or self.x > pyxel.width + 30 or self.y - self.height < -30 or self.y > pyxel.height + 30:
            self.health = 0

        self.x += self.speed * cos(radians(self.angle)) * constants.DELTA_TIME
        self.y += self.speed * sin(radians(self.angle)) * constants.DELTA_TIME
        if randint(0, 100) == 1:
            self.shoot()

        # Remove the shots that go off the screen
        for shot in self.shots:
            # Destroys the shot if it goes out of the screen
            if shot.x - shot.width < 0 or shot.x > pyxel.width or shot.y - shot.height < 0 or shot.y > pyxel.height:
                self.shots.remove(shot)

    # def draw(self):
    #     """Draws the enemy"""

    #     if self.angle == 90:
    #         pyxel.blt(self.x, self.y, 0, 3, 28, self.width, self.height, 0)
    #     elif self.angle == 270:
    #         pass
    #     else:
    #         raise Exception("The angle of the enemy is not supported")

    def shoot(self):
        """Shoots from the enemy(Creates an instance of the shot class)"""
        # Creates an instance of the shot class
        self.shots.append(Shot(self.x, self.y, 70, self.angle, "enemy"))
