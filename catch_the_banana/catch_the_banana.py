import random

FONT_COLOUR = (255, 255, 255)
WIDTH = 800
HEIGHT = 600
# centreは英式のcenter
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
    # len()はlengthのこと。配列の中に要素がない。
    if len(fruits) == 0:
        fruits = make_fruits(current_level)


def make_fruits(number_of_extra_fruits):
    items_to_create = get_items_to_create(number_of_extra_fruits)
    new_fruits = create_fruits(items_to_create)
    layout_fruits(new_fruits)
    animate_fruits(new_fruits)
    return new_fruits


def get_items_to_create(number_of_extra_fruits):
    items_to_create = ["banana"]
    for i in range(0, number_of_extra_fruits):
        random_item = random.choice(ITEMS)
        items_to_create.append(random_item)
    return items_to_create


def create_fruits(items_to_create):
    new_fruits = []
    for item in items_to_create:
        fruit = Actor(item)
        new_fruits.append(fruit)
    return new_fruits


def layout_fruits(fruits_to_layout):
    pass


def animate_fruits(fruits_to_animate):
    pass