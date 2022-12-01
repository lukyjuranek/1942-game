from Classes.enemy import Enemy


class Bombardier(Enemy):
    def __init__(self, x, y, angle):
        super().__init__(self, x, y, angle)
        self.speed = 1
        self.width = 10
        self.height = 9
        self.gainedScore = 150
        self.health = 3
        self.shots = []