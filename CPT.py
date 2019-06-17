import arcade
from Snake import Snake
from Variable import *
import time
from apple import Apple


# Do the math to figure out oiur screen dimensions
SCREEN_WIDTH = (WIDTH + MARGIN) * COLUMN_COUNT + MARGIN
SCREEN_HEIGHT = (HEIGHT + MARGIN) * ROW_COUNT + MARGIN

TITLE = "Snake"


class MyGame(arcade.Window):
    # define the initials
    def __init__(self, width, height, title):
        super().__init__(width, height, title, update_rate=10)

        # add snake
        self.snake = Snake()
        self.direction = UP
        self.grid = []
        self.defeat = False
        self.state = 0  # 1 instruction  0 menu 2 game 3 defeat
        # add apple
        self.apple = Apple()
        self.apple.produce(self.snake)

        for row in range(ROW_COUNT):
            # Add an empty array that will hold each cell
            # in this row
            self.grid.append([])
            for column in range(COLUMN_COUNT):
                self.grid[row].append(0)  # Append a cell

        self.add_snake_to_grid()

    def add_snake_to_grid(self):
        # add a cell for each block
        for i in range(ROW_COUNT):
            for j in range(COLUMN_COUNT):
                self.grid[i][j] = 0

        for i in range(1, self.snake.length):
            row = self.snake.body[i][0]
            col = self.snake.body[i][1]
            self.grid[row][col] = SNAKE

        # give a value to a block represent different types of apple
        if self.apple.score == 1:
            apple_x = self.apple.x
            apple_y = self.apple.y
            self.grid[apple_x][apple_y] = APPLE
        elif self.apple.score == 5:
            apple_x = self.apple.x
            apple_y = self.apple.y
            self.grid[apple_x][apple_y] = APPLE5

        # define the first snake body is snake head
        head = self.snake.body[0]
        self.grid[head[0]][head[1]] = S_HEAD

    def draw_menu(self):
        # button_i for instruction, button_s for start
        xi, yi, wi, hi = button_i
        xs, ys, ws, hs = button_s

        arcade.start_render()
        arcade.set_background_color(arcade.color.VANILLA)
        # display buttons and texts
        arcade.draw_text("Snakes", width/4 + 40, height/4*3, arcade.color.BLACK, font_size=50)
        arcade.draw_xywh_rectangle_filled(xi, yi, wi, hi, arcade.color.WHITE_SMOKE)
        arcade.draw_xywh_rectangle_filled(xs, ys, ws, hs, arcade.color.WHITE_SMOKE)

        arcade.draw_text("* Instructions", width / 4 + 30, height / 2 - 80,
                         arcade.color.BLACK, font_size=35)
        arcade.draw_text("* Start", width / 4 + 30, height / 2 + 50,
                         arcade.color.BLACK, font_size=35,)

    def on_mouse_press(self, x, y, button, modifiers):
        # if click the buttons, change the state
        if self.state == 0:
            i_x, i_y, i_w, i_h = button_i
            s_x, s_y, s_w, s_h = button_s
            if x > i_x and x < i_x + i_w and y > i_y and y < i_y + i_h:
                self.state = 1
                self.snake.body = []
                self.draw_game()
            elif x > s_x and x < s_x + s_w and y > s_y and y < s_y + s_h:
                self.state = 2
        elif self.state == 1:
            b_x, b_y, b_w, b_h = button_b
            if x > b_x and x < b_x + b_w and y > b_y and y < b_y + b_h:
                # start a new game
                self.setup()
        elif self.state == 3:
            b2_x, b2_y, b2_w, b2_h = button_b2
            if x > b2_x and x < b2_x + b2_w and y > b2_y and y < b2_y + b2_h:
                # start a new game
                self.setup()

    # setup function reset all values to origin
    def setup(self):
        self.state = 0
        self.snake.body = []
        self.snake.direction = UP
        self.snake.length = 0
        self.snake.tail = []
        self.snake.add_body(4, 4)
        self.snake.score = 0
        self.snake.add_body(3, 4)
        self.snake.add_body(2, 4)
        self.angle = (self.direction - 10) * 90
        self.direction = UP

    def draw_instruction(self):
        # draw instruction interface
        arcade.draw_rectangle_filled(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, SCREEN_WIDTH, SCREEN_HEIGHT,
                                     arcade.color.ROSE_GOLD)
        arcade.draw_text("Instructions", width/2 - 95, 600,
                         arcade.color.BLUE_GRAY, font_size=35)
        arcade.draw_text("""
                              - The player as a snake in this game,
                                the player can use the keyboard
                                (up, down, right, left) to control the snake.
                              - The goal for the player is to eat as
                                many apples as they can.
                              - Only one apple is available for the player
                                 at each time.
                              - There will be random golden apple available
                                for the player to eat,
                                they can get five bonus if they successfully eat it,
                                the golden apple will disappear if the player
                                didn't eat it for a while.
                              - The head of the snake cannot touch its body,
                                or any places out to the grid.
                                If they do so, they will lose.
                              - Do not choose the direction which opposite with
                                the direction that the snake is moving on.
                                """,
                         5, height / 4,
                         arcade.color.BLACK, font_size=18)

        xb, yb, wb, hb = button_b
        arcade.draw_xywh_rectangle_filled(xb, yb, wb, hb, arcade.color.WHITE_SMOKE)
        arcade.draw_text("* Back", xb, yb,
                         arcade.color.ROSE_GOLD, font_size=20)

    def draw_defeat(self):
        # draw defeat interface
        arcade.draw_rectangle_filled(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, SCREEN_WIDTH, SCREEN_HEIGHT,
                                     arcade.color.RED)
        arcade.draw_text("YOU LOSE", SCREEN_WIDTH/2 - 70, SCREEN_HEIGHT/2,
                         arcade.color.WHITE_SMOKE, font_size=35)
        # display your scores
        arcade.draw_text(f"Score: {str(self.snake.score)}", SCREEN_WIDTH/2 - 50, SCREEN_HEIGHT/2 - 50,
                         arcade.color.BLACK, font_size=35)

        xb2, yb2, wb2, hb2 = button_b2
        arcade.draw_xywh_rectangle_filled(xb2, yb2, wb2, hb2, arcade.color.WHITE_SMOKE)
        arcade.draw_text("* Back", xb2, yb2,
                         arcade.color.ROSE_GOLD, font_size=20)

    def draw_game(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        arcade.start_render()
        # Draw the grid
        if self.defeat:
            arcade.set_background_color(arcade.color.ALLOY_ORANGE)
            arcade.draw_text("LOSE", 50, 50, arcade.color.BLACK)

        for row in range(ROW_COUNT):
            for column in range(COLUMN_COUNT):
                # Figure out what color to draw the box
                if self.grid[row][column] != SNAKE:
                    color = arcade.color.ARYLIDE_YELLOW

                # Do the math to figure out where the box is
                x = (MARGIN + WIDTH) * column + MARGIN + WIDTH // 2
                y = (MARGIN + HEIGHT) * row + MARGIN + HEIGHT // 2

                # Draw the box
                arcade.draw_rectangle_filled(x, y, WIDTH, HEIGHT, color)

                # Draw sprite
                if self.grid[row][column] == S_HEAD:
                    angle = (self.direction - 10) * 90
                    snake_head.draw(x, y, WIDTH, HEIGHT, angle=angle)
                elif self.grid[row][column] == APPLE:
                    red_apple.draw(x, y, WIDTH, HEIGHT)
                elif self.grid[row][column] == APPLE5:
                    golden_apple.draw(x, y, WIDTH, HEIGHT)
                elif self.grid[row][column] == SNAKE:
                    snake_body.draw(x, y, WIDTH, HEIGHT)

    def on_draw(self):
        # draw different interfaces
        if self.state == 0:
            self.draw_menu()
        elif self.state == 2:
            self.draw_game()
        elif self.state == 1:
            self.draw_instruction()
        elif self.state == 3:
            self.draw_defeat()

    def update(self, delta_time: float):
        # update all functions
        if self.state != 2:
            return

        if self.snake.update(self.direction):
            self.state = 3

        self.snake.eat_apple(self.apple)

        self.add_snake_to_grid()

    def on_key_press(self, key: int, modifiers: int):
        # use keyboard to control directions
        if key == arcade.key.UP:
            self.direction = UP
        elif key == arcade.key.DOWN:
            self.direction = DOWN
        elif key == arcade.key.LEFT:
            self.direction = LEFT
        elif key == arcade.key.RIGHT:
            self.direction = RIGHT


def main():
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, TITLE)
    arcade.run()


if __name__ == "__main__":
    main()
