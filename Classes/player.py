from Classes.shot import Shot
import constants
from math import cos, sin, radians
import pyxel


class Player:
    """Class that represents the player.

    Attributes:
        x (float): X coordinate of the player
        y (float): Y coordinate of the player
        lives (int): Number of lives the player has
        score (int): Score of the player
        shots (list): List of the shots that the player has fired. It stores the shot instances.
        width (int)(readonly): Width of the player
        height (int)(readonly): Height of the player
        speed (int)(readonly): Speed of the player
        invincible (bool): If the player is invincible or not
        is_doing_loop (bool): If the player is doing a loop or not
        loop_distance (int): Distance of the loop. It is used as a loop timer
        flash_red (bool): If the player is flashing red or not
        hit_indicator_timer (int): Timer that is used to make the player flash red when hit. When hit the timer is set to a number and it is decremented every frame

    Methods:
        update(): Updates the player position and shoots if the appropriate key is pressed.
        register_hit(): Does the necessary actions when the player is hit.
        shoot(): Shoots a shot
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.lives = 3
        self.score = 0
        self.shots = []
        self.invincible = False
        self.is_doing_loop = False
        self.loop_distance = 40
        self.flash_red = False
        self.hit_indicator_timer = 0

    @property
    def width(self):
        return 16

    @property
    def height(self):
        return 14

    @property
    def speed(self):
        return 120

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int and type(value) != float:
            raise TypeError("The value must be an integer")
        else:
            self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int and type(value) != float:
            raise TypeError("The value must be an integer")
        else:
            self.__y = value

    @property
    def lives(self):
        return self.__lives

    @lives.setter
    def lives(self, value):
        if type(value) != int:
            raise TypeError("The number of lives must me an integer")
        else:
            self.__lives = value

    def update(self):
        """Updates the player position and shoots if the appropriate key is pressed"""

        # Booleeans that check if the player is on the edge of the screen
        top_edge = self.y > 0
        right_edge = self.x < pyxel.width - self.width
        left_edge = self.x > 0
        bottom_edge = self.y < pyxel.height - self.height

        # X and Y distances used for the diagonal movement
        diag_a = sin(radians(45))
        diag_b = cos(radians(45))

        if not self.is_doing_loop:
            # Player movement
            if pyxel.btn(pyxel.KEY_LEFT) and pyxel.btn(pyxel.KEY_UP) and left_edge and top_edge:
                # LEFT + UP
                self.x -= self.speed * diag_a * constants.DELTA_TIME
                self.y -= self.speed * diag_b * constants.DELTA_TIME
            elif pyxel.btn(pyxel.KEY_LEFT) and pyxel.btn(pyxel.KEY_DOWN) and left_edge and bottom_edge:
                # LEFT + DOWN
                self.x -= self.speed * diag_a * constants.DELTA_TIME
                self.y += self.speed * diag_b * constants.DELTA_TIME
            elif pyxel.btn(pyxel.KEY_RIGHT) and pyxel.btn(pyxel.KEY_UP) and right_edge and top_edge:
                # RIGHT + UP
                self.x += self.speed * diag_a * constants.DELTA_TIME
                self.y -= self.speed * diag_b * constants.DELTA_TIME
            elif pyxel.btn(pyxel.KEY_RIGHT) and pyxel.btn(pyxel.KEY_DOWN) and right_edge and bottom_edge:
                # RIGHT + DOWN
                self.x += self.speed * diag_a * constants.DELTA_TIME
                self.y += self.speed * diag_b * constants.DELTA_TIME
            elif pyxel.btn(pyxel.KEY_LEFT) and left_edge:
                # LEFT
                self.x -= self.speed * constants.DELTA_TIME
            elif pyxel.btn(pyxel.KEY_RIGHT) and right_edge:
                # RIGHT
                self.x += self.speed * constants.DELTA_TIME
            elif pyxel.btn(pyxel.KEY_UP) and top_edge:
                # UP
                self.y -= self.speed * constants.DELTA_TIME
            elif pyxel.btn(pyxel.KEY_DOWN) and bottom_edge:
                # DOWN
                self.y += self.speed * constants.DELTA_TIME

            if pyxel.btnp(pyxel.KEY_SPACE):
                self.shoot()

            if pyxel.btnp(pyxel.KEY_Z):
                self.is_doing_loop = True
                self.invincible = True
        else:
            # Loop movement
            self.loop_distance -= self.speed * constants.DELTA_TIME / 2
            self.y += self.speed * constants.DELTA_TIME / 2
            if self.loop_distance <= 0 or not bottom_edge:
                self.is_doing_loop = False
                self.invincible = False
                self.loop_distance = 40

        # Lets us pause the game for testing purposes
        if pyxel.btnp(pyxel.KEY_P):
            constants.DELTA_TIME = 0
        if pyxel.btnr(pyxel.KEY_P):
            constants.DELTA_TIME = 1/constants.FRAME_RATE

        # Remove the shots that go off the screen
        for shot in self.shots:
            # Destroys the shot if it goes out of the screen
            if shot.x - shot.width < 0 or shot.x > pyxel.width or shot.y - shot.height < 0 or shot.y > pyxel.height:
                self.shots.remove(shot)

    def draw(self):
        """Draws the player"""
        if self.is_doing_loop:
            # Draws the plane propeller
            if pyxel.frame_count % 4 == 0:
                pyxel.blt(self.x+5, self.y+self.height, 0, 0, 22, 6, 1, 0)
            else:
                pyxel.blt(self.x+5, self.y+self.height, 0, 0, 23, 6, 1, 0)
            # Draws the plane
            pyxel.blt(self.x, self.y, 0, 16, 0, self.width, self.height, 0)
        else:
            # Draws the plane propeller
            if pyxel.frame_count % 4 == 0:
                pyxel.blt(self.x+5, self.y-1, 0, 0, 22, 6, 1, 0)
            else:
                pyxel.blt(self.x+5, self.y-1, 0, 0, 23, 6, 1, 0)

            # Toggles the hit_indicator which makes the plane flash red when hit
            if pyxel.frame_count % 20 == 0 and self.hit_indicator_timer > 0:
                self.hit_indicator_timer -= 1
                # Toggles the hit indicator to make it blink
                self.flash_red = not self.flash_red
            elif self.hit_indicator_timer == 0:
                self.flash_red = False
                self.invincible = False

            # Draws the plane
            if self.flash_red:
                pyxel.blt(self.x, self.y, 0, 32, 2, self.width, self.height, 0)
            else:
                pyxel.blt(self.x, self.y, 0, 0, 2, self.width, self.height, 0)

    def register_hit(self):
        """Does the necessary actions when the player is hit."""
        self.lives -= 1
        # Starts flashing red
        self.hit_indicator_timer = 7
        self.invincible = True

    def shoot(self):
        """Shoots from the player(Creates an instance of the shot class)"""
        # Creates an instance of the shot class
        self.shots.append(Shot(self.x, self.y, 180, 270, "player"))
        self.shots.append(Shot(self.x + self.width-4, self.y, 180, 270, "player"))
