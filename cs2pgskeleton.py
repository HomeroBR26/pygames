# skeleton.py file to use as a template when porting CodeSkulptor
# projects over to PyGame.  It should provide the basic structure
# to allow moving your code into PyGame.  It will not make your
# code work automatically, but does provide the *new* pieces of code
# that are required to make your Codeskulptor projects run in
# PyGame.  You then need to replace calls to simplegui functions
# with their equivalent functions in PyGame.  Good Luck!
#
# As it is setup it will run a simple text animation illustrating
# the draw handler and timers.
#
# Kevin B.


# import modules
import os
import pygame

# pygame specific locals/constants
from pygame.locals import *

# some resource related warnings
if not pygame.font: print('Warning, fonts disabled')
if not pygame.mixer: print('Warning, sound disabled')

# initializations
pygame.init()

# a bit similar to CodeSkulptor frame creation -- we'll call the window the canvas
canvas = pygame.display.set_mode((640, 480))
pygame.display.set_caption("My_Project")


# Pygame Wrapper functions -- resource loading sanity checks
# Taken from the "Monkey tutorial" and updated for 3.3 by me
#
# load Image:
# A colorkey is used in graphics to represent a color of the image
# that is transparent (r, g, b). -1 = top left pixel colour is used.
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
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey, RLEACCEL)
    else:
        image = image.convert_alpha()
    return image, image.get_rect()


# Load Sound
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


# need to create fonts and colour objects in PyGame
# fontObj = pygame.font.Font('ARBERKLEY.ttf', 32)
# fontObj2 = pygame.font.Font('ARBERKLEY.ttf', 24)
fontObj3 = pygame.font.Font(pygame.font.match_font('timesnewroman'), 32)

gold_color = pygame.Color(255, 215, 0)
white_color = pygame.Color(255, 255, 255)

# ------------------------Begin Your CodeSkulptor Port-------------------------




























count = 0
draw_colour = white_color


def draw_handler(canvas):
    # clear canvas -- fill canvas with uniform colour, then draw everything below.
    # this removes everything previously drawn and refreshes
    canvas.fill((0, 0, 0))

    # draw example
    global count
    count += 1

    text_draw = fontObj3.render("CodeSkulptor Port", True, draw_colour)
    text_draw2 = fontObj3.render("Tutorial", True, draw_colour)

    if count % 90 < 45:
        canvas.blit(text_draw, (190, 220))
    else:
        canvas.blit(text_draw2, (250, 220))

    # update the display
    pygame.display.update()


def t_example():
    global draw_colour
    if draw_colour == white_color:
        draw_colour = gold_color
    else:
        draw_colour = white_color


# pygame has no start() and stop() methods -- 0 time is off any other value is on
# set some on/off constants for readability with each timer
TIMER_OFF = 0

# timer for example -- 1500 milliseconds when on
TIMER_EXAMPLE_ON = 1500
# set the timer name to its user event for readability
timer_example = USEREVENT + 1
pygame.time.set_timer(timer_example, TIMER_EXAMPLE_ON)


# call this function to start everything
# could be thought of as the implemntation of the CodeSkulptor frame .start() method.
def main():
    # initialize loop until quit variable
    running = True

    # create our FPS timer clock
    clock = pygame.time.Clock()

    # ---------------------------Frame is now Running-----------------------------------------

    # doing the infinte loop until quit -- the game is running
    while running:

        # event queue iteration
        for event in pygame.event.get():

            # window GUI ('x' the window)
            if event.type == pygame.QUIT:
                running = False

            # input - key and mouse event handlers
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pass
                # just respond to left mouse clicks
                # if pygame.mouse.get_pressed()[0]:
                # mc_handler(pygame.mouse.get_pos())
            elif event.type == pygame.KEYDOWN:
                pass
                # kd_handler(event.key)

            # timers
            elif event.type == timer_example:
                t_example()

        # the call to the draw handler
        draw_handler(canvas)

        # FPS limit to 60 -- essentially, setting the draw handler timing
        # it micro pauses so while loop only runs 60 times a second max.
        clock.tick(60)

    # -----------------------------Frame Stops------------------------------------------

    # quit game -- we're now allowed to hit the quit call
    pygame.quit()


# this calls the 'main' function when this script is executed
# could be thought of as a call to frame.start() of sorts
if __name__ == '__main__':
    main()
