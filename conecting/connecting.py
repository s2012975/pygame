from random import randint

width = 400
height = 400

bananas = []
lines = []

next_banana = 0

for banana in range(0, 10):
    actor = Actor("banana")
    actor.pos = randint(20, width - 20), randint(20, height - 20)
    bananas.append(actor)


def draw():
    screen.fill("gray")
    number = 1
    for banana in bananas:
        screen.draw.text(str(number), (banana.pos[0], banana.pos[1] + 12))
        banana.draw()
        number = number + 1
    for line in lines:
        screen.draw.line(line[0], line[1], (100, 0, 0))


def on_mouse_down(pos):
    global next_banana
    global lines
    if bananas[next_banana].collidepoint(pos):
        if next_banana:
            lines.append((bananas[next_banana - 1].pos, bananas[next_banana].pos))
        next_banana += 1
    else:
        lines = []
        next_banana = 0
