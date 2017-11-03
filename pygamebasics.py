"""Draw a circle in canvas using Pygame module."""

import os
import math
import pygame
from pygame.locals import *
from collections import Counter
if not pygame.font: print('Warning, fonts disabled')
if not pygame.mixer: print('Warning, sound disabled')

pygame.init()

canvas = pygame.display.set_mode((640, 100))
pygame.display.set_caption('Drawing')

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

ball_pos = (50, 50)
ball_color = BLUE
ball_sack = []
BALL_RADIUS = 20


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


def distance(a, b):
    return math.sqrt((a[1] - b[1]) ** 2 + (a[0] - b[0]) ** 2)


def click_handler(pos):
    global ball_pos, BALL_RADIUS, ball_sack
    changed = False
    remove = []

    for ball in ball_sack:
        if distance(ball[1], pos) < BALL_RADIUS:
            if ball[0] == BLUE:
                ball[0] = GREEN
            else:
                remove.append(ball)
            changed = True

    if not changed:
        ball_sack.append([ball_color, pos])
    else:
        ball_sack.extend(remove)
        ball_sack = [ball for ball in ball_sack if ball not in remove]

    print(len(ball_sack))


def draw_handler(canvas):
    canvas.fill(WHITE)

    for ball in ball_sack:
        pygame.draw.circle(canvas, ball[0], ball[1], BALL_RADIUS)

    pygame.display.update()


def main():
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
