import random

FONT_COLOUR = (255, 255, 255)
WIDTH = 800
HEIGHT = 600
CENTRE_X = WIDTH / 2
CENTRE_Y = HEIGHT / 2
CENTRE = (CENTRE_X, CENTRE_Y)
FINAL_LEVEL = 6
START_SPEED = 10
ITEMS = ["apple", "orange"]

game_over = False
game_complete = False
current_level = 1
fruits = []
animations = []


def draw():
    global fruits, current_level, game_over, game_complete
    screen.clear()
    # screen.blit("space", (0, 0))
    if game_over:
        display_message("GAME OVER!", "Try again.")
    elif game_complete:
        display_message("YOU WON!", "Well done.")
    else:
        for fruit in fruits:
            fruit.draw()


def update():
    global fruits
    # len()はlengthのこと
    if len(fruits) == 0:
        fruits = make_fruits(current_level)


def make_fruits(number_of_extra_fruits):
    items_to_create = get_items_to_create(number_of_extra_fruits)
    new_fruits = create_fruits(items_to_create)
    layout_fruits(new_fruits)
    animate_fruits(new_fruits)
    return new_fruits


def get_items_to_create(number_of_extra_fruits):
    return []


def create_fruits(items_to_create):
    return []


def layout_fruits(fruits_to_layout):
    pass


def animate_fruits(fruits_to_animate):
    pass