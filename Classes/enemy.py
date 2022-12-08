from Classes.shot import Shot
import constants
from random import randint
from math import sin, cos, radians
import pyxel


class Enemy:
    """Enemy class"""

    def __init__(self, x: float, y: float, angle: float):
        self.x = x
        self.y = y
        self.angle = angle
        self.health = 1
        self.shots = []

    @property
    def width(self):
        return 10

    @property
    def height(self):
        return 10

    @property
    def angle(self):
        return self.__angle

    @angle.setter
    def angle(self, value):
        if type(value) != float and type(value) != int:
            raise TypeError("The angle must be a float")
        else:
            # Makes the angle positive
            if value < 0:
                self.__angle = -value
            elif value == 360:
                self.__angle = 0
            else:
                self.__angle = value

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, value):
        if type(value) != int:
            raise TypeError("The health can be only an integer")
        else:
            self.__health = value

    @property
    def speed(self):
        return 40

    @speed.setter
    def speed(self, value):
        if type(value) != int and value < 0:
            raise TypeError(
                "The speed can be only an integer and greater than or equal to 0")
        else:
            self.__speed = value

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
        self.shots.append(Shot(self.x+self.width/2-2, self.y + self.height/2-2, 70, self.angle, "enemy"))
