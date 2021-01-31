from random import randint

width = 400
height = 400

bananas = []
lines = []

next_dot = 0

for banana in range(0, 10):
    actor = Actor("banana")
    actor.pos = randint(20, width - 20), randint(20, height - 20)
    bananas.append(actor)


def draw():
    screen.fill("black")
    number = 1
    for banana in bananas:
        screen.draw.text(str(number), (banana.pos[0], banana.pos[1] + 12))
        banana.draw()
        number = number + 1
