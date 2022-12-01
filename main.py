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
import constants
from math import pi


def update():
    # Updates all the elements in the game
    board.update_all()
    # Checks all the collisions in the game
    board.check_all_collisions()


def draw():
    pyxel.cls(6)
    # Draws all the elements in the game
    board.draw_all()

# Initializes the board object
board = Board()

# Creates some enemies for testing purposes
board.enemies.append(RegularEnemy(20, 50, 90))
board.enemies.append(RegularEnemy(100, 50, 270))
board.enemies.append(RedEnemy(40, 10, 90))
board.enemies.append(RedEnemy(120, 30, 270))
board.enemies.append(RedEnemy(40, 10, 0))
board.enemies.append(RedEnemy(120, 30, 180))

# Initializes and runs pyxel and loads the resources
pyxel.init(board.width, board.height, "1942", fps=constants.FRAME_RATE)  # type: ignore
pyxel.load("pyxel_resource_file.pyxres")
pyxel.run(update, draw)
