from Classes.enemy import Enemy
from Classes.frameRate import FrameRate
import pyxel
from math import pi


class RedEnemy(Enemy):
    def __init__(self, x, y, angle):
        super().__init__(x, y, angle)
        self.speed = 80
        self.width = 10
        self.height = 10
        self.gained_score = 100
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
        """Draws the enemy"""

        if self.angle == 270:
            # UP
            pyxel.blt(self.x, self.y, 0, 3, 59, self.width, self.height, 0)
        elif self.angle == 90:
            # DOWN
            pyxel.blt(self.x, self.y, 0, 3, 74, self.width, self.height, 0)
        elif self.angle == 180:
            # LEFT
            pyxel.blt(self.x, self.y, 0, 20, 59, self.width, self.height, 0)
        elif self.angle == 0:
            # RIGHT
            pyxel.blt(self.x, self.y, 0, 35, 75, self.width, self.height, 0)
        else:
            print("angle: ", self.angle)
            raise Exception("The angle of the enemy is not supported")
