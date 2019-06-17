import arcade

ROW_COUNT = 28
COLUMN_COUNT = 28

# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 25
HEIGHT = 25

# This sets the margin between each cell
# and on the edges of the screen.
MARGIN = 0.7

# Define the variable used
SNAKE = 2
APPLE = 3
APPLE5 = 1
S_HEAD = 4


# Define the variable used
SNAKE = 2

UP = 10
DOWN = 12
LEFT = 11
RIGHT = 13

# Do the math to figure out oiur screen dimensions
SCREEN_WIDTH = (WIDTH + MARGIN) * COLUMN_COUNT + MARGIN
SCREEN_HEIGHT = (HEIGHT + MARGIN) * ROW_COUNT + MARGIN

TITLE = "Snake"

# buttons variables
width = 700
height = 700
button_i = [width / 4 + 15, height / 2 - 90, 340, 60]
button_s = [width / 4 + 15, height / 2 + 40, 340, 60]
button_b = [width / 3 * 2, height / 5, 100, 30]
button_b2 = [width / 3 * 2, height / 5, 100, 30]
buttons = [button_i, button_s]

# load image
snake_head = arcade.load_texture("./snake_head.png")
snake_body = arcade.load_texture("./snake_body.png")
red_apple = arcade.load_texture("./red_apple.png")
golden_apple = arcade.load_texture("./golden_apple.png")
