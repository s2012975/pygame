#普通の Python プログラムとして実行する方法
import pgzrun
def draw():
    name = "martin"
    screen.draw.text("Hello", topleft=(10, 10))
    screen.draw.text(name, topleft=(20, 20))
pgzrun.go()
