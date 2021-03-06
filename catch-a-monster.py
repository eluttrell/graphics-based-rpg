import pygame
import random
import time
import math

KEY_UP = 273
KEY_DOWN = 274
KEY_LEFT = 276
KEY_RIGHT = 275
ENTER = 13


class Move(object):

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def movement(self):
        self.x += self.x_speed
        self.y += self.y_speed

    def stay_on_screen(self):
        if self.x >= 448:
            self.x = 448
        if self.x <= 32:
            self.x = 32
        if self.y >= 408:
            self.y = 408
        if self.y <= 32:
            self.y = 32

    def loop_across_screen(self, screen_width, screen_height):
        if self.x > screen_width:
            self.x = 0
        if self.x < 0:
            self.x = screen_width
        if self.y > screen_height:
            self.y = 0
        if self.y < 0:
            self.y = screen_height

    def change_direction(self):
        direction = random.randint(0, 4)
        if direction == 0:
            self.x_speed = random.randint(3, 7)
            self.y_speed = 0
        elif direction == 1:
            self.x_speed = -random.randint(3, 7)
            self.y_speed = 0
        elif direction == 2:
            self.y_speed = random.randint(3, 7)
            self.x_speed = 0
        elif direction == 3:
            self.y_speed = -random.randint(3, 7)
            self.x_speed = 0


class Hero(Move):

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.x_speed = 0
        self.y_speed = 0
        self.dead = False

    def render(self, screen):
        hero_image = pygame.image.load('images/hero.png').convert_alpha()
        screen.blit(hero_image, (self.x, self.y))


class Monster(Move):

    def __init__(self):
        self.x = random.randint(33, 440)
        self.y = random.randint(33, 440)
        self.x_speed = random.randint(3, 7)
        self.y_speed = random.randint(3, 7)
        self.dead = False

    def render(self, screen):
        monster_image = pygame.image.load('images/monster.png').convert_alpha()
        screen.blit(monster_image, (self.x, self.y))


class Goblin(Move):

    def __init__(self, x, y):
        self.x = random.randint(33, 440)
        self.y = random.randint(33, 440)
        self.x_speed = x
        self.y_speed = y

    def render(self, screen):
        goblin_image = pygame.image.load('images/goblin.png').convert_alpha()
        screen.blit(goblin_image, (self.x, self.y))

    def change_speed(self, x):
        self.x_speed = x
        self.y_speed = x

    # def decrease_speed(self):
    #     self.x_speed -= 1
    #     self.y_speed -= 1


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

    # sounds for game
    win_sound = pygame.mixer.Sound('sounds/win.wav')
    lose_sound = pygame.mixer.Sound('sounds/lose.wav')
    game_music = pygame.mixer.Sound('sounds/music.wav')

    ################################
    # PUT INITIALIZATION CODE HERE #
    ################################

    # game counters
    win_counter = 0
    lose_counter = 0

    # monster stuff
    change_dir_countdown = 50
    monster = Monster()

    # hero stuff
    # hero_image = pygame.image.load('images/hero.png').convert_alpha()
    hero = Hero(240, 230)

    # goblin stuff
    goblin_list = [
        Goblin(2, 2),
        Goblin(3, 3),
        Goblin(4, 4)
    ]

    # music
    game_music.play()

    # game loop
    game_over = False
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
            if event.type == pygame.KEYDOWN:
                if event.key == ENTER:
                    monster.dead = False
                    monster = Monster()
                    hero.dead = False
                    hero = Hero(240, 230)
                    game_music.play()
                    game_over = False
                elif event.key == 27:
                    break

        #######################################
        # PUT LOGIC TO UPDATE GAME STATE HERE #
        #######################################

        hero.movement()
        monster.movement()
        for goblin in goblin_list:
            goblin.movement()

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
        if hero.dead == False:
            hero.render(screen)
        else:
            game_music.stop()
            font = pygame.font.Font(None, 25)
            text = font.render(
                'You Lose :( Hit ENTER to play again!', True, (0, 0, 0))
            screen.blit(text, (150, 230))

        hero.stay_on_screen()

        # monster stuff
        if monster.dead == False:
            monster.render(screen)
        elif hero.dead == True:
            monster.render(screen)
        elif monster.dead == True:
            font = pygame.font.Font(None, 25)
            text = font.render(
                'You Win! Hit ENTER to play again!', True, (0, 0, 0))
            screen.blit(text, (150, 230))

        monster.loop_across_screen(width, height)
        if change_dir_countdown == 0:
            monster.change_direction()
            change_dir_countdown = 50

        # goblin stuff
        for goblin in goblin_list:
            goblin.render(screen)
            goblin.loop_across_screen(width, height)
            if change_dir_countdown == 0:
                goblin.change_direction()
                change_dir_countdown = 50

        # catch the monster
        if math.hypot(hero.x - monster.x, hero.y - monster.y) <= 32:
            game_music.stop()
            win_sound.play()
            win_counter += 1
            game_over = True
            monster.dead = True

        # goblin catch hero
        for goblin in goblin_list:
            if math.hypot(hero.x - goblin.x, hero.y - goblin.y) <= 32:
                game_music.stop()
                lose_sound.play()
                hero.dead = True
                lose_counter += 1
                game_over = True

        # win and lose counters
        gold_counter = win_counter - lose_counter + 50
        font = pygame.font.Font(None, 25)
        text = font.render(
            'Gold: %d' % gold_counter, True, (255, 255, 255))
        screen.blit(text, (5, 460))
        speed_increase = gold_counter / 100
        if speed_increase == 1:
            for goblin in goblin_list:
                goblin.change_speed(4)
        elif speed_increase == 2:
            for goblin in goblin_list:
                goblin.change_speed(7)
        elif speed_increase == 0:
            for goblin in goblin_list:
                goblin.change_speed(2)

        # update the canvas display with the currently drawn frame
        pygame.display.update()

        # tick the clock to enforce a max framerate
        clock.tick(60)

    # quit pygame properly to clean up resources
    pygame.quit()

if __name__ == '__main__':
    main()
