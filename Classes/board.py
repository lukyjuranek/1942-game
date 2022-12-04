from Classes.player import Player
from Classes.enemy import Enemy
from Classes.redEnemy import RedEnemy
from Classes.regularEnemy import RegularEnemy
from Classes.bombardier import Bombardier
from Classes.superBombardier import SuperBombardier
import constants
import pyxel
from random import randint


class Board:
    """Class that stores the board, the elements and some global variables of the game"""
    def __init__(self):
        self.width = 200
        self.height = 200
        self.player = Player(self.width/2, self.height - 40)
        self.enemies = []
        self.enemy_shots = []
        self.bg_offset = 0

    def update(self):
        # Updates all the elements in the game
        self.update_all()
        # Checks all the collisions in the game
        self.check_all_collisions()

        # Makes the background scroll
        self.bg_offset += self.player.speed * constants.DELTA_TIME /2
        if self.bg_offset > 16:
            self.bg_offset = 0

    def draw(self):
        """Draws all the elements in the game"""
        pyxel.cls(6)
        # Draws the background
        self.draw_background()
        # Draws the text elements
        self.draw_text()

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

    def update_all(self):
        """Updates all the elements in the game and does the according actions(like removing enemies)"""
        # Updates the player position
        self.player.update()

        # Updates the player's shots
        for shot in self.player.shots:
            shot.update()

        # Updates the enemy positions and their shots
        for enemy in self.enemies:
            # Removes the enemy if it has 0 health
            if enemy.health <= 0:
                self.enemies.remove(enemy)
            enemy.update()
            for shot in enemy.shots:
                shot.update()

        # Randomly spawns enemies
        if randint(0, 100) == 1:
            self.enemies.append(RegularEnemy(randint(0, self.width), 0, 90))
        if randint(0, 100) == 1:
            self.enemies.append(RedEnemy(0, randint(0, self.height), 0))
        # if randint(0, 100) == 1:
        #     self.enemies.append(Bombardier(randint(0, self.width), 0, 90))

    def draw_text(self):
        """Draws the text elements in the game"""
        pyxel.text(2, 2, "SCORE", 7)
        pyxel.text(2, 10, str(self.player.score), 7)
        pyxel.text(self.width/2-15, 2, "HIGH SCORE", 7)
        pyxel.text(self.width/2-10, 10, str(self.player.high_score), 7)

    def draw_background(self):
        """Draws the background of the game"""
        for x in range(0, self.width//16+1):
            for y in range(-16, self.height//16+1):
                pyxel.blt(x*16, y*16 + self.bg_offset, 0, 80, 144, 16, 16, 0)

    def check_collision(self, ob1, ob2):
        """Checks if the ob1(object1) and ob2(object2) are overlapping"""
        if ob1.x < ob2.x + ob2.width and ob1.x + ob1.width > ob2.x and ob1.y < ob2.y + ob2.height and ob1.height + ob1.y > ob2.y:
            return True
        else:
            return False

    def check_all_collisions(self):
        """Checks all the collisions in the game and does the according actions"""

        if not self.player.is_doing_loop:
            
            # Checks if any enemy has collided with the player
            for enemy in self.enemies:
                if self.check_collision(self.player, enemy):
                    print("Player has collided with an enemy")
                    # TODO: Reset game and remove a life

            # Checks if any enemy has shot the player
            for enemy in self.enemies:
                for shot in enemy.shots:
                    if self.check_collision(shot, self.player):
                        print("Player has been shots ny an enemy")

        # Checks if the player has shot an enemy
        for enemy in self.enemies:
            for shot in self.player.shots:
                if self.check_collision(shot, enemy):
                    print("An enemy has been hit by the player")
                    # Adds the score to the player
                    self.player.score += enemy.gained_score
                    if self.player.score > self.player.high_score:
                        self.player.high_score = self.player.score

                    self.enemies.remove(enemy)

                    self.player.shots.remove(shot)
