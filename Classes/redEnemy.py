from Classes.enemy import Enemy
import pyxel
from math import pi

class RedEnemy(Enemy):
    def __init__(self, x, y, angle):
        super().__init__(x, y, angle)
        self.speed = 3
        self.width = 10
        self.height = 9
        self.gainedScore = 100
        self.health = 2
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

        if self.angle == 3*pi/2:
            pyxel.blt(self.x, self.y, 0, 3, 60, self.width, self.height, 0)
        elif self.angle == pi/2:
            pyxel.blt(self.x, self.y, 0, 3, 75, self.width, self.height, 0)
        else:
            raise Exception("The angle of the enemy is not supported")
