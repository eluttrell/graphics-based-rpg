import pygame
import random
import time
import math

KEY_UP = 273
KEY_DOWN = 274
KEY_LEFT = 276
KEY_RIGHT = 275


class Hero(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.x_speed = 0
        self.y_speed = 0

    def render(self, screen):
        hero_image = pygame.image.load('images/hero.png').convert_alpha()
        screen.blit(hero_image, (self.x, self.y))

    def stay_on_screen(self):
        if self.x >= 448:
            self.x = 448
        if self.x <= 32:
            self.x = 32
        if self.y >= 408:
            self.y = 408
        if self.y <= 32:
            self.y = 32

    def movement(self):
        self.x += self.x_speed
        self.y += self.y_speed


class Monster(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.x_speed = 6
        self.y_speed = 6

    def render(self, screen):
        monster_image = pygame.image.load('images/monster.png').convert_alpha()
        screen.blit(monster_image, (self.x, self.y))

    def stay_on_screen(self):
        if self.x > 512:
            self.x = 0
        if self.x < 0:
            self.x = 512
        if self.y > 480:
            self.y = 0
        if self.y < 0:
            self.y = 480

    def monster_move(self):
        self.x += self.x_speed
        self.y += self.y_speed

    def change_direction(self):
        x = 6
        direction = random.randint(0, 8)
        if direction == 0:
            self.x_speed = x
            self.y_speed = 0
        elif direction == 1:
            self.x_speed = -x
            self.y_speed = 0
        elif direction == 2:
            self.y_speed = x
            self.x_speed = 0
        elif direction == 3:
            self.y_speed = -x
            self.x_speed = 0
        elif direction == 4:
            self.y_speed = x
            self.x_speed = x
        elif direction == 5:
            self.y_speed = -x
            self.x_speed = -x
        elif direction == 6:
            self.y_speed = x
            self.x_speed = -x
        else:
            self.y_speed = -x
            self.x_speed = x


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

    # monster stuff
    change_dir_countdown = 50
    monster = Monster(345, 180)

    # hero stuff
    # hero_image = pygame.image.load('images/hero.png').convert_alpha()
    hero = Hero(240, 230)

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
            if event.type == pygame.KEYDOWN:
                # activate the cooresponding speeds
                # when an arrow key is pressed down
                if event.key == KEY_DOWN:
                    hero.y_speed = 3
                elif event.key == KEY_UP:
                    hero.y_speed = -3
                elif event.key == KEY_LEFT:
                    hero.x_speed = -3
                elif event.key == KEY_RIGHT:
                    hero.x_speed = 3
            if event.type == pygame.KEYUP:
                # deactivate the cooresponding speeds
                # when an arrow key is released
                if event.key == KEY_DOWN:
                    hero.y_speed = 0
                elif event.key == KEY_UP:
                    hero.y_speed = 0
                elif event.key == KEY_LEFT:
                    hero.x_speed = 0
                elif event.key == KEY_RIGHT:
                    hero.x_speed = 0

        #######################################
        # PUT LOGIC TO UPDATE GAME STATE HERE #
        #######################################

        hero.movement()

        change_dir_countdown -= 1

        # initialize pygame.display for bacground image
        background_image = pygame.image.load(
            'images/background.png').convert_alpha()

        # fill background color
        screen.blit(background_image, (0, 0))

        ################################
        # PUT CUSTOM DISPLAY CODE HERE #
        ################################

        # hero stuff
        # screen.blit(hero_image, (240, 230))
        hero.render(screen)
        hero.stay_on_screen()

        # monster stuff
        monster.render(screen)
        monster.stay_on_screen()
        monster.monster_move()
        if change_dir_countdown == 0:
            monster.change_direction()
            change_dir_countdown = 50

        # update the canvas display with the currently drawn frame
        pygame.display.update()

        # tick the clock to enforce a max framerate
        clock.tick(60)

    # quit pygame properly to clean up resources
    pygame.quit()

if __name__ == '__main__':
    main()
