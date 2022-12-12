from Classes.enemy import Enemy
from Classes.shot import Shot
import constants
import pyxel
from math import cos, sin, atan2, degrees, radians


class SuperBombardier(Enemy):
    """The regular enemy class
    
    Attributes:
        health (int): The health of the enemy
        shots (list): The list of the shots of the enemy
        speed (int)(readonly): The speed of the enemy
        width (int)(readonly): The width of the enemy
        height (int)(readonly): The height of the enemy
        gained_score (int)(readonly): The score gained by killing the enemy

    Methods:
        update(): Updates the enemy
        draw(): Draws the enemy
        shoot(): Shoots a shot. Shoots at the screen center
        """

    def __init__(self, x, y, angle):
        super().__init__(x, y, angle)
        self.health = 10
        self.speed = 40
        self.shots = []
        self.flash = False

    @property
    def width(self):
        return 18

    @property
    def height(self):
        return 18

    @property
    def gained_score(self):
        return 300

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, value):
        if type(value) != int and value < 0:
            raise TypeError(
                "The speed can be only an integer and greater than or equal to 0")
        else:
            self.__speed = value

    @property
    def flash(self):
        return self.__flash

    @flash.setter
    def flash(self, value):
        if type(value) != bool:
            raise TypeError("The flash can be only a boolean")
        else:
            self.__flash = value

    def update(self):
        """Updates the enemy"""

        self.x += self.speed * cos(radians(self.angle)) * constants.DELTA_TIME
        self.y += self.speed * sin(radians(self.angle)) * constants.DELTA_TIME
        if pyxel.frame_count % 40 == 0:
            self.shoot()

        # Makes the enemy stop when it reaches the top of the screen
        if self.y < 40:
            self.speed = 0

        # Remove the shots that go off the screen
        for shot in self.shots:
            # Destroys the shot if it goes out of the screen
            if shot.x - shot.width < 0 or shot.x > pyxel.width or shot.y - shot.height < 0 or shot.y > pyxel.height:
                self.shots.remove(shot)

    def draw(self):
        """Draws the enemy"""
        if self.angle == 270:
            # Makes the enemy flash red when it's low on health
            if self.health <= 2 and pyxel.frame_count % 20 == 0:
                self.flash = not self.flash

            if self.flash:
                pyxel.blt(self.x, self.y, 0, 7, 144, self.width, self.height, 0)
            else:
                pyxel.blt(self.x, self.y, 0, 7, 120, self.width, self.height, 0)

        elif self.angle == 90:
            pyxel.blt(self.x, self.y, 0, 1, 105, self.width, self.height, 0)
        else:
            raise Exception("The angle of the enemy is not supported")

    def shoot(self):
        """Shoots from the enemy. Makes the super bombardier shoot at the screen center"""
        # Calculates the angle between the enemy and the screen center
        x_diff = pyxel.width/2 - self.x
        y_diff = pyxel.height/2 - self.y
        shot_angle = degrees(atan2(y_diff, x_diff))

        self.shots.append(Shot(self.x+self.width/2-2, self.y + self.height/2-2, 70, shot_angle, "enemy"))
