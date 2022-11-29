from Classes.shot import Shot
from math import pi

import pyxel

class Player():
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.width = 16
        self.height = 16
        self.speed = speed
        self.lives = 3
        self.shots = []

    def update(self):
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
        pyxel.blt(self.x, self.y, 0, 0, 0, self.width, self.height, 0)

    
    def shoot(self):
        # Creates an instance of the shot class
        self.shots.append(Shot(self.x, self.y, 100, 3, 3*pi/2))
        self.shots.append(Shot(self.x + self.width, self.y, 100, 3, 3*pi/2))