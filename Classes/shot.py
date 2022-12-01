import pyxel
import constants
from math import sin, cos, radians

class Shot:
    def __init__(self, x: float, y: float, speed: int, angle: float, shot_type: str):
        self.x = x
        self.y = y
        self.speed = speed
        self.angle = angle
        self.width = 4
        self.height = 4
        self.shot_type = shot_type
        # TODO: Change speed of shots depending on the type of shot

    def update(self):
        '''Updates the shot position'''
        self.x += self.speed * cos(radians(self.angle)) * constants.DELTA_TIME
        self.y += self.speed * sin(radians(self.angle)) * constants.DELTA_TIME


    def draw(self):
        '''Draws the shot'''
        if self.shot_type == "player":
            pyxel.blt(self.x, self.y, 0, 0, 16, self.width, self.height, 0)
        elif self.shot_type == "enemy":
            pyxel.blt(self.x, self.y, 0, 5, 16, self.width, self.height, 0)