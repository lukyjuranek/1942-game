from Classes.enemy import Enemy


class RegularEnemy(Enemy):
    def __init__(self, x, y, angle):
        super().__init__(self, x, y, angle)
        self.speed = 2
        self.width = 10
        self.height = 9
        self.gainedScore = 50
        self.health = 1
        self.shots = []




