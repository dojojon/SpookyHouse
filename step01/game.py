import pygame

# set up pygame
pygame.init()

# set up a screen 800 pixels wide by 600 high
screen = pygame.display.set_mode((800, 600))

# set up the clock
clock = pygame.time.Clock()

# keep the game running while true
running = True

while running:

    # handle every event since the last frame.
    for event in pygame.event.get():

        # if quit (esc) exit the game
        if event.type == pygame.QUIT:
            pygame.quit()  # quit the screen
            running = False

    # fill the screen with a solid black colour
    screen.fill((0, 0, 0))

    # update the screen
    pygame.display.update()

    # limit the game to 60 frames per second
    clock.tick(60)
