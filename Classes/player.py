from Classes.shot import Shot
from Classes.frameRate import FrameRate
from math import pi
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
        if pyxel.btn(pyxel.KEY_LEFT) and self.x > 0:
            self.x -= self.speed * FrameRate.delta_time

        if pyxel.btn(pyxel.KEY_RIGHT) and self.x < pyxel.width - self.width:
            self.x += self.speed * FrameRate.delta_time

        if pyxel.btn(pyxel.KEY_UP) and self.y > 0:
            self.y -= self.speed * FrameRate.delta_time
        
        if pyxel.btn(pyxel.KEY_DOWN) and self.y < pyxel.height - self.height:
            self.y += self.speed * FrameRate.delta_time

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
        self.shots.append(Shot(self.x, self.y, 180, 270))
        self.shots.append(Shot(self.x + self.width, self.y, 180, 270))
