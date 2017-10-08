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
    windows_file = open(asset_path + "windows_data.txt", "r")
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
    window_width = ghost["x2"] - ghost["x1"]
    window_height = ghost["y2"] - ghost["y1"]
    # Resize the ghost image to the window
    windows_scaled = pygame.transform.scale(
        ghost_image, (window_width, window_height))
    # Draw ghost
    screen.blit(windows_scaled, (ghost["x1"], ghost["y1"]))
    return


def update_ghosts():
    global hide_ghost_at, show_ghost_at
    "Update the ghost states"

    # if the hide time is in the past, hide the ghosts
    if hide_ghost_at < pygame.time.get_ticks():
        for ghost in ghosts:
            if ghost["visible"] == True:
                ghost["visible"] = False
                show_ghost_at = randomShowTime()

    # check to see if all ghosts are hidden
    if(all(ghost["visible"] == False for ghost in ghosts)):
        # if show_ghost_at is in the past, show a ghost
        if show_ghost_at < pygame.time.get_ticks():
            ghost_to_turn_on = randint(0, len(ghosts) - 1)
            ghosts[ghost_to_turn_on]["visible"] = True
            hide_ghost_at = randomHideTime()

    return


def randomHideTime():
    "Return when to hide the ghost in ticks"
    now = pygame.time.get_ticks()
    now = now + randint(1000, 2000)
    return now


def randomShowTime():
    "Return when to show the next ghost in ticks"
    now = pygame.time.get_ticks()
    now = now + randint(1000, 3000)
    return now


def render_ghosts():
    "Draw the ghosts"
    # Check each of the ghosts
    for ghost in ghosts:
        # Check if its visible
        if(ghost["visible"]):
            # Draw it
            render_ghost(ghost)
    return


def checkMouseClick(mouse_position):
    "Check if the mouse position is over a visible ghost"
    for ghost in ghosts:

        # Check if its visible
        if(ghost["visible"]):

            # call a function to check if we have clicked ghost
            ghost_clicked = checkPoint(mouse_position, ghost)

            if(ghost_clicked):
                print("found ghost")
    return


def checkPoint(mouse_position, ghost):
    "check to see point is in rectangle"
    # create a rectangle
    rect = pygame.Rect((ghost["x1"], ghost["y1"]), (ghost["x2"], ghost["y2"]))
    # check to see if our mouse position is inside the rectangle
    result = rect.collidepoint(mouse_position)
    return result

# Define variables
screen_width = 800
screen_height = 600

# set up pygame
pygame.init()

# set up a screen 800 pixels wide by 600 high
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

# Hide and shot times
hide_ghost_at = 0
show_ghost_at = 0

# Window Positions
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
        elif event.type == pygame.MOUSEBUTTONDOWN:
            checkMouseClick(pygame.mouse.get_pos())

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
