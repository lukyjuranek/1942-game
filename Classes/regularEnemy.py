from Classes.enemy import Enemy
from Classes.frameRate import FrameRate
import pyxel
from math import pi

class RegularEnemy(Enemy):
    def __init__(self, x, y, angle):
        super().__init__(x, y, angle)
        self.speed = 40
        self.width = 10
        self.height = 9
        self.gainedScore = 50
        self.health = 1
        self.shots = []

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, value):
        if type(value) != int:
            raise TypeError("The health can be only an integer")
        else:
            self.__health = value

    def draw(self):
        '''Draws the enemy'''
        if self.angle == 270:
            pyxel.blt(self.x, self.y, 0, 3, 28, self.width, self.height, 0)
        elif self.angle == 90:
            pyxel.blt(self.x, self.y, 0, 3, 43, self.width, self.height, 0)
        else:
            raise Exception("The angle of the enemy is not supported")