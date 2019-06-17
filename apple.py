import random
from Variable import *


class Apple:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.score = 1
        # self.time = 0
        self.luck = 0

    def prodece(self, snake):
        self.x = random.randint(0, ROW_COUNT - 1)
        self.y = random.randint(0, COLUMN_COUNT - 1)

        while [self.x, self.y] in snake.body:
            self.x = random.randint(0, ROW_COUNT - 1)
            self.y = random.randint(0, COLUMN_COUNT - 1)

        self.luck = random.randint(0, 3)
        if self.luck == 2:
            self.score = 5
            self.time = 7
        else:
            self.score = 1

    # def update(self):
    #      if self.time > 0:
    #          self.time -= 1
    #      elif self.time == 0:
    #          self.score = 1
