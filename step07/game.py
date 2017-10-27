import pygame
from random import randint


def render_sky():
    "Draw the sky"
    screen.blit(sky_image, (0, 0))
    return


def render_windows():
    "Draw the window back grounds"
    screen.blit(windows_image, (0, 0))
    return


def render_house():
    "Draw the house"
    screen.blit(house_image, (0, 0))
    return


def render_title():
    "Draw the title of the game in the center of the screen"
    # draw title text to a surface
    surface = large_font.render("Spooky House", True, (255, 255, 255))
    # calculate the x postion to center text
    screen_x = (screen_width - surface.get_width()) / 2
    # draw to screen
    screen.blit(surface, (screen_x, 0))
    return


def read_ghost_data(asset_path):
    "Read the positions of the ghosts"
    result = []
    # open up the file for reading
    windows_file = open(asset_path + "ghost_data.txt", "r")
    # read the contents
    window_lines = windows_file.readlines()
    # process each line to a list
    for line in window_lines:
        line = line.rstrip("\n")
        line = line.split(",")
        # create a dictionary for each line
        line = {
            "x1": int(line[0]),
            "y1": int(line[1]),
            "x2": int(line[2]),
            "y2": int(line[3]),
            "visible": False
        }
        # add to a list
        result.append(line)
    # close the file
    windows_file.close()
    return result


def render_ghost(ghost):
    "Draw a ghost"
    # Calculate width and height of Window
    ghost_width = ghost["x2"] - ghost["x1"]
    ghost_height = ghost["y2"] - ghost["y1"]
    # Resize the ghost image to the window
    ghost_scaled = pygame.transform.scale(
        ghost_image, (ghost_width, ghost_height))
    # Draw ghost
    screen.blit(ghost_scaled, (ghost["x1"], ghost["y1"]))
    return


def render_ghosts():
    # Draw some ghosts
    for ghost in ghosts:
        if ghost["visible"]:
            render_ghost(ghost)


def update_ghosts():
    "Update the ghost states"

    # check to see if all ghosts are hidden
    if(all(ghost["visible"] == False for ghost in ghosts)):
        ghost_to_turn_on = randint(0, len(ghosts) - 1)
        ghosts[ghost_to_turn_on]["visible"] = True

    return

# Define variables
screen_width = 800
screen_height = 600

# set up pygame
pygame.init()

# set up a screen
screen = pygame.display.set_mode((screen_width, screen_height))

# set up the clock
clock = pygame.time.Clock()

# folder containing the game assets
asset_path = "../assets/"

# Loading game assets
house_image = pygame.image.load(asset_path + "house.png")
sky_image = pygame.image.load(asset_path + "sky.png")
windows_image = pygame.image.load(asset_path + "windows.png")
ghost_image = pygame.image.load(asset_path + "ghost.png")
skull_image = pygame.image.load(asset_path + "skull.png")

# set up font support
pygame.font.init()
large_font = pygame.font.Font(asset_path + "StartlingFont.ttf", 50)

# Ghost Positions
ghosts = read_ghost_data(asset_path)

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

    # draw ghosts
    render_ghosts()

    # draw house
    render_house()

    # draw title
    render_title()

    # update the screen
    pygame.display.update()

    # limit the game to 60 frames per second
    clock.tick(60)
