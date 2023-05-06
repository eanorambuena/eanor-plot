from cliper import clip_images
from engine import Screen, Sin, red, black, X, I
import os

path = os.path.join("examples", "example4")
output_path = os.path.join("examples", "example4.mp4")

if not os.path.exists(path):
    os.makedirs(path)

SCREEN_WIDTH = 1080
SCREEN_HEIGHT = 720
BGCOLOR = black
FPS = 60
SECONDS = 10

engine_screen = Screen(SCREEN_HEIGHT, SCREEN_WIDTH, BGCOLOR)
velocity = 1.0

def loop(screen: Screen, index: int):
    screen.fill_room()
    screen.draw_axes()
    phase = index / float(FPS * velocity)
    F = Sin[X - I * phase]
    screen.plot(F, color=red, zoom=100) 

for i in range(SECONDS * FPS):
    loop(engine_screen, i)
    engine_screen.save(os.path.join(path, f"example4_{i}.png"))
    print(f"Saved frame {i}.")

clip_images(path, FPS, output_path)
