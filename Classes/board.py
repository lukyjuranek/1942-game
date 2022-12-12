from Classes.player import Player
from Classes.redEnemy import RedEnemy
from Classes.regularEnemy import RegularEnemy
from Classes.bombardier import Bombardier
from Classes.superBombardier import SuperBombardier
import constants
import pyxel
from random import randint


class Board:
    """Class that stores the board, the main game elements and some global variables of the game like the game state
    
    Attributes:
        player (Player): Player instance. It stores the player object.
        enemies (list): List of the enemies that are currently on the board.
        high_score (int): High score of the game.
        bg_offset (float): Background offset. It is used to make the background scroll.
        game_state (str): Game state. It can be one of the following: "start_screen", "game", "game_over"
        width (int)(readonly): Width of the board
        height (int)(readonly): Height of the board
        island_position_x (float): X coordinate of the island. Used to make the island move.
        island_position_y (float): Y coordinate of the island. Used to make the island move.

    Methods:
        update(): Updates the board. The main game loop is in this method. It's called every frame directly from the main.py file.
        draw(): Draws the board. Same as the update method, it's called every frame directly from the main.py file.

        __draw_start_screen(): Draws the start screen.
        __draw_game_over_screen(): Draws the game over screen.
        __draw_game(): Draws the game.

        __draw_background(): Draws the background.
        __draw_stats(): Draws the stats like the score, the lives and the high score.
        __draw_and_update_island(): Draws and updates the island.

        __update_game_elements(): Updates all the elements in the game and does the according actions(like removing enemies)
        __check_collision(): Checks if two objects are colliding(overlapping) or not.
        __check_all_collisions(): Checks all the collisions in the game and does the according actions(like removing enemies)

        __blinking_color(): Returns the color that should be used for the blinking effect and black alternately.
    """

    def __init__(self):
        self.player = Player(self.width/2-8, self.height - 40)
        self.enemies = []
        self.high_score = 0
        self.bg_offset = 0
        self.game_state = "start_screen"
        self.island_position_x = 30
        self.island_position_y = -40

    @property
    def width(self):
        return 200

    @property
    def height(self):
        return 200

    @property
    def high_score(self):
        return self.__high_score

    @high_score.setter
    def high_score(self, value):
        if type(value) != int or value < 0:
            raise TypeError(
                "The high score can be only an integer and greater than or equal to 0")
        else:
            self.__high_score = value

    @property
    def game_state(self):
        return self.__game_state

    @game_state.setter
    def game_state(self, value):
        if type(value) != str:
            raise TypeError("The game state can be only a string")
        elif value not in ["start_screen", "game", "game_over"]:
            raise ValueError(
                "The game state must be one of the following: 'start_screen', 'game', 'game_over'")
        else:
            self.__game_state = value

    @property
    def bg_offset(self):
        return self.__bg_offset

    @bg_offset.setter
    def bg_offset(self, value):
        if type(value) != int and type(value) != float:
            raise TypeError(
                "The background offset can be only an integer or a float")
        else:
            self.__bg_offset = value

    @property
    def island_position_x(self):
        return self.__island_position_x

    @island_position_x.setter
    def island_position_x(self, value):
        if type(value) != int and type(value) != float:
            raise TypeError(
                "The island position y can be only an integer or a float")
        else:
            self.__island_position_x = value

    @property
    def island_position_y(self):
        return self.__island_position_y

    @island_position_y.setter
    def island_position_y(self, value):
        if type(value) != int and type(value) != float:
            raise TypeError(
                "The island position y can be only an integer or a float")
        else:
            self.__island_position_y = value

    def update(self):
        """Updates all the elements in the game. Runs the corresponding update function depending on the game state"""
        if self.game_state == "start_screen" and pyxel.btnp(pyxel.KEY_SPACE):
            self.game_state = "game"

        elif self.game_state == "game_over" and pyxel.btnp(pyxel.KEY_R):
            self.game_state = "start_screen"
            self.player = Player(self.width/2, self.height - 40)
            self.enemies = []

        elif self.game_state == "game":
            # Updates all the elements in the game
            self.__update_game_elements()

            # Checks all the collisions in the game
            self.__check_all_collisions()

            # Makes the background scroll
            self.bg_offset += self.player.speed * constants.DELTA_TIME / 5
            if self.bg_offset > 16:
                self.bg_offset = 0
                
    def draw(self):
        """Draws all the elements in the game. Runs the corresponding draw function depending on the game state"""
        if self.game_state == "start_screen":
            self.__draw_start_screen()
            
        elif self.game_state == "game":
            self.__draw_game_screen()

        elif self.game_state == "game_over":
            self.__draw_game_over_screen()

    def __draw_start_screen(self):
        """Draws the start screen"""
        pyxel.cls(0)
        pyxel.text(self.width/2-40, 150, "Press Space to start", self.__blinking_color(7))
        pyxel.blt(self.width/2-32, self.height/2-15, 0, 136, 56, 64, 32, 0)
        self.__draw_stats()

    def __draw_game_over_screen(self):
        """Draws the game over screen"""
        pyxel.cls(0)
        pyxel.text(self.width/2-36, 150, "Press R to restart", self.__blinking_color(7))
        # Game over text
        pyxel.blt(self.width/2-29, self.height/2-15, 0, 138, 18, 60, 30, 0)
        self.__draw_stats()

    def __draw_game_screen(self):
        """Draws the game"""
        # Clears the screen
        pyxel.cls(6)
        # Draws the background
        self.__draw_background()
        self.__draw_and_update_island()

        # Draws the text elements
        self.__draw_stats()

        # Draws the player
        self.player.draw()
        # Draws the enemies and their shots
        for enemy in self.enemies:
            for shot in enemy.shots:
                shot.draw()
            enemy.draw()

        # Draws the player shots
        for shot in self.player.shots:
            shot.draw()

    def __update_game_elements(self):
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
        if randint(0, 1200) == 1:
            self.enemies.append(SuperBombardier(randint(20, self.width-20), self.height, 270))

    def __draw_stats(self):
        """Draws the text elements in the game like score, highscore and lives indicator"""
        pyxel.text(2, 2, "SCORE", 7)
        pyxel.text(2, 10, str(self.player.score), 7)
        pyxel.text(self.width/2-15, 2, "HIGH SCORE", 7)
        pyxel.text(self.width/2-10, 10, str(self.high_score), 7)

        pyxel.text(self.width-20, 5, str(self.player.lives)+"x", 7)
        pyxel.blt(self.width-10, 3, 0, 16, 16, 8, 8, 0)

    def __draw_and_update_island(self):
        """Draws the island and updates its position"""
        self.island_position_y += self.player.speed * constants.DELTA_TIME / 5
        pyxel.blt(self.island_position_x, self.island_position_y, 0, 89, 114, 30, 30, 0)
        if self.island_position_y > self.height:
            self.island_position_y = -60
            self.island_position_x = randint(0, self.width-30)

    def __draw_background(self):
        """Draws the background of the game"""
        for x in range(0, self.width//16+1):
            for y in range(-16, self.height//16+1):
                pyxel.blt(x*16, y*16 + self.bg_offset, 0, 48, 0, 16, 16, 0)

    def __check_collision(self, ob1, ob2):
        """Checks if the ob1(object1) and ob2(object2) are overlapping"""
        if ob1.x < ob2.x + ob2.width and ob1.x + ob1.width > ob2.x and ob1.y < ob2.y + ob2.height and ob1.height + ob1.y > ob2.y:
            return True
        else:
            return False

    def __check_all_collisions(self):
        """Checks all the collisions in the game and does the according actions"""

        if not self.player.invincible:

            # Checks if any enemy has collided with the player
            for enemy in self.enemies:
                if self.__check_collision(self.player, enemy):
                    self.enemies.remove(enemy)
                    self.player.register_hit()
                    if self.player.lives <= 0:
                        self.game_state = "game_over"

            # Checks if any enemy has shot the player
            for enemy in self.enemies:
                for shot in enemy.shots:
                    if self.__check_collision(shot, self.player):
                        enemy.shots.remove(shot)
                        self.player.register_hit()
                        if self.player.lives <= 0:
                            self.game_state = "game_over"

        # Checks if the player has shot an enemy
        for enemy in self.enemies:
            for shot in self.player.shots:
                if self.__check_collision(shot, enemy):
                    # Adds the score to the player
                    self.player.score += enemy.gained_score
                    if self.player.score > self.high_score:
                        self.high_score = self.player.score

                    enemy.health -= 1

                    self.player.shots.remove(shot)

    def __blinking_color(self, color):
        """Makes a color blink and is controlled by the frame count. Returns the color and black alternatively"""
        if pyxel.frame_count % 30 < 15:
            return color
        else:
            return 0