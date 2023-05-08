from engine import render_animation, Screen, Sin, blue, white, X as theta
from os.path import join

PATH = join("examples", "example5")
OUTPUT_PATH = join("examples", "example5.mp4")
SCREEN_WIDTH = 1080
SCREEN_HEIGHT = 720
BGCOLOR = white
FPS = 60
SECONDS = 20
VELOCITY = 150.0

r = theta

def loop(screen: Screen, delta_time: float):
    phase = VELOCITY * delta_time
    zoom_velocity = 0.02
    zoom_phase = zoom_velocity * phase
    screen.fill_room()
    screen.draw_axes()
    screen.polar_plot(r, color=blue, zoom=140-int(zoom_phase), theta_range=range(int(phase)))

render_animation(loop, PATH, OUTPUT_PATH, FPS, SECONDS, SCREEN_HEIGHT, SCREEN_WIDTH, BGCOLOR)
