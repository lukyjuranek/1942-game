from Classes.enemy import Enemy


class RedEnemy(Enemy):
    def __init__(self, x, y, angle):
        super().__init__(x, y, angle)
        self.speed = 3
        self.width = 10
        self.height = 9
        self.gainedScore = 100
        self.health = 2
        self.shots = []

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, value):
        if type(value) != int:
            raise TypeError("The health can be only an integer")
        else:
            self.__health = value
