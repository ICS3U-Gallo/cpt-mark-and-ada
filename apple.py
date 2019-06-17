import random
from Variable import *


class Apple:
    # define the initials
    def __init__(self):
        self.x = 0
        self.y = 0
        self.score = 1
        # self.time = 0
        self.luck = 0

    # define the APPLE produce function
    def produce(self, snake):
        self.x = random.randint(0, ROW_COUNT - 1)
        self.y = random.randint(0, COLUMN_COUNT - 1)

        # if apple produce inside snake body, reproduce another one
        while [self.x, self.y] in snake.body:
            self.x = random.randint(0, ROW_COUNT - 1)
            self.y = random.randint(0, COLUMN_COUNT - 1)

        # 1/10 oppurtunity to produce a golden apple (5 scores)
        self.luck = random.randint(0, 9)
        if self.luck == 9:
            self.score = 5
        else:
            self.score = 1
