# PyGame Halloween House 

We are going to learn how to program a "Spooky House" halloween game using Python and Pygame.

![Spooky House Screen Shot](/screenshots/Game_Screen_Shot.png?raw=true "Spooky House")

You can follow this tutorial without any programming or Python experience, but it's a good idea to have completed through the Beginners Python (http://kata.coderdojo.com/wiki/Beginner_Python) and Intermediate Python (http://kata.coderdojo.com/wiki/Intermediate_Python) Sushi Cards if you have no experience.

## Getting Set Up

1.  Before you can start coding, you'll need to setup your computer to writePython. You'll need to have Python and a text editor installed, and know how to run a Python program.

2. To install Python, go to http://dojo.soy/py-setup and click on the Download
Python 3 button. There will be some other numbers after the 3, but they
change too often for me to include them. Don't worry about them.
Once the installer has downloaded, start it and click through it, accepting
the default choices.

3. Now you need to get a text editor, to write your Python in. We
recommend Atom, which you can download from http://atom.io, but you
can use another editor if you're more familiar with it. Or just like it better.

4. Once you have both of these setup, you're ready to go. You just need to
make sure that everything is working and that you know how to run a
Python program. Follow these steps:
  * Make a new folder for your Spooky House game.
  * Open your text editor and create a new file. Save it into the folder
you just made and call it game.py.
  * Open the command line on your computer (called command prompt
on Windows and Terminal on Mac) and navigate to your folder using
the cd command.
  * Once you've opened your folder in the command line, you're ready
to try running this blank file with this command, entered into the
command line:

```
python3 game.py
```

Note: On Windows you may need to use python rather than python3.

If this has worked, you shouldn't see any messages when you run
the command.

