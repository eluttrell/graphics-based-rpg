import pygame
import random
import time
import math

KEY_UP = 273
KEY_DOWN = 274
KEY_LEFT = 276
KEY_RIGHT = 275


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
        direction = random.randint(0, 8)
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
        elif direction == 4:
            self.y_speed = random.randint(3, 7)
            self.x_speed = random.randint(3, 7)
        elif direction == 5:
            self.y_speed = -random.randint(3, 7)
            self.x_speed = -random.randint(3, 7)
        elif direction == 6:
            self.y_speed = random.randint(3, 7)
            self.x_speed = -random.randint(3, 7)
        else:
            self.y_speed = -random.randint(3, 7)
            self.x_speed = random.randint(3, 7)


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

    def __init__(self):
        self.x = random.randint(33, 440)
        self.y = random.randint(33, 440)
        self.x_speed = random.randint(3, 7)
        self.y_speed = random.randint(3, 7)

    def render(self, screen):
        goblin_image = pygame.image.load('images/goblin.png').convert_alpha()
        screen.blit(goblin_image, (self.x, self.y))


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

    # monster stuff
    change_dir_countdown = 50
    monster = Monster()

    # hero stuff
    # hero_image = pygame.image.load('images/hero.png').convert_alpha()
    hero = Hero(240, 230)

    # goblin stuff
    goblin = Goblin()
    goblin2 = Goblin()
    goblin3 = Goblin()

    # music
    game_music.play()

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
            if event.type == pygame.KEYDOWN:
                if event.key == 13:
                    monster.dead = False
                    monster = Monster()
                    hero.dead = False
                    hero = Hero(240, 230)
                    game_music.play()
                elif event.key == 27:
                    break

        #######################################
        # PUT LOGIC TO UPDATE GAME STATE HERE #
        #######################################

        hero.movement()
        monster.movement()
        goblin.movement()
        goblin2.movement()
        goblin3.movement()

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
        else:
            font = pygame.font.Font(None, 25)
            text = font.render(
                'You Win! Hit ENTER to play again!', True, (0, 0, 0))
            screen.blit(text, (150, 230))

        monster.loop_across_screen(512, 480)
        if change_dir_countdown == 0:
            monster.change_direction()
            change_dir_countdown = 50

        # goblin stuff
        goblin.render(screen)
        goblin2.render(screen)
        goblin3.render(screen)
        goblin.loop_across_screen(512, 480)
        if change_dir_countdown == 0:
            goblin.change_direction()
            change_dir_countdown = 50
        goblin2.loop_across_screen(512, 480)
        if change_dir_countdown == 0:
            goblin.change_direction()
            change_dir_countdown = 50
        goblin3.loop_across_screen(512, 480)
        if change_dir_countdown == 0:
            goblin.change_direction()
            change_dir_countdown = 50

        # catch the monster
        if math.hypot(hero.x - monster.x, hero.y - monster.y) <= 32:
            game_music.stop()
            win_sound.play()
            monster.dead = True

        # goblin catch hero
        if math.hypot(hero.x - goblin.x, hero.y - goblin.y) <= 32 or math.hypot(hero.x - goblin2.x, hero.y - goblin2.y) <= 32 or math.hypot(hero.x - goblin3.x, hero.y - goblin3.y) <= 32:
            game_music.stop()
            lose_sound.play()
            hero.dead = True

        # update the canvas display with the currently drawn frame
        pygame.display.update()

        # tick the clock to enforce a max framerate
        clock.tick(60)

    # quit pygame properly to clean up resources
    pygame.quit()

if __name__ == '__main__':
    main()
