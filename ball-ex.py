import pygame


def main():
    # declare the size of the canvas
    width = 500
    height = 500
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

    ball_x = 50
    ball_y = 50
    ball_speed_x = 5
    ball_speed_y = 5
    radius = 50

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

        ball_x += ball_speed_x
        ball_y += ball_speed_y
        if ball_x + radius > width:
            ball_speed_x = -5
        if ball_y + radius > height:
            ball_speed_y = -5
        if ball_x - radius < 0:
            ball_speed_x = 5
        if ball_y - radius < 0:
            ball_speed_y = 5

        # fill background color
        screen.fill(blue_color)

        ################################
        # PUT CUSTOM DISPLAY CODE HERE #
        ################################

        pygame.draw.circle(screen, (255, 0, 0), (ball_x, ball_y), radius)

        # update the canvas display with the currently drawn frame
        pygame.display.update()

        # tick the clock to enforce a max framerate
        clock.tick(60)

    # quit pygame properly to clean up resources
    pygame.quit()

if __name__ == '__main__':
    main()
