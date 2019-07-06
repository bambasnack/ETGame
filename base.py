import sys
import random
import pygame as pg
from box import *

# def get_box(x, y, width, height, color, border_width=-1, border_color=(0, 0, 0)):
#     surface = pg.Surface((width, height))
#     surface.fill(color)
#     pg.draw.rect(surface, border_color, pg.Rect(0, 0, width, height), border_width)
#     rect = surface.get_rect(topleft=(x, y))
#     return (surface, rect)

def blit_all(surface, to_blit):
    for item in to_blit:
        surface.blit(item[0], item[1])

def run():
    #basic game variables
    playing = True
    game_width = 500
    game_height = 400
    visible = []

    #set up pygame stuff
    pg.init()
    pg.font.init()
    dimensions = (game_width, game_height)
    screen = pg.display.set_mode(dimensions)
    bg_color = (100, 0, 100)

    #play music
    pg.mixer.music.load('temp.wav')
    pg.mixer.music.set_volume(0.5)
    pg.mixer.music.play(-1)

    #player surface and variables
    player = Box(100, 100, 50, 50, (0, 255, 0))
    visible.append(player.get_box())
    #enemy surface and variables
    enemy = Box(400, 100, 50, 50, (255, 0, 0))
    visible.append(enemy.get_box())
    #menu box
    # menu = get_box(10, game_height-110, game_width-20, 100, (255, 255, 255), 20, (0, 0, 0))
    # visible.append(menu)

    while playing:
        screen.fill(bg_color)

        #handle events
        for event in pg.event.get():
            #quitting
            if event.type == pg.QUIT:
                playing = False
            #mouse input
            elif event.type == pg.MOUSEBUTTONDOWN:
                #change player color
                player.surface.fill((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
            # #keyboard input
            # elif event.type == pg.KEYDOWN:
            #     #start player motion
            #     if event.key == pg.K_w:
            #         move_up = True
            #     elif event.key == pg.K_s:
            #         move_down = True
            #     elif event.key == pg.K_a:
            #         move_left = True
            #     elif event.key == pg.K_d:
            #         move_right = True
            # elif event.type == pg.KEYUP:
            #     #stop player motion
            #     if event.key == pg.K_w:
            #         move_up = False
            #     elif event.key == pg.K_s:
            #         move_down = False
            #     elif event.key == pg.K_a:
            #         move_left = False
            #     elif event.key == pg.K_d:
            #         move_right = False

        menu = Box(10, game_height-110, game_width-20, 100, (255, 255, 255), 10, (100, 200, 100))
        visible.append(menu.get_box())

        blit_all(screen, visible)

        pg.display.flip()
    pg.quit()
    sys.exit()


run()
