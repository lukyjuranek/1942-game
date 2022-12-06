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
    """Class that stores the board, the elements and some global variables of the game like the game state"""
    def __init__(self):
        self.width = 200
        self.height = 200
        self.player = Player(self.width/2, self.height - 40)
        self.enemies = []
        self.enemy_shots = []
        self.high_score = 0
        self.bg_offset = 0
        self.game_state = "start_screen"
        self.island_position_x = 30
        self.island_position_y = -40

    def update(self):
        """Updates the game"""
        if self.game_state == "start_screen" and pyxel.btnp(pyxel.KEY_SPACE):
            self.game_state = "game"
        elif self.game_state == "game":
            # Updates all the elements in the game
            self.update_game_elements()

            # Checks all the collisions in the game
            self.check_all_collisions()

            # Makes the background scroll
            self.bg_offset += self.player.speed * constants.DELTA_TIME /5
            if self.bg_offset > 16:
                self.bg_offset = 0
        elif self.game_state == "game_over" and pyxel.btnp(pyxel.KEY_SPACE):
            self.game_state = "start_screen"
            self.player = Player(self.width/2, self.height - 40)
            self.enemies = []
            

    def draw(self):
        """Draws all the elements in the game. Runs the corresponding draw function depending on the game state"""
        if self.game_state == "start_screen":
            self.draw_start_screen()
        elif self.game_state == "game":
            self.draw_game_screen()
        elif self.game_state == "game_over":
            self.draw_game_over_screen()
        
    def draw_start_screen(self):
        """Draws the start screen"""
        pyxel.cls(0)
        pyxel.text(self.width/2-40, 150, "Press Space to start", self.blinking_color(7))
        pyxel.blt(self.width/2-32, self.height/2-15, 0, 136, 56, 64, 32, 0)
        self.draw_stats()

    def draw_game_over_screen(self):
        """Draws the game over screen"""
        pyxel.cls(0)
        pyxel.text(self.width/2-40, 150, "Press Space to restart", self.blinking_color(7))
        pyxel.blt(self.width/2-32, self.height/2-15, 0, 138, 18, 60, 30, 0)
        self.draw_stats()

    def draw_game_screen(self):
        """Draws the game"""
        pyxel.cls(6)
        # Draws the background
        self.draw_background()
        self.draw_and_update_island()

        # Draws the text elements
        self.draw_stats()

        # Draws the player
        self.player.draw()
        # Draws the enemies and their shots
        for enemy in self.enemies:
            for shot in enemy.shots:
                shot.draw()
            enemy.draw()

        # Draws the shots
        for shot in self.player.shots:
            shot.draw()


    def update_game_elements(self):
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
            self.enemies.append(RegularEnemy(randint(20, self.width-20), 0, 90))
        if randint(0, 100) == 1:
            self.enemies.append(RedEnemy(0, randint(0, self.height-50), 0))
        if randint(0, 200) == 1:
            self.enemies.append(Bombardier(randint(20, self.width-20), 0, 90))
        if randint(0, 400) == 1:
            self.enemies.append(SuperBombardier(randint(20, self.width-20), self.height, 270))

    def draw_stats(self):
        """Draws the text elements in the game"""
        pyxel.text(2, 2, "SCORE", 7)
        pyxel.text(2, 10, str(self.player.score), 7)
        pyxel.text(self.width/2-15, 2, "HIGH SCORE", 7)
        pyxel.text(self.width/2-10, 10, str(self.high_score), 7)

        pyxel.text(self.width-20, 10, str(self.player.lives)+"x", 7)
        pyxel.blt(self.width-10, 8, 0, 16, 16, 8, 8, 0)

    def draw_and_update_island(self):
        """Draws the player"""
        self.island_position_y += self.player.speed * constants.DELTA_TIME /5
        pyxel.blt(self.island_position_x, self.island_position_y, 0, 89, 114, 30, 30, 0)
        if self.island_position_y > self.height:
            self.island_position_y = -60
            self.island_position_x = randint(0, self.width-30)
            

    def draw_background(self):
        """Draws the background of the game"""
        for x in range(0, self.width//16+1):
            for y in range(-16, self.height//16+1):
                pyxel.blt(x*16, y*16 + self.bg_offset, 0, 48, 0, 16, 16, 0)

    def check_collision(self, ob1, ob2):
        """Checks if the ob1(object1) and ob2(object2) are overlapping"""
        if ob1.x < ob2.x + ob2.width and ob1.x + ob1.width > ob2.x and ob1.y < ob2.y + ob2.height and ob1.height + ob1.y > ob2.y:
            return True
        else:
            return False

    def check_all_collisions(self):
        """Checks all the collisions in the game and does the according actions"""

        if not self.player.invincible:
            
            # Checks if any enemy has collided with the player
            for enemy in self.enemies:
                if self.check_collision(self.player, enemy):
                    self.enemies.remove(enemy)
                    self.player.register_hit()
                    if self.player.lives <= 0:
                        self.game_state = "game_over"

            # Checks if any enemy has shot the player
            for enemy in self.enemies:
                for shot in enemy.shots:
                    if self.check_collision(shot, self.player):
                        enemy.shots.remove(shot)
                        self.player.register_hit()
                        if self.player.lives <= 0:
                            self.game_state = "game_over"

        # Checks if the player has shot an enemy
        for enemy in self.enemies:
            for shot in self.player.shots:
                if self.check_collision(shot, enemy):
                    # Adds the score to the player
                    self.player.score += enemy.gained_score
                    if self.player.score > self.high_score:
                        self.high_score = self.player.score

                    enemy.health -= 1

                    self.player.shots.remove(shot)

    def blinking_color(self, color):
        """Makes a color blink and is controlled by the frame count"""
        if pyxel.frame_count % 30 < 15:
            return color
        else:
            return color
