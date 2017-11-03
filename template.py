""""""

import os
import math
import pygame
from pygame.locals import *
from collections import Counter
if not pygame.font: print('Warning, fonts disabled')
if not pygame.mixer: print('Warning, sound disabled')

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

WIDTH = 640
HEIGHT = 400


def load_image(name, colorkey=None):
    fullname = os.path.join('data\images', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error as message:
        print('Cannot load image:', name)
        raise SystemExit(message)
    if colorkey is not None:
        image = image.convert()
        if colorkey is -1:
            colorkey = image.get_at((0,0))
        image.set_colorkey(colorkey, RLEACCEL)
    else:
        image = image.convert_alpha()
    return image, image.get_rect()


def load_sound(name):
    class NoneSound:
        def play(self): pass
    if not pygame.mixer:
        return NoneSound()
    fullname = os.path.join('data\sounds', name)
    try:
        sound = pygame.mixer.Sound(fullname)
    except pygame.error as message:
        print('Cannot load sound:', name)
        raise SystemExit(message)
    return sound


def click_handler(pos):
    print(pos)


def draw_handler(canvas):
    canvas.fill(WHITE)

    pygame.display.update()


def main():
    pygame.init()

    canvas = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('')

    running = True
    clock = pygame.time.Clock()

    # ---------------------------Frame is now Running-----------------------------------------
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                click_handler(pygame.mouse.get_pos())

        draw_handler(canvas)
        clock.tick(60)
    # -----------------------------Frame Stops------------------------------------------

    pygame.quit()

if __name__ == '__main__':
    main()
