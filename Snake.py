from Variable import *
from apple import Apple


class Snake:
    # define the initials
    def __init__(self):
        self.body = []
        self.length = 0
        self.tail = []
        self.add_body(4, 4)
        self.add_body(3, 4)
        self.add_body(2, 4)
        self.score = 0

    # add snake body
    def add_body(self, row, column):
        self.body.append([row, column])
        self.length += 1
        self.tail = self.body[-1]

    def update(self, direction):
        # determine wheather snake is died or not
        if self.defeat(direction):
            return True

        self.tail = [self.body[-1][0], self.body[-1][1]]

        # snake moving
        try:
            for i in range(self.length - 1, 0, -1):
                self.body[i][0] = self.body[i - 1][0]
                self.body[i][1] = self.body[i - 1][1]
        except ValueError:
            return

        # change snake's direction
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
        # snake died if eat itself
        if self.body[0] in self.body[1:]:
            return True

        # snake died if go out of boundary
        elif direction == UP and self.body[0][0] >= COLUMN_COUNT - 1:
            return True
        elif direction == DOWN and self.body[0][0] <= 0:
            return True
        elif direction == RIGHT and self.body[0][1] >= ROW_COUNT - 1:
            return True
        elif direction == LEFT and self.body[0][1] <= 0:
            return True

        return False

    # if snake eat an apple, increase its body length by 1 grid
    def eat_apple(self, apple):
        if self.body[0] == [apple.x, apple.y]:
            self.length += 1
            self.body.append(self.tail)
            self.score += apple.score

            apple.produce(self)
