import pyxel
# from random import randint
from Classes.enemy import Enemy
# from Classes.player import Player
from Classes.board import Board
from Classes.collisionChecker import CollisionChecker
from math import pi


def update():
    board.updateAll()
    board.checkAllCollisions()


def draw():
    pyxel.cls(6)
    # Draws all the elements in the game
    board.drawAll()


board = Board()
# collisionChecker = CollisionChecker()
# Testing enemies
board.enemies.append(Enemy(20, 10, pi/2, 1, 1))
board.enemies.append(Enemy(100, 30, pi/2, 1, 1))

# Initializes and runs pyxel and loads the resources
pyxel.init(board.width, board.height, "1942")
pyxel.load("pyxel_resource_file.pyxres")
pyxel.run(update, draw)