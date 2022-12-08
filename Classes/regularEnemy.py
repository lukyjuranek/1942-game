from Classes.enemy import Enemy
import pyxel


class RegularEnemy(Enemy):
    """The regular enemy class
    
    Attributes:
        health (int): The health of the enemy
        shots (list): The list of the shots of the enemy
        speed (int)(readonly): The speed of the enemy
        width (int)(readonly): The width of the enemy
        height (int)(readonly): The height of the enemy
        gained_score (int)(readonly): The score gained by killing the enemy

    Methods:
        draw(): Draws the enemy
        """

    def __init__(self, x, y, angle):
        super().__init__(x, y, angle)
        self.health = 1
        self.shots = []

    @property
    def speed(self):
        return 40

    @property
    def width(self):
        return 10

    @property
    def height(self):
        return 10

    @property
    def gained_score(self):
        return 50

    def draw(self):
        """Draws the enemy"""

        if self.angle == 270:
            pyxel.blt(self.x, self.y, 0, 3, 28, self.width, self.height, 0)
        elif self.angle == 90:
            pyxel.blt(self.x, self.y, 0, 3, 43, self.width, self.height, 0)
        else:
            raise Exception("The angle of the enemy is not supported")
