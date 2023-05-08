from engine import render_animation, Screen, Sin, blue, white, X as theta, clearConsole
from os.path import join
from timeit import default_timer as timer

PATH = join("examples", "example6")
OUTPUT_PATH = join("examples", "example6.mp4")
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
BGCOLOR = white
FPS = 10
SECONDS = 1
VELOCITY = 150.0

r = theta

def loop(screen: Screen, delta_time: float):
    phase = VELOCITY * delta_time
    zoom_velocity = 0.02
    zoom_phase = zoom_velocity * phase
    screen.fill_room()
    screen.draw_axes()
    screen.polar_plot(r, color=blue, zoom=140-int(zoom_phase), theta_range=range(int(phase)))

def loop_optimized(screen: Screen, delta_time: float):
    phase = VELOCITY * delta_time
    zoom_velocity = 0.02
    zoom_phase = zoom_velocity * phase
    # Instead of using screen.fill_room() we can revert the drawing operations, but using BGCOLOR as the color
    # This can be faster than screen.fill_room() because we are not drawing the background again
    screen.polar_plot(r, color=BGCOLOR, zoom=140-int(zoom_phase), theta_range=range(int(phase)))
    screen.draw_axes(color=BGCOLOR)
    # --------------------------------------------------------------------------------------------------------
    screen.draw_axes()
    screen.polar_plot(r, color=blue, zoom=140-int(zoom_phase), theta_range=range(int(phase)))

start = timer()
render_animation(loop, PATH, OUTPUT_PATH, FPS, SECONDS, SCREEN_HEIGHT, SCREEN_WIDTH, BGCOLOR)
end = timer()
start_optimized = timer()
render_animation(loop_optimized, PATH, OUTPUT_PATH, FPS, SECONDS, SCREEN_HEIGHT, SCREEN_WIDTH, BGCOLOR)
end_optimized = timer()
clearConsole()
print(f"Time elapsed: {end - start} seconds")
print(f"Time elapsed (optimized): {end_optimized - start_optimized} seconds")
print(f"Time saved: {((end - start) - (end_optimized - start_optimized)) / (end - start) * 100}%")
