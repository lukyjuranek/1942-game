from Classes.player import Player
from Classes.enemy import Enemy
from Classes.collisionChecker import CollisionChecker
import pyxel

class Board:
    '''
    Class that stores the board, the elements and some global variables of the game
    '''
    def __init__(self):
        self.width = 200
        self.height = 200
        self.player = Player(self.width/2, self.height - 40, 2)
        self.enemies = []
        self.enemyShots = []

    def updateAll(self):
        # Updates the player position
        self.player.update()

        # Updates the enemy positions and their shots
        for enemy in self.enemies:
            enemy.update()
            for shot in enemy.shots:
                shot.update()

        # Updates the shots
        for shot in self.player.shots:
            shot.update()

    def drawText(self):
        pyxel.text(0, 0, str(self.player.score), 7)
        pyxel.text(self.width/2, 0, "1942", 7)

    def drawAll(self):
        '''Draws all the elements in the game'''
        # Draws the text elements
        self.drawText()

        # Draws the player
        self.player.draw()
        # Draws the enemies and their shots
        for enemy in self.enemies:
            enemy.draw()
            for shot in enemy.shots:
                shot.draw()
                
        # Draws the shots
        for shot in self.player.shots:
            shot.draw()

    def checkAllCollisions(self):
        '''Checks all the collisions in the game and does the according actions'''
        # Checks if any enemy has collided with the player
        for enemy in self.enemies:
            if CollisionChecker.checkCollision(self.player, enemy):
                print("Player has collided with an enemy")
                # TODO: Reset game and remove a life

        # Checks if the player has shot an enemy
        for enemy in self.enemies:
            for shot in self.player.shots:
                if CollisionChecker.checkCollision(shot, enemy):
                    print("An enemy has been hit by the player")
                    # Adds the score to the player
                    self.player.score += enemy.gainedScore
                    self.enemies.remove(enemy)

        # Checks if any enemy has shot the player
        for enemy in self.enemies:
            for shot in enemy.shots:
                if CollisionChecker.checkCollision(shot, self.player):
                    print("Player has been shots ny an enemy")

        # TODO: Remove this code
        #         print("Player has been shots ny an enemy")
        # # Checks if any enemy has collided with the player
        # if CollisionChecker.checkCollisionList(self.player, self.enemies):
        #     print("Player has collided with an enemy")
        #     # TODO: Reset game and remove a life

        # # Checks if the player has shot an enemy
        # if CollisionChecker.checkCollisionListList(self.player.shots, self.enemies):
        #     print("An enemy has been hit by the player")
        #     # Adds the score to the player
        #     self.player.score += enemy.gainedScore
        #     self.enemies.remove(enemy)

        # # Checks if any has shot  the player
        # for enemy in self.enemies:
        #     if CollisionChecker.checkCollisionList(self.player, enemy.shots):