import pyxel
# from random import randint
from Classes.enemy import Enemy
# from Classes.player import Player
from Classes.board import Board


def update():
    # Updates the player position
    board.player.update()
    # Updates the enemy positions
    for enemy in board.enemies:
        enemy.update()
    # Updates the shots
    for shot in board.player.shots:
        shot.update()


def draw():
    pyxel.cls(0)
    # pyxel.text(WIDTH/2, HEIGHT/2, "1942", 7)
    # pyxel.blt(x:int, y:int, bank:int, u:int, v:int, w:int, h:int)
    # pyxel.blt(50, 50, 0, 0, 0, 16, 16)

    # Draws the player
    board.player.draw()
    # Draws the enemies
    for enemy in board.enemies:
        enemy.draw()
    # Draws the shots
    for shot in board.player.shots:
        shot.draw()


    # Draws the bullet to test it
    pyxel.blt(20, 20, 0, 0, 16, 4, 19)


board = Board()
# Tests one enemy
board.enemies.append(Enemy(10, 10, 100, 1, 0))
# player = Player(WIDTH/2, HEIGHT - 40, 100, 0, 0)


# Runs pyxel
pyxel.init(board.width, board.height, "Hello Pyxel")
pyxel.load("pyxel_resource_file.pyxres")
pyxel.run(update, draw)
