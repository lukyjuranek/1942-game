import pyxel
from random import randint
from Classes.plane import Plane
from Classes.player import Player


def update():
    # Updates the player position
    player.update()
    # Updates the enemy positions
    for enemy in enemies:
        enemy.update()


def draw():
    pyxel.cls(0)
    pyxel.text(WIDTH/2, HEIGHT/2, "1942", 7)
    # pyxel.blt(x:int, y:int, bank:int, u:int, v:int, w:int, h:int)
    # pyxel.blt(50, 50, 0, 0, 0, 16, 16)

    # Draws the player
    player.draw()
    # Draws the enemies
    for enemy in enemies:
        enemy.draw()
    # Draws the bullets
    for shot in player.shots:
        shot.draw()

    # Draws the bullet to test it
    pyxel.blt(20, 20, 0, 0, 16, 4, 19)


HEIGHT = 200
WIDTH = 200

enemies = []
# bullets = []

# Tests one enemy
enemies.append(Plane(10, 10, 100, 1, 0))
player = Plane(WIDTH/2, HEIGHT - 40, 100, 0, 0)

# Runs pyxel
pyxel.init(WIDTH, HEIGHT, "Hello Pyxel")
pyxel.load("pyxel_resource_file.pyxres")
pyxel.run(update, draw)
