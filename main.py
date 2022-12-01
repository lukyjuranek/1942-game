import pyxel
# from random import randint
# from Classes.player import Player
from Classes.board import Board
from Classes.enemy import Enemy
from Classes.redEnemy import RedEnemy
from Classes.regularEnemy import RegularEnemy
from Classes.bombardier import Bombardier
from Classes.superBomardier import SuperBombardier
# from Classes.collisionChecker import CollisionChecker
from math import pi


def update():
    # Updates all the elements in the game
    board.updateAll()
    # Checks all the collisions in the game
    board.checkAllCollisions()


def draw():
    pyxel.cls(6)
    # Draws all the elements in the game
    board.drawAll()


board = Board()
# Testing enemies
board.enemies.append(RegularEnemy(20, 50, pi/2))
board.enemies.append(RegularEnemy(100, 50, 3*pi/2))
board.enemies.append(RedEnemy(40, 10, pi/2))
board.enemies.append(RedEnemy(120, 30, 3*pi/2))

# Initializes and runs pyxel and loads the resources
pyxel.init(board.width, board.height, "1942")  # type: ignore
pyxel.load("pyxel_resource_file.pyxres")
pyxel.run(update, draw)