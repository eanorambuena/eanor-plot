from engine import render_animation, Screen, Sin, blue, white, X as theta
from os.path import join

PATH = join("examples", "example5")
OUTPUT_PATH = join("examples", "example5.mp4")
SCREEN_WIDTH = 1080
SCREEN_HEIGHT = 720
BGCOLOR = white
FPS = 24
SECONDS = 15
VELOCITY = 150.0

r = theta

def loop(screen: Screen, delta_time: float):
    screen.fill_room()
    screen.draw_axes()
    phase = VELOCITY * delta_time
    screen.polar_plot(r, color=blue, zoom=150, theta_range=range(int(phase)))

render_animation(loop, PATH, OUTPUT_PATH, FPS, SECONDS, SCREEN_HEIGHT, SCREEN_WIDTH, BGCOLOR)
