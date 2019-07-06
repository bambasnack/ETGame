import sys
import random
import pygame as pg

def run():
    #set up pygame stuff
    pg.init()
    pg.font.init()
    dimensions = (500, 400)
    screen = pg.display.set_mode(dimensions)
    bg_color = (100, 0, 100)

    #play music
    pg.mixer.music.load('temp.wav')
    pg.mixer.music.set_volume(0.5)
    pg.mixer.music.play(-1)


    #basic game variables
    playing = True

    #player surface and variables
    player_position = (100, 50)
    player_surface = pg.Surface((50, 50))
    player_surface.fill((0, 255, 0))
    player_rect = player_surface.get_rect(topleft = player_position)
    #player motion
    player_speed = 2
    move_right = False
    move_left = False
    move_up = False
    move_down = False

    while playing:
        screen.fill(bg_color)

        #handle events
        for event in pg.event.get():
            #quitting
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            #mouse input
            elif event.type == pg.MOUSEBUTTONDOWN:
                #change player color
                player_surface.fill((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
            #keyboard input
            elif event.type == pg.KEYDOWN:
                #start player motion
                if event.key == pg.K_w:
                    move_up = True
                elif event.key == pg.K_s:
                    move_down = True
                elif event.key == pg.K_a:
                    move_left = True
                elif event.key == pg.K_d:
                    move_right = True
            elif event.type == pg.KEYUP:
                #stop player motion
                if event.key == pg.K_w:
                    move_up = False
                elif event.key == pg.K_s:
                    move_down = False
                elif event.key == pg.K_a:
                    move_left = False
                elif event.key == pg.K_d:
                    move_right = False

        #move the player
        player_position = (player_position[0]+player_speed*(move_right-move_left), player_position[1]+player_speed*(move_down-move_up))
        player_rect.topleft = player_position
        screen.blit(player_surface, player_rect)

        pg.display.flip()


run()
