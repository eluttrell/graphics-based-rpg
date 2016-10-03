import pygame
import random
import time
import threading


class Monster(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.x_speed = 3
        self.y_speed = 3

    def render(self, screen):
        monster_image = pygame.image.load('images/monster.png').convert_alpha()
        screen.blit(monster_image, (self.x, self.y))

    def stay_on_screen(self, width, height):
        if self.x > width:
            self.x = 0
        if self.x < 0:
            self.x = 512
        if self.y > height:
            self.y = 0
        if self.y < 0:
            self.y = 480

    def monster_move(self):
        self.x += self.x_speed
        self.y += self.y_speed

    def change_direction(self):
        direction = random.randint(0, 8)
        if direction == 0:
            self.x_speed = 2
            self.y_speed = 0
        elif direction == 1:
            self.x_speed = -2
            self.y_speed = 0
        elif direction == 2:
            self.y_speed = 2
            self.x_speed = 0
        elif direction == 3:
            self.y_speed = -2
            self.x_speed = 0
        elif direction == 4:
            self.y_speed = 2
            self.x_speed = 2
        elif direction == 5:
            self.y_speed = -2
            self.x_speed = -2
        elif direction == 6:
            self.y_speed = 2
            self.x_speed = -2
        else:
            self.y_speed = -2
            self.x_speed = 2


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

    change_dir_countdown = 50

    # monster_image = pygame.image.load('images/monster.png').convert_alpha()

    monster = Monster(345, 180)

    hero_image = pygame.image.load('images/hero.png').convert_alpha()

    # monster_x = 345
    # monster_y = 180

    # monster_x_speed = 0
    # monster_y_speed = 0

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
        # screen.blit(monster_image, (monster_x, monster_y))
        monster.render(screen)
        monster.stay_on_screen(512, 480)
        monster.monster_move()
        if change_dir_countdown == 0:
            monster.change_direction()
            change_dir_countdown = 50
        # if monster_x > width:
        #     monster_x = 0
        # if monster_x < 0:
        #     monster_x = 512
        # if monster_y > height:
        #     monster_y = 0
        # if monster_y < 0:
        #     monster_y = 480

        # monster_x += monster_x_speed
        # monster_y += monster_y_speed

        # if change_dir_countdown == 0:
        #     change_dir_countdown = 50
        #     direction = random.randint(0, 3)
        #     if direction == 0:
        #         monster_x_speed = 2
        #         monster_y_speed = 0
        #     elif direction == 1:
        #         monster_x_speed = -2
        #         monster_y_speed = 0
        #     elif direction == 2:
        #         monster_y_speed = 2
        #         monster_x_speed = 0
        #     else:
        #         monster_y_speed = -2
        #         monster_x_speed = 0

        # update the canvas display with the currently drawn frame
        pygame.display.update()

        # tick the clock to enforce a max framerate
        clock.tick(60)

    # quit pygame properly to clean up resources
    pygame.quit()

if __name__ == '__main__':
    main()
