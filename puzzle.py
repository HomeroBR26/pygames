""""""

import os
import sys
import random
import pygame
from pygame.locals import *
if not pygame.font: print('Warning, fonts disabled')
if not pygame.mixer: print('Warning, sound disabled')


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

WINDOW_WIDTH = 640
WINDOW_HEIGHT = 400

BOARD_WIDTH = 4
BOARD_HEIGHT = 4
TILE_SIZE = 80

FPS = 30

BGCOLOR = (110, 0, 255)
TILE_COLOR = GREEN
TEXT_COLOR = WHITE
BORDER_COLOR = (110, 110, 255)
BASIC_FONTSIZE = 20
BUTTON_COLOR = WHITE
BUTTONTEXT_COLOR = BLACK
MESSAGE_COLOR = WHITE

X_MARGIN = int((WINDOW_WIDTH - (TILE_SIZE * BOARD_WIDTH + (BOARD_WIDTH - 1))) / 2)
Y_MARGIN = int((WINDOW_HEIGHT - (TILE_SIZE * BOARD_HEIGHT + (BOARD_HEIGHT - 1))) / 2)

UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'

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

    canvas = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
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
        clock.tick(FPS)
    # -----------------------------Frame Stops------------------------------------------

    pygame.quit()

if __name__ == '__main__':
    main()
