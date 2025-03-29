from mammal import Mammal

class Puma(Mammal):
    def __init__(self, age,tick):
        super().__init__(age)

        self.tick = tick