5. Next we need to install the PyGame (http://Pygame.org) library.
  * Open the command line on your computer
  * Run the following command to install the pygame library

```
python3 -m pip install pygame --user
```

To see if it works, run one of the included examples:

```
python3 -m pygame.examples.aliens
```

If it works, you are ready to go! 

## Making the Game

Instructions on making the game have been broken up into small steps.  You should start at step 1 with an empty game.py file.  Each step has instructions documented below.  Each step has a starting file that you can use if you have got lost.  You can use these to compare your code to a working version.  The staring files are contained in the folders named step00 through step13.

### Game Assets

A game asset is the images, fonts and sound effects that are used to make the contents of a game.

The assets directory contains all the assets required for the game.  It also contains a working directory that contains some of the source assets.

### Low Screen Resolutions
The ```assets_low``` directory contains a set of assets from running the game at a lower screen resolution.  You will need to change screen resolution set up in step 1 and the `asset_path` variable added in step 3.  

Change the variables as follows:

```
screen_width = 640
screen_height = 480
```

and

```
asset_path = "../assets_low/"
```

### Code comments
Python uses # to indicate the text following it is a comment.  Comments are useful in helping you understand the code.  The starting files contain comments to help you understand what its doing.  It is up to you to decide if you want to write comments in your own code.

```
# I am a comment
```

### Step 1 - Initialize pygame and main loop.
Ok.  Lets get started.  This steps contains everything to set up pygame and clear the screen.  It also adds the code to allow us to quit the game.

1. First of all we need to import the pygame library.  This will allow us to use pygame to make our game.

``` 
import pygame
``` 

2. Next we need to initialize the pygame library.  This tells the pygame library to get its modules ready to be used.  Add the following to do this.

```
pygame.init()
```

3. We will be drawing things in pygame, such as the sky, house, ghosts and scores.  To do this we use a screen.  We set up the screen using the following.

```
screen_width = 800
screen_height = 600

screen = pygame.display.set_mode((screen_height, screen_height))
```

You can change the game resolution here.  The above code creates a screen 800 pixels wide by 600 pixels high.   If you want to run the low resolution version change the values as shown below.  

```
screen_width = 640
screen_height = 480

screen = pygame.display.set_mode((screen_height, screen_height))
```

Most computers will be fine using 800 by 600.

4. PyGame uses a clock to help track time.  Lets create a clock.

```
clock = pygame.time.Clock()
```

5. Our game is going to use a loop.  In side this loop we will update what is happening in the game along with drawing it to the screen.  Lets add the as follows:

```
running = True

while running:
```

The running variable is used to track if we should stay in the loop or exit the game.

5.  Inside our while loop add the following to check if need to exit the loop by setting `running` to `False`.

This code is also used later to check for mouse clicks.
```
    # handle every event since the last frame.
    for event in pygame.event.get():

        # if quit (esc) exit the game
        if event.type == pygame.QUIT:
            pygame.quit()  # quit the screen
            running = False
```

You can close the game by clicking the close button on the window.

6.  Next we are going to fill our screen with solid black. Add the following to the loop as well.

``` 
   screen.fill((0, 0, 0))
```

7.  Try running the game.  Notice that the screen is white.  This is because we need to tell pygame to update the display

```
    pygame.display.update()
```
8. Now run the game.  You should see a black screen.

9. Last of all we need to call the clock.tick() function.  This will limit the game to 60 frames per second.

```
    clock.tick(60)
```

10. Try running the game again.  It should run without error.  If you are having problems, check out the game.py file in the step2 directory.

### Step 2 - Game title

Step 1 set up the pygame library and cleared the screen to black in the game loop.  Not very exciting, but needed to be done.

In this step we are going add a title to our game using a font.  Font are definitions of how text is displayed on computers.  If you have used a word processor you will have likely seen all the different fonts that are installed on your computer.


1. To draw text in the game we need to load a font.  First lets create a variable that points to the directory contain all the assets we are going to use in the game. Add the following just above the ```running = True``` line.

```
asset_path = "../assets/"
```
2. Next we need to initialize the pygame font module.  Add the following line next

```
pygame.font.init()
```
3. So lets load a font and store it in a variable we can use later whenever we need to display some text.  Add this line.

```
large_font = pygame.font.Font(asset_path + "StartlingFont.ttf", 50)

```

4. Next we are going add a function we can call to draw the title to the screen.  In game programming drawing is often referred to as rendering, so lets name our function starting with the word render.  We will do this for all the functions that are drawing stuff.  You can find out more about function in the intermediate python course.  Under the import statement add the following:

```
def render_title():
```

5. This has defined a function we can call from later in our code.  Next add the following line to create a surface

```
    surface = large_font.render("Spooky House", True, (255, 255, 255))
``` 

6.  Lets calculate a position on the screen to draw the title.  We do this by subtracting the width of the surface from the screen width and dividing it by 2.  We will store the result in a variable called ```screen_x```

```
    screen_x = (screen_width - surface.get_width()) / 2
```

7.  Last of all we need to blit (draw) our surface to the screen.  We do this with the following line.

```
    screen.blit(surface, (screen_x, 0))
    return
```

8.  Your function should look like this.

```
def render_title():
    surface = large_font.render("Spooky House", True, (255, 255, 255))
    screen_x = (screen_width - surface.get_width()) / 2
    screen.blit(surface, (screen_x, 0))
    return
```

9.  With our function complete we need to add the code to call it.  Between the ```screen.fill((0, 0, 0))``` and ```pygame.display.update()``` add the following to call our function.

```
    render_title()
```

10.  Try running the game again.  It should look like this.  If it does not run or does not look like this, check your code and try again.  You can always compare the starting file for step 03 if you need help.

![Spooky House Step 2 Screen Shot](/screenshots/step02.png?raw=true "Step 2")

### Step 3 - Draw the Sky, Windows and House
Well its a start, lets draw the sky, windows and house in this step.  We are going to draw these in layers starting with the sky, then the windows and last of all the house.  This will allow us to draw the ghosts later on between the windows and the house.

1.  As in step 2 we need to load up the image assets before we can use them.  As we know we are going to need the ghost and skull assets later on lets load them into variables at the same time.  Add the following under the ```asset_path = "../assets/"``` statement.

```
# Loading game assets
house_image = pygame.image.load(asset_path + "house.png")
sky_image = pygame.image.load(asset_path + "sky.png")
windows_image = pygame.image.load(asset_path + "windows.png")
ghost_image = pygame.image.load(asset_path + "ghost.png")
skull_image = pygame.image.load(asset_path + "skull.png")
```

2.  Lets add a function to draw the sky.  Under our import statement at the top of the file add the ```render_sky()``` function.  It draws the the sky_image surface to the screen positioning the image at the top left of the screen `(0,0)`.

```
def render_sky():
    screen.blit(sky_image, (0, 0))
    return
```
3.  We need similar function for the windows and the house.  Add the following after the ```def render_sky()``` function.

```
def render_windows():
    screen.blit(windows_image, (0, 0))
    return

def render_house():
    screen.blit(house_image, (0, 0))
    return
```

4.  Functions don't run unless they are called, so lets call them.  We need to draw the sky first, then the windows, followed by the house and last of all the title.  Add the following to our game loop before the ```   render_title()``` function call.

```
    render_sky()

    render_windows()

    render_house()
```

5.  Run the game, it should look like this.   

![Spooky House Step 3 Screen Shot](/screenshots/step03.png?raw=true "Step 3")

### Step 4 - Load the ghost data

Take a look at the house and count the windows.  You should see that it has 14.  Each window is a rectangle.  So we have a choice.  We could write the position of each window into the game code.  Thats one option, but imagine if we wanted to have a different house for harder levels than our code would become bloated with lots of data.  Its good practice to move this data into a file we can load when the program runs.  Thats the plan for this step.

If you want to find out more about read and saving files check out the Intermediate Python Sushi cards.

1. Lets take a look at our data.  In the assets directory you will find a file named ```ghost_data.txt```.  Open this with an editor and take a look.

2. Each line in the file contains the screen position of a window where we will draw a ghost.  The first number is the x position of the top left corner.  The second is y position of the top left corner.  The next two are the x and y of the bottom right. 

![Spooky House Step 4 Screen Shot](/screenshots/step04.png?raw=true "Step 4 Window Positions")

3. Lets add a function to read in the ghost data.  We will then be able to use this in the game.  Add a function at the just under the end of the ```def render_title()``` function.  This function will take an argument called asset_path that contains a string for the asset directory.

```
def read_ghost_data(asset_path):

```
4.  This function is going to return a list of ghost positions.  Add a variable to the function called ```result``` and set it to an empty list.

```
    result = []
```    

5.  Next  we are going to open and read the contents of the ```ghost_data.txt``` file.  The readlines() function will put each line of the file into a list.

```
    windows_file = open(asset_path + "ghost_data.txt", "r")
    window_lines = windows_file.readlines()
```   

6.  The window_lines list conatins one line for each window in the file.  Lets use a for loop to process each one.

```
    for line in window_lines:
```

7.  Each line ends with a special character called a new line. We need to remove this.
```
        line = line.rstrip("\n")
```

8.  Each number is seperated by a comma.  We can split this line into another list using the following:   
```
        line = line.split(",")
```

9.  To make accessing the date easier in our code, we will put the data into a dictionary.  We will also add ```visible``` and set this to ```False```.  We will use this to check if we should draw a ghost or not.

```
        line = {
            "x1": int(line[0]),
            "y1": int(line[1]),
            "x2": int(line[2]),
            "y2": int(line[3]),
            "visible": False
        }
```

10.  Almost there. Add the line to the results list.
```
        # add to a list
        result.append(line)
```

11. Finally lets close the file and return the data from the function.
   
```
    windows_file.close()
    return result
```

12.  The function should look like this.  

```
def read_ghost_data(asset_path):
    result = []
    windows_file = open(asset_path + "ghost_data.txt", "r")
    window_lines = windows_file.readlines()
    for line in window_lines:
        line = line.rstrip("\n")
        line = line.split(",")
        line = {
            "x1": int(line[0]),
            "y1": int(line[1]),
            "x2": int(line[2]),
            "y2": int(line[3]),
            "visible": False
        }
        result.append(line)
    windows_file.close()
    return result
```
13. We can call the function in our code to load the data into the ghosts variable.  Add the following before the ```running = True``` variable we added earlier.

```
ghosts = read_ghost_data(asset_path)
```

14.  Wow thats a lot to take in.  Try running the program now.  It should run without error.  If not, check the starting code for the next step if you need help.  


### Step 5 - Draw some ghosts

Step 4 loaded the ghost data for the positions we will draw the ghosts on the screen.  This dictionary for each ghost containing the window positions and a key for the visibility of the ghost.  In this step we will add a function to draw an individual ghost.  To test this we will add a function to loop over all the ghosts in the list and draw them.

1. Under the ```def read_ghost_data(asset_path):``` add a new function that will draw a single ghost we pass into it.

```
def render_ghost(ghost):
```

2. Our windows are different sizes.  Rather than have different sized ghosts we can use the pygame library to transform our ghost image before we blit it to the screen.  Lets calculate the width and height.

``` 
    ghost_width = ghost["x2"] - ghost["x1"]
    ghost_height = ghost["y2"] - ghost["y1"]
```

3. With the width and height we can call the pygame.transform.scale function to resize the ghost before we blit it. 
```
    ghost_scaled = pygame.transform.scale(ghost_image, (ghost_width, ghost_height))
```

4. Lets draw the scaled ghost to the screen, using the top left (x1, y1) coordinates to position on the screen.  We can also end the function using the return statement.

```
    screen.blit(ghost_scaled, (ghost["x1"], ghost["y1"]))
    return
```

5.  The function should look like this.

```
def render_ghost(ghost):
    ghost_width = ghost["x2"] - ghost["x1"]
    ghost_height = ghost["y2"] - ghost["y1"]
    ghost_scaled = pygame.transform.scale(ghost_image, (ghost_width, ghost_height))
    screen.blit(ghost_scaled, (ghost["x1"], ghost["y1"]))
    return
```

6.  Lets add another function to draw all the ghosts.  Add this below the ```def render_ghost(ghost):``` function we just added.  As you can see the function uses a for loop and calls the ```def render_ghost(ghost):``` with each ghost.

```
def render_ghosts():
    # Draw some ghosts
    for ghost in ghosts:
        render_ghost(ghost)
    return
```

7.  Last of all we need to call the ```def render_ghosts():``` function.  Remember in step3 we added functions to draw the sky, windows and house textures.  We need to add a call to ```def render_ghosts():``` after the ```render_windows()``` call and before the ``` render_house()``` call.

8.  Try running the game now.  It should look like this.  

![Spooky House Step 5 Screen Shot](/screenshots/step05.png?raw=true "Step 5 All the ghosts")



### Step 6
Show a random ghost if none is displayed

### Step 7
Hide the ghost after a time
Show a ghost after a time

### Step 8 
Check for mouse clicks 
Check for mouse clicks on visible ghosts

### Step 9
Hide found ghost
Score

### Step 10
Lives

### Step 11
Menu

### Step 12
Game Over

### Step 13

Other things to try

Make the game harder as the score increases
Audio and Sound effects
Animation
Different Game Assets



