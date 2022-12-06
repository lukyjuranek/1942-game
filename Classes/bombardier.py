from Classes.enemy import Enemy
import constants
import pyxel
from math import pi

class Bombardier(Enemy):
    def __init__(self, x, y, angle):
        super().__init__(x, y, angle)
        self.gained_score = 100
        self.health = 2
        self.shots = []

    @property
    def speed(self):
        return 40

    @property
    def width(self):
        return 15
    
    @property
    def height(self):
        return 15

    # @property
    # def health(self):
    #     return self.__health

    # @health.setter
    # def health(self, value):
    #     if type(value) != int:
    #         raise TypeError("The health can be only an integer")
    #     else:
    #         self.__health = value

    def draw(self):
        '''Draws the enemy'''
        if self.angle == 270:
            pyxel.blt(self.x, self.y, 0, 1, 89, self.width, self.height, 0)
        elif self.angle == 90:
            pyxel.blt(self.x, self.y, 0, 1, 105, self.width, self.height, 0)
        else:
            raise Exception("The angle of the enemy is not supported")