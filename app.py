from    engine import *
import  pygame, sys

SCREEN_WIDTH = 1080
SCREEN_HEIGHT = 720
BGCOLOR = black

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    engine_screen = Screen(SCREEN_HEIGHT, SCREEN_WIDTH, BGCOLOR)

    pygame.display.set_caption("Eanorambuena Mathematica")

    engine_screen.draw_axes()
    engine_screen.plot(sin, 0, 0, red)
    engine_screen.plot(sin, 0, 0, green, 40)

    engine_screen.save()

    bg = pygame.image.load("img.png").convert()
    screen.blit(bg, (0, 0))
    pygame.display.flip()

    while True: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

main()
