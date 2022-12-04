from Classes.enemy import Enemy


class SuperBombardier(Enemy):
    def __init__(self, x, y, angle):
        super().__init__(x, y, angle)
        self.speed = 1
        self.width = 10
        self.height = 9
        self.gained_score = 200
        self.health = 4
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

# 4 shots will kill him, but on 3 shots we can do that he blinks to show that he is about to die.
