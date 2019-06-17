from Variable import *
from apple import Apple


class Snake:
    def __init__(self):

        self.body = []
        self.length = 0
        self.tail = []
        self.add_body(4, 4)
        self.score = 0
        self.add_body(3, 4)
        self.add_body(2, 4)

    def add_body(self, row, column):
        self.body.append([row, column])
        self.length += 1
        self.tail = self.body[-1]

    def update(self, direction):

        if self.defeat(direction):
            return True

        self.tail = [self.body[-1][0], self.body[-1][1]]

        for i in range(self.length - 1, 0, -1):
            self.body[i][0] = self.body[i - 1][0]
            self.body[i][1] = self.body[i - 1][1]

        if direction == UP:
            self.body[0][0] += 1
        elif direction == DOWN:
            self.body[0][0] -= 1
        elif direction == LEFT:
            self.body[0][1] -= 1
        elif direction == RIGHT:
            self.body[0][1] += 1

        return False

    def defeat(self, direction):
        if self.body[0] in self.body[1:]:
            return True
        elif direction == UP and self.body[0][0] >= COLUMN_COUNT - 1:
            return True
        elif direction == DOWN and self.body[0][0] <= 0:
            return True
        elif direction == RIGHT and self.body[0][1] >= ROW_COUNT - 1:
            return True
        elif direction == LEFT and self.body[0][1] <= 0:
            return True

        return False

    def eat_apple(self, apple):
        if self.body[0] == [apple.x, apple.y]:
            self.length += 1
            self.body.append(self.tail)
            self.score += apple.score

            apple.prodece(self)