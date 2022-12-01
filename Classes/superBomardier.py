from Classes.enemy import Enemy


class SuperBombardier(Enemy):
    def __init__(self, x, y, angle):
        super().__init__(self, x, y, angle)
        self.speed = 1
        self.width = 10
        self.height = 9
        self.gainedScore = 200
        self.health = 4
        self.shots = []

# 4 shots will kill him, but on 3 shots we can do that he blinks to show that he is about to die.
