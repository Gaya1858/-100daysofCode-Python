import random

class RandomNumber:

    def __init__(self):
        self.rand_coin =random.randint(0,1)

    def get_coin(self):
        return self.rand_coin
