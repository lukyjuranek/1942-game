class Shot:
    def __init__(self, x: float, y: float, health: int, speed: int, angle, pyxel):
        self.x = x
        self.y = y
        self.health = health
        self.speed = speed
        self.angle = angle
        self.pyxel = pyxel

    def draw(self):
        self.pyxel.blt(self.x, self.y, 0, 0, 16, 3, 19)