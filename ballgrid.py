""""""

import os
import math
import pygame
from pygame.locals import *
from collections import Counter
if not pygame.font: print('Warning, fonts disabled')
if not pygame.mixer: print('Warning, sound disabled')

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

BALL_RADIUS = 20

WIDTH = 400
HEIGHT = 600

canvas = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('')


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
    cols = (WIDTH//(BALL_RADIUS*2))
    rows = (HEIGHT//(BALL_RADIUS*2))

    for c in range(cols):
        for r in range(rows):
            pygame.draw.circle(canvas, BLACK, (BALL_RADIUS+(BALL_RADIUS*2*c),
                                               BALL_RADIUS+(BALL_RADIUS*2*r)),
                               BALL_RADIUS)

    pygame.display.update()


def main():
    running = True
    clock = pygame.time.Clock()

    # ---------------------------Frame is now Running-------------------------
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                click_handler(pygame.mouse.get_pos())

        draw_handler(canvas)
        clock.tick(60)
    # -----------------------------Frame Stops--------------------------------

    pygame.quit()

if __name__ == '__main__':
    main()
