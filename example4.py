from engine import render_animation, Screen, Sin, red, black, X, I
import os

PATH = os.path.join("examples", "example4")
OUTPUT_PATH = os.path.join("examples", "example4.mp4")
SCREEN_WIDTH = 1080
SCREEN_HEIGHT = 720
BGCOLOR = black
FPS = 30
SECONDS = 5
VELOCITY = 1.0

def loop(screen: Screen, delta_time: float):
    screen.fill_room()
    screen.draw_axes()
    phase = VELOCITY * delta_time
    F = Sin[X - I * phase]
    screen.plot(F, color=red, zoom=100) 

render_animation(loop, PATH, OUTPUT_PATH, FPS, SECONDS, SCREEN_HEIGHT, SCREEN_WIDTH, BGCOLOR)
