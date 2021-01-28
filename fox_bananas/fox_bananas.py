from random import randint

apple = Actor("apple")
banana = Actor("banana")


def draw():
    screen.clear()
    apple.draw()
    banana.draw()


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
