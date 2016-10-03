import pygame
import random
import time
import threading


def main():
    # declare the size of the canvas
    width = 512
    height = 480
    blue_color = (97, 159, 182)

    # initialize the pygame framework
    pygame.init()

    # create screen
    screen = pygame.display.set_mode((width, height))

    # set window caption
    pygame.display.set_caption('Simple Example')

    # create a clock
    clock = pygame.time.Clock()

    ################################
    # PUT INITIALIZATION CODE HERE #
    ################################

    change_dir_countdown = 120

    monster_image = pygame.image.load('images/monster.png').convert_alpha()

    hero_image = pygame.image.load('images/hero.png').convert_alpha()

    monster_x = 345
    monster_y = 180

    loop_counter = 0

    monster_x_speed = 0
    monster_y_speed = 0

    # game loop
    stop_game = False
    while not stop_game:
        # look through user events fired
        for event in pygame.event.get():
            ################################
            # PUT EVENT HANDLING CODE HERE #
            ################################
            if event.type == pygame.QUIT:
                # if they closed the window, set stop_game to True
                # to exit the main loop
                stop_game = True

        #######################################
        # PUT LOGIC TO UPDATE GAME STATE HERE #
        #######################################

        change_dir_countdown -= 1

        # initialize pygame.display for bacground image
        background_image = pygame.image.load(
            'images/background.png').convert_alpha()

        # fill background color
        screen.blit(background_image, (0, 0))

        ################################
        # PUT CUSTOM DISPLAY CODE HERE #
        ################################

        screen.blit(hero_image, (240, 230))
        screen.blit(monster_image, (monster_x, monster_y))
        if monster_x > width:
            monster_x = 0
        if monster_x < 0:
            monster_x = 512
        if monster_y > height:
            monster_y = 0
        if monster_y < 0:
            monster_y = 480

        monster_x += monster_x_speed
        monster_y += monster_y_speed

        print change_dir_countdown
        if change_dir_countdown == 0:
            change_dir_countdown = 120
            direction = random.randint(0, 3)
            if direction == 0:
                monster_x_speed = 2
                monster_y_speed = 0
            elif direction == 1:
                monster_x_speed = -2
                monster_y_speed = 0
            elif direction == 2:
                monster_y_speed = 2
                monster_x_speed = 0
            else:
                monster_y_speed = -2
                monster_x_speed = 0

        # update the canvas display with the currently drawn frame
        pygame.display.update()

        # tick the clock to enforce a max framerate
        clock.tick(60)

    # quit pygame properly to clean up resources
    pygame.quit()

if __name__ == '__main__':
    main()
