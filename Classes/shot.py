import pyxel
import constants
from math import sin, cos, radians

class Shot:
    """Class that represents a shot.

    Attributes:
        x (float): X coordinate of the shot
        y (float): Y coordinate of the shot
        speed (int): Speed of the shot
        angle (float): Angle of the shot
        shot_type (str): Type of the shot. It can be "player" or "enemy". This determines only the color of the shot
        width (int)(readonly): Width of the shot
        height (int)(readonly): Height of the shot

    Methods:
        update(): Updates the shot position
        draw(): Draws the shot
        """

    def __init__(self, x: float, y: float, speed: int, angle: float, shot_type: str):
        self.x = x
        self.y = y
        self.speed = speed
        self.angle = angle
        self.shot_type = shot_type

    @property
    def width(self):
        """This attribute is defined here and not in the init method in order for it to be read only."""
        return 4
    
    @property
    def height(self):
        """This attribute is defined here and not in the init method in order for it to be read only."""
        return 4

    @property
    def shot_type(self):
        return self.__shot_type

    @shot_type.setter
    def shot_type(self, value):
        if value != "player" and value != "enemy":
            raise ValueError("The shot type must be either 'player' or 'enemy'")
        else:
            self.__shot_type = value

    def update(self):
        """"Updates the shot position"""
        self.x += self.speed * cos(radians(self.angle)) * constants.DELTA_TIME
        self.y += self.speed * sin(radians(self.angle)) * constants.DELTA_TIME


    def draw(self):
        """Draws the shot"""
        if self.shot_type == "player":
            pyxel.blt(self.x, self.y, 0, 0, 16, self.width, self.height, 0)
        elif self.shot_type == "enemy":
            pyxel.blt(self.x, self.y, 0, 5, 16, self.width, self.height, 0)