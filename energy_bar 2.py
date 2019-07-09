import sys
import random
import pygame as pg
import pygame
from box import *
import sys
import random
import pygame as pg
import pygame
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
    #live = True
    playing = True
    game_width = 500
    game_height = 400
    visible = []
    battle = False

    #set up pygame stuff
    pg.init()
    pg.font.init()
    dimensions = (game_width, game_height)
    screen = pg.display.set_mode(dimensions)
    bg_color = (100, 0, 100)

    #colors
    black = (0, 0, 0)
    white = (255,255,255)
    lighter_blue = (152, 245, 255)


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

    def text_objects(text, font):
        textSurface = font.render(text, True, black)
        return textSurface, textSurface.get_rect()

    #function for buttons
    def button(text, x, y, w, h, ic, ac, action=None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        # variables for energy
        player_energy = 50
        enemy_energy = 50
        #hover to change color
        if x + w > mouse[0] > x and y + h > mouse[1] > y:
            pygame.draw.rect(screen, ac, (x, y, w, h))

            #clicking doing something
            if click[0] == 1 and action != None:
                # player button attack
                if action == attack:
                    chance_attack = rand.int(range(1, 10))
                    if chance_attack % 2 == 0:
                        enemy_energy -= 10
                        return enemy_energy
                    else:
                        print("Your attack missed!")
                        return enemy_energy

                # player button refresh
                if action == refresh:
                    player_energy += 5
                    return player_energy

                # player button range attack
                if action == range_attack:
                    enemy_energy -= 5
                    return enemy_energy
        #hover to change color
        else:
            pygame.draw.rect(screen, ic, (x, y, w, h))

        #setting font
        font_use = pygame.font.SysFont("arial black", 20)
        textSurf, textRect = text_objects(text, font_use)
        textRect.center = ((x + (w / 2)), (y + (h / 2)))
        screen.blit(textSurf, textRect)

        #to start battle
        #if action == start_battle:
            #battle = True

    #menu box
    # menu = get_box(10, game_height-110, game_width-20, 100, (255, 255, 255), 20, (0, 0, 0))
    # visible.append(menu)
    while playing:
        screen.fill(bg_color)

        # player energy display
        pygame.draw.rect(screen, (0, 255, 0), (100, 80, player_energy, 10))
        pygame.draw.rect(screen, (75, 0, 130), (100, 80, 50, 10))

        # enemy energy display
        pygame.draw.rect(screen, (0, 255, 0), (100, 80, enemy_energy, 10))
        pygame.draw.rect(screen, (75, 0, 130), (400, 80, 50, 10))

        #button("Start Battle Now", 180, 300, 200, 50, white, lighter_blue)

        #while battle:
        #displayed buttons
        button("Attack", 50, 250, 180, 50, (255,255,255), (152, 245, 255), attack)
        button("Refresh", 270, 250, 180, 50, white, lighter_blue, refresh)
        button("Range Attack", 50, 400, 180, 50, white, lighter_blue, range_attack)

        #pygame.display.update()

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
