import pygame
from random import randint


def render_sky():
    "Draw the sky"
    screen.blit(sky_image, (0, 0))


def render_windows():
    "Draw the window back grounds"
    screen.blit(windows_image, (0, 0))


def render_house():
    "Draw the house"
    screen.blit(house_image, (0, 0))


def render_title():
    "Draw the title of the game in the center of the screen"
    # draw title text to a surface
    surface = large_font.render("Spooky House", True, (255, 255, 255))
    # calculate the x postion to center text
    screen_x = (screen_width - surface.get_width()) / 2
    # draw to screen
    screen.blit(surface, (screen_x, 0))


def update_ghosts():
    "Update the ghost states"
    # check to see how many ghost we are displaying
    if(ghost_states.count(1) == 0):
        ghost_to_turn_on = randint(0, len(window_positions))
        ghost_states[ghost_to_turn_on] = 1


def render_ghosts():
    "Draw the ghosts"
    for ghost_index in range(0, len(window_positions)):
        if(ghost_states[ghost_index] == 1):
            render_ghost(ghost_index)


def render_ghost(ghost):
    "Draw a ghost"

    ghost_window = window_positions[ghost]
    window_width = ghost_window[2] - ghost_window[0]
    window_height = ghost_window[3] - ghost_window[1]
    windows_scaled = pygame.transform.scale(
        ghost_image, (window_width, window_height))
    screen.blit(windows_scaled, (ghost_window[0], ghost_window[1]))


# Define variables
screen_width = 800
screen_height = 600

# set up pygame
pygame.init()

# set up a screen 800 pixels wide by 600 high
screen = pygame.display.set_mode((screen_width, screen_height))

# set up the clock
clock = pygame.time.Clock()

# Loading game assets
house_image = pygame.image.load("../assets/house.png")
sky_image = pygame.image.load("../assets/sky.png")
windows_image = pygame.image.load("../assets/windows.png")
ghost_image = pygame.image.load("../assets/ghost.png")

# set up font support
pygame.font.init()
large_font = pygame.font.Font("../assets/StartlingFont.ttf", 60)

# Window Positions
window_positions = [
    [182, 385, 	224, 472],
    [272, 385,	314, 473],
    [520, 386,	560, 470],
    [606, 385,	648, 471],

    [184, 275,	224, 348],
    [273, 275,	314, 348],
    [395, 275,	436, 345],
    [518, 275,	561, 348],
    [606, 275,	646, 348],

    [239, 179,	269, 220],
    [395, 178,	428, 220],
    [559, 178,	592, 220],

    [395, 408, 438, 478],
    [73, 428, 88, 458]]

ghost_states = []
for ghost_index in range(0, len(window_positions)):
    ghost_states.append(0)

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

    # Update ghosts
    update_ghosts()

    # draw sky
    render_sky()

    # draw windows
    render_windows()

    # render ghost
    render_ghosts()

    # draw house
    render_house()

    # draw title
    render_title()

    # update the screen
    pygame.display.update()

    # limit the game to 60 frames per second
    clock.tick(60)