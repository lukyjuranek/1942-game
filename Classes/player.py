from Classes.shot import Shot
from math import pi
import pyxel

class Player():
    '''Player class'''
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 16
        self.height = 14
        self.speed = 2
        self.lives = 3
        self.score = 0
        self.shots = []

    def update(self):
        '''Updates the player position and shoots if the appropriate key is pressed'''
        if pyxel.btn(pyxel.KEY_LEFT) and self.x > 0:
            self.x -= self.speed

        if pyxel.btn(pyxel.KEY_RIGHT) and self.x < pyxel.width - self.width:
            self.x += self.speed

        if pyxel.btn(pyxel.KEY_UP) and self.y > 0:
            self.y -= self.speed
        
        if pyxel.btn(pyxel.KEY_DOWN) and self.y < pyxel.height - self.height:
            self.y += self.speed

        if pyxel.btnp(pyxel.KEY_SPACE):
            self.shoot()

    def draw(self):
        '''Draws the player'''
        pyxel.blt(self.x, self.y, 0, 0, 2, self.width, self.height, 0)

    
    def shoot(self):
        '''Shoots from the player(Creates an instance of the shot class)'''
        # Creates an instance of the shot class
        self.shots.append(Shot(self.x, self.y, 3, 270))
        self.shots.append(Shot(self.x + self.width, self.y, 3, 270))