from Classes.player import Player
from Classes.enemy import Enemy

class Board:
    def __init__(self):
        self.width = 200
        self.height = 200
        self.player = Player(self.width/2, self.height - 40, 2)
        self.enemies = []
        self.bullets = []