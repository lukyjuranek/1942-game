from Classes.enemy import Enemy
import constants
import pyxel
from math import pi

class SuperBombardier(Enemy):
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
        return 18
    
    @property
    def height(self):
        return 18

    def draw(self):
        '''Draws the enemy'''
        if self.angle == 270:
            pyxel.blt(self.x, self.y, 0, 7, 128, self.width, self.height, 0)
        elif self.angle == 90:
            pyxel.blt(self.x, self.y, 0, 1, 105, self.width, self.height, 0)
        else:
            raise Exception("The angle of the enemy is not supported")