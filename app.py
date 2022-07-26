from    engine import *
import  pygame, sys

def load2screen(screen = pygame.Surface, file_name = "result.png"):
    bg = pygame.image.load(file_name).convert()
    screen.blit(bg, (0, 0))
    pygame.display.flip()

SCREEN_WIDTH = 1080
SCREEN_HEIGHT = 720
BGCOLOR = black

def main():
    pygame.init()
    pygame_screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    engine_screen = Screen(SCREEN_HEIGHT, SCREEN_WIDTH, BGCOLOR)

    pygame.display.set_caption("Eanorambuena Mathematica")

    def setup(screen):
        screen.draw_axes()
        screen.plot(Sin, 0, 0, red)
        screen.plot(Sin, 0, 0, green, 40)
        for i in range(0, 1000,3):
            screen.plot(Sin * 0.7 + Sin[X * 0.5 - 1] + Cos[X * 0.2] * 3 - i, 0, 0, blue, 40)

    def loop(screen):
        screen.draw_axes()
        screen.plot(Sin, 0, 0, red)
        screen.plot(sin, 0, 0, green, 40)

    setup(engine_screen)
    engine_screen.save()
    load2screen(pygame_screen)

    while True: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()
                elif event.key == pygame.K_r:
                    if engine_screen.bgcolor == black:
                        engine_screen.bgcolor = white
                    else:
                        engine_screen.bgcolor = black
                    engine_screen.fill_room()
                    loop(engine_screen)
                    engine_screen.save()
                    load2screen(pygame_screen)

main()
