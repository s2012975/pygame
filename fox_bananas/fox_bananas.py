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
    screen.fill("brown")
    fox.draw()
    banana.draw()
    screen.draw.text("Score: " + str(score), color="black", topleft=(10, 10))

    if game_over:
        screen.fill("pink")
        screen.draw.text("Fimal Score: " + str(score), topleft=(10, 10), fontsize=60)


def place_banana():
    banana.x = randint(20, (width - 20))
    banana.y = randint(20, (height - 20))


def time_up():
    global game_over
    game_over = True


def update():
    global score

    if (keyboard.left) and (keyboard.up):
        fox.x = fox.x - 4
        fox.y = fox.y - 4
    elif (keyboard.right) and (keyboard.up):
        fox.x = fox.x + 4
        fox.y = fox.y - 4
    elif (keyboard.left) and (keyboard.down):
        fox.x = fox.x - 4
        fox.y = fox.y + 4
    elif (keyboard.right) and (keyboard.down):
        fox.x = fox.x + 4
        fox.y = fox.y + 4
    elif keyboard.left:
        fox.x = fox.x - 4
    elif keyboard.right:
        fox.x = fox.x + 4
    elif keyboard.up:
        fox.y = fox.y - 4
    elif keyboard.down:
        fox.y = fox.y + 4

    banana_collected = fox.colliderect(banana)

    if banana_collected:
        score = score + 10
        place_banana()


clock.schedule(time_up, 7.0)
place_banana()


# under lines are no relation this game

# def place():
#     apple.x = randint(100, 700)
#     apple.y = randint(100, 500)
#     banana.x = randint(100, 700)
#     banana.y = randint(100, 500)


# def on_mouse_down(pos):
#     if apple.collidepoint(pos):
#         print("Good shot!")
#         place()
#     elif banana.collidepoint(pos):
#         print("This is a banana")
#         place()
#     else:
#         print("You missed!")
#         place()