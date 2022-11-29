from Classes.plane import Plane

class Enemy(Plane):
    def __init__(self, x: float, y: float, health: int, speed: int, angle: int, pyxel):
        super().__init__(x, y, health, speed, pyxel)
        self.angle = angle

    @property
    def angle(self):
        return self.angle

    @angle.setter
    def angle(self, angle):
        