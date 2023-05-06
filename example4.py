from engine import render_animation, Screen, Sin, red, black, X, I
from os.path import join

PATH = join("examples", "example4")
OUTPUT_PATH = join("examples", "example4.mp4")
SCREEN_WIDTH = 1080
SCREEN_HEIGHT = 720
BGCOLOR = black
FPS = 24
SECONDS = 5
VELOCITY = 1.0

def loop(screen: Screen, delta_time: float):
    screen.fill_room()
    screen.draw_axes()
    phase = VELOCITY * delta_time
    F = Sin[X - I * phase]
    screen.plot(F, color=red, zoom=100) 

render_animation(loop, PATH, OUTPUT_PATH, FPS, SECONDS, SCREEN_HEIGHT, SCREEN_WIDTH, BGCOLOR)
