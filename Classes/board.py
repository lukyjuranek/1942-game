from Classes.player import Player
from Classes.enemy import Enemy
import pyxel

class Board:
    def __init__(self):
        self.width = 200
        self.height = 200
        self.player = Player(self.width/2, self.height - 40, 2)
        self.enemies = []
        self.bullets = []

    def drawText(self):
        pyxel.text(0, 0, "Score", 7)
        pyxel.text(self.width/2, 0, "1942", 7)