from engine import *
import os

SCREEN_WIDTH = 1080
SCREEN_HEIGHT = 720
BGCOLOR = black

engine_screen = Screen(SCREEN_HEIGHT, SCREEN_WIDTH, BGCOLOR)

def setup(screen: Screen):
    screen.draw_axes()

    a = 0.1
    b = 9

    Weistrass = I * 0
    for n in range(10):
        Weistrass += Cos[X * (b ** n * pi)] * (a ** n)
    
    screen.split_regions(Weistrass, colors = [red, violet, blue], zoom = 150)

setup(engine_screen)
path = os.path.join("examples", "example2.png")
engine_screen.save(path)
