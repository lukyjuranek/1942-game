from Classes.shot import Shot
import constants
from math import pi, cos, sin, radians
import pyxel

class Player:
    """Player class"""
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 16
        self.height = 14
        self.speed = 120
        self.lives = 3
        self.score = 0
        self.shots = []

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

        # Remove the shots that go off the screen
        for shot in self.shots:
            # Destroys the shot if it goes out of the screen
            if shot.x - shot.width < 0 or shot.x > pyxel.width or shot.y - shot.height < 0 or shot.y > pyxel.height:
                self.shots.remove(shot)

    def draw(self):
        """Draws the player"""
        pyxel.blt(self.x, self.y, 0, 0, 2, self.width, self.height, 0)

    def shoot(self):
        """Shoots from the player(Creates an instance of the shot class)"""
        # Creates an instance of the shot class
        self.shots.append(Shot(self.x, self.y, 180, 270, "player"))
        self.shots.append(Shot(self.x + self.width, self.y, 180, 270, "player"))
