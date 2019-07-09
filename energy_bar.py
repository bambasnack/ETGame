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
    pygame.display.update()
    while playing:
        screen.fill(bg_color)

        # variables for energy
        player_energy = 50
        enemy_energy = 50

        # player energy display
        pygame.draw.rect(screen, (0, 255, 0), (100, 80, player_energy, 10))
        pygame.draw.rect(screen, (75, 0, 130), (100, 80, 50, 10))

        # enemy energy display
        pygame.draw.rect(screen, (0, 255, 0), (100, 80, enemy_energy, 10))
        pygame.draw.rect(screen, (75, 0, 130), (400, 80, 50, 10))

        #each turn in battle loop
    #while live:
        if player_energy <= 0:
            print("You have been defeated.")
            live = False
        elif player_energy > 0 and enemy_energy > 0:
            # player button attack
            pygame.draw.rect(screen, (248, 248, 255), (50, 300, 180, 50))  # attack
            option_text = pygame.font.SysFont("arial black", 20)
            attack = option_text.render("Attack", 1, (0, 0, 0))
            screen.blit(attack, (105, 310))

            # player button refresh
            pygame.draw.rect(screen, (248, 248, 255), (270, 300, 180, 50))  # refresh
            refresh = option_text.render("Refresh", 1, (0, 0, 0))
            screen.blit(refresh, (320, 310))

            # move mouse over position to change color
            mouse = pygame.mouse.get_pos()
            # mouse[0] implies x while mouse[1] implies y?
            if 230 > mouse[0] > 50 and 350 > mouse[1] > 300:
                pygame.draw.rect(screen, (152, 245, 255), (50, 300, 180, 50))
            elif 450 > mouse[0] > 270 and 350 > mouse[1] > 300:
                pygame.draw.rect(screen, (152, 245, 255), (270, 300, 180, 50))

            click = pygame.mouse.get_pressed()

            turn_count = 1

            # enemy choosing move
            enemy_option = [1, 2]
            enemy_choice = random.choice(enemy_option)
            #energy bar is display is in code below
            if turn_count % 2 == 0:
                # player energy after attacked
                if enemy_choice == 1:
                    player_energy -= 5
                    #pygame.draw.rect(screen, (0, 255, 0), (100, 80, player_energy, 10))
                    #pygame.draw.rect(screen, (75, 0, 130), (100, 80, 50, 10))
                    turn_count += 1
                # enemy energy after refreshed
                elif enemy_choice == 2 and enemy_energy >= 40:
                    enemy_energy += 2.5
                    #pygame.draw.rect(screen, (0, 255, 0), (400, 80, enemy_energy, 10))
                    #pygame.draw.rect(screen, (75, 0, 130), (400, 80, 50, 10))
                    turn_count += 1
            else:
                # enemy energy after attacked
                if 160 > click[0] > 100 and 350 > click[1] > 300:
                    enemy_energy -= 10
                    #pygame.draw.rect(screen, (0, 255, 0), (100, 80, enemy_energy, 10))
                    #pygame.draw.rect(screen, (75, 0, 130), (400, 80, 50, 10))
                    turn_count += 1
                # player energy after refreshed
                elif 400 > click[0] > 340 and 350 > click[1] > 300:
                    if player_energy >= 40:
                        print("Your health is full")
                    else:
                        player_energy += 5
                        #pygame.draw.rect(screen, (0, 255, 0), (100, 80, player_energy, 10))
                        #pygame.draw.rect(screen, (75, 0, 130), (400, 80, 50, 10))
                        turn_count += 1
        if enemy_energy <= 0:
            print("You have defeated the monster!")

        pygame.display.flip()

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
