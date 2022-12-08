from Classes.enemy import Enemy
import constants
import pyxel
from math import cos, sin, radians
from random import randint


class RedEnemy(Enemy):
    """The red enemy class
    
    Attributes:
        health (int): The health of the enemy
        shots (list): The list of the shots of the enemy
        speed (int)(readonly): The speed of the enemy
        width (int)(readonly): The width of the enemy
        height (int)(readonly): The height of the enemy
        gained_score (int)(readonly): The score gained by killing the enemy

    Methods:
        draw(): Draws the enemy
        update(): Updates the enemy position and shoots
        """
    
    def __init__(self, x, y, angle):
        super().__init__(x, y, angle)
        self.health = 2
        self.shots = []

    @property
    def speed(self):
        return 50

    @property
    def width(self):
        return 10

    @property
    def height(self):
        return 10

    @property
    def gained_score(self):
        return 100

    def update(self):
        """Updates the enemy position and shoots"""
        # Randomly changes the angle of the plane
        if pyxel.frame_count % 60 == 0 and randint(0, 2) == 1:
            self.angle += 45 * randint(-2, 2)

        # Destroys the plane if it goes out of the screen by more than 30 pixels
        if self.x - self.width < -30 or self.x > pyxel.width + 30 or self.y - self.height < -30 or self.y > pyxel.height + 30:
            self.health = 0

        self.x += self.speed * cos(radians(self.angle)) * constants.DELTA_TIME
        self.y += self.speed * sin(radians(self.angle)) * constants.DELTA_TIME
        if randint(0, 100) == 1:
            self.shoot()

        # Remove the shots that go off the screen
        for shot in self.shots:
            # Destroys the shot if it goes out of the screen
            if shot.x - shot.width < 0 or shot.x > pyxel.width or shot.y - shot.height < 0 or shot.y > pyxel.height:
                self.shots.remove(shot)

    def draw(self):
        """Draws the enemy"""

        if self.angle == 270:
            # UP
            pyxel.blt(self.x, self.y, 0, 3, 59, self.width, self.height, 0)
        elif self.angle == 90:
            # DOWN
            pyxel.blt(self.x, self.y, 0, 3, 74, self.width, self.height, 0)
        elif self.angle == 180:
            # LEFT
            pyxel.blt(self.x, self.y, 0, 20, 59, self.width, self.height, 0)
        elif self.angle == 0:
            # RIGHT
            pyxel.blt(self.x, self.y, 0, 35, 75, self.width, self.height, 0)
        elif self.angle == 315:
            # RIGHT UP
            pyxel.blt(self.x, self.y, 0, 51, 76, self.width, self.height, 0)
        elif self.angle == 45:
            # RIGHT DOWN
            pyxel.blt(self.x, self.y, 0, 19, 75, self.width, self.height, 0)
        elif self.angle == 135:
            # LEFT DOWN
            pyxel.blt(self.x, self.y, 0, 52, 58, self.width, self.height, 0)
        elif self.angle == 225:
            # LEFT UP
            pyxel.blt(self.x, self.y, 0, 36, 60, self.width, self.height, 0)
        else:
            print("angle: ", self.angle)
            raise Exception("The angle of the enemy is not supported")
