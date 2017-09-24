import pygame


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

# set up font support
pygame.font.init()
large_font = pygame.font.Font("../assets/StartlingFont.ttf", 60)

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

    # draw sky
    render_sky()

    # draw windows
    render_windows()

    # draw house
    render_house()

    # draw title
    render_title()

    # update the screen
    pygame.display.update()

    # limit the game to 60 frames per second
    clock.tick(60)
