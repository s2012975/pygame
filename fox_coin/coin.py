from random import randint

width = 400
height = 400
score = 0
game_over = False

fox = Actor("fox")
fox.pos = 100, 100

banana = Actor("banana")
banana.pos = 200, 200


def draw():
    screen.fill("green")
    fox.draw()
    banana.draw()
    screen


def place():
    apple.x = randint(100, 700)
    apple.y = randint(100, 500)
    banana.x = randint(100, 700)
    banana.y = randint(100, 500)


def on_mouse_down(pos):
    if apple.collidepoint(pos):
        print("Good shot!")
        place()
    elif banana.collidepoint(pos):
        print("This is a banana")
        place()
    else:
        print("You missed!")
        place()


place()
