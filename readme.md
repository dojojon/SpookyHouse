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

Instructions on making the game have been broken up into small steps.  You should start at step 1 with an empty game.py file.  Each step has instructions documented below.  Each step has a starting file that you can use if you have got lost.  You can use these to compare your code to a working version.  The staring files are contained in the folders named step00 through step12.

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

screen = pygame.display.set_mode((screen_width, screen_height))
```

You can change the game resolution here.  The above code creates a screen 800 pixels wide by 600 pixels high.   If you want to run the low resolution version change the values as shown below.  

```
screen_width = 640
screen_height = 480

screen = pygame.display.set_mode((screen_width, screen_height))
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


### Step 6  Random Ghosts

So in this game we will show a ghost if none are visible.  Lets add a function called ```update_ghosts()``` to make this happen.
1.  At the top of the game.py file we need to import a random number function.  Add the following under the ```import pygame```.

```
from random import randint
```

2.  Add a function near the ```render_ghosts()``` function
```
def update_ghosts():
```

3. We area going to use the visible attribute of the ghost data to store if a ghost is visible or not.  We only want to set this to true if all of the ghosts are hidden.  We can use the build in all function to do this.  You find out more about the all function here [https://docs.python.org/2/library/functions.html#all].  We can use the all function to return ```True``` if all the ghosts are not visible.

```
    if(all(ghost["visible"] == False for ghost in ghosts)):
```

4.  If no ghost is visible, then use another function to pick one at random and make if visible.  

```
        ghost_to_turn_on = randint(0, len(ghosts) - 1)
        ghosts[ghost_to_turn_on]["visible"] = True
```

5. Last of all lets close the function by returning,
```
    return
```

6.  The function should look like this.

```
def update_ghosts():
    if(all(ghost["visible"] == False for ghost in ghosts)):
        ghost_to_turn_on = randint(0, len(ghosts) - 1)
        ghosts[ghost_to_turn_on]["visible"] = True
    return
```

7.  We need to call this function in out game loop.  Below the screen.fill((0,0,0)) call, call our new function.

```
    update_ghosts()
```

8.  Try running the game now.  Strange all the ghosts are still showing.  Thats because we need to add an if statement to only render ghosts if they are visible.  Go to the ```render_ghosts()``` function.  It should look like this.

```
def render_ghosts():
    # Draw some ghosts
    for ghost in ghosts:
        render_ghost(ghost)

```

9.  Add an if statement to only call the render_ghost() function if the ghost is visible.

```
def render_ghosts():
    # Draw some ghosts
    for ghost in ghosts:
        if ghost["visible"]:
            render_ghost(ghost)
```

10. Try running it again, now you should see a single ghost being drawn.  Try stopping and starting the game a few times to see a different ghost drawn. 


### Step 7 Now you see me, now you don't
In the last step we added code to randomly select a ghost if none as visible.  This step lets hide the ghost after a little time.  We are going to use the pygame function ```pygame.time.get_ticks()``.  This function returns the number of milliseconds (also known as ticks in game programming) since we initialized pygame.  It does not reset and just continues to get bigger.

1.  Lets add two variables to track when we need to hide and show a ghost.  Add the following near the ```running = True``` statement.

```
hide_ghost_at = 0
show_ghost_at = 0
```

2. Next we will add two functions that we can call to set the hide_ghost_at and show_ghost_at variables.  Ypou can put them near the ```update_ghosts()``` function.  We are going to use the ```randint()``` function.  We can call the ```randint(min, max)``` with a minimum and maximum values.  This is handy as the result will be between these values.   FYI.  1000 ticks equals 1 second 

```
def randomHideTime():
    now = pygame.time.get_ticks()
    now = now + randint(1000, 2000)
    return now

def randomShowTime():
    now = pygame.time.get_ticks()
    now = now + randint(1000, 3000)
    return now
```

3. Next we will use these functions in the ```update_ghosts()``` functions.  We need to be able to access the global ```hide_ghost_at``` and ```show_ghost_at``` variables.  Add the following below ```def update_ghosts():``` function definition.

```
    global hide_ghost_at, show_ghost_at
```

4. If the hide time is in the past (smaller than the current number of ticks, lets hide any visible ghosts.  We can use and if statement and a for loop to do this. 

```
    if hide_ghost_at < pygame.time.get_ticks():
        for ghost in ghosts:
            if ghost["visible"] == True:
                ghost["visible"] = False
```

5.  As we have hidden all the ghosts we need to set the show_ghost_at variable.  Add the following just the for loop.  Add this just before the for loop.  

```
        show_ghost_at = randomShowTime()
```

6.  Try running the game.  The ghost should disappear.  Lets now add the code to make it re-appear.  Similar to the hiding ghosts we will add an if statment to check the ```show_ghosts_at```.  Add an if statement within the check to see if all the ghosts are hidden.  We will also need to indent the code that selects a random ghost.

```
    if(all(ghost["visible"] == False for ghost in ghosts)):
        # if show_ghost_at is in the past, show a ghost
        if show_ghost_at < pygame.time.get_ticks():
            ghost_to_turn_on = randint(0, len(ghosts) - 1)
```

7. Last of all we need to set the ```hide_ghost_at``` variable.  Do this after the statement that sets the ghost visible.  The complete ```update_ghosts``` function is show below:

```
def update_ghosts():
    global hide_ghost_at, show_ghost_at
    "Update the ghost states"

    # if the hide time is in the past, hide the ghosts
    if hide_ghost_at < pygame.time.get_ticks():
        show_ghost_at = randomShowTime()
        for ghost in ghosts:
            if ghost["visible"] == True:
                ghost["visible"] = False

    # check to see if all ghosts are hidden
    if(all(ghost["visible"] == False for ghost in ghosts)):
        # if show_ghost_at is in the past, show a ghost
        if show_ghost_at < pygame.time.get_ticks():
            ghost_to_turn_on = randint(0, len(ghosts) - 1)
            ghosts[ghost_to_turn_on]["visible"] = True
            hide_ghost_at = randomHideTime()

    return
```

8.  Run the game, and you should see the ghost appear and disappear.

### Step 8 Mouse clicks

Ok,  In this step we will use the pygame events system to detect mouse clicks.

1.  Go to main game loop and find the event processing we added earlier.  We are going to add another test to check for pygame mouse click events.  This event is only occurs when the mouse is down.   If we see it we will call a function with the screen position of the mouse pointer which we can get by calling ```pygame.mouse.get_pos()```.  You can see the extra two lines at the bottom.

```
    # handle every event since the last frame.
    for event in pygame.event.get():

        # if quit (esc) exit the game
        if event.type == pygame.QUIT:
            pygame.quit()  # quit the screen
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            checkMouseClick(pygame.mouse.get_pos())

```

2. Lets add the checkMouseClick function. We are going to check each ghost that is visible.  We can do this with a for loop and an if statement.  If visible we will call another function that will check we clicked a ghost.  For now lets just print out if we have found a ghost.  The code should look like the following:

```
def checkMouseClick(mouse_position):

    for ghost in ghosts:

        if ghost["visible"]:
            ghost_clicked = checkPoint(mouse_position, ghost)

            if(ghost_clicked):
                print("found ghost")

```

3.  We need to implement the checkPoint function.  This takes the mouse_position and a ghost.  We will use a ```pygame.Rect``` object that has functions to help check if a point is inside it.  The function will return True if the mouse click is with the rectangle of the ghost.

```
def checkPoint(mouse_position, ghost):

    rect = pygame.Rect((ghost["x1"], ghost["y1"]), (ghost["x2"], ghost["y2"]))

    result = rect.collidepoint(mouse_position)

    return result

```

4.  Try running the game now.  Try clicking on a ghost, you should see "found ghost" printed in the terminal window.  Also try not clicking on a ghost, less exciting, you should not see anything.

### Step 9  Ghost Busters !!!

In the last step we added code for using the mouse events to detect if we found a ghost.  In this step we will hide the ghost if we click it and a place score.

1.  We can keep track of the score using a variable.  Add one near the ```running = True``` statement.

```
score = 0
```

2.   Lets add a function to render the score to the screen.

```
def render_score():
    surface = large_font.render("Score:" + str(score), True, (255, 255, 255))
    screen.blit(surface, (10, 0))
    return

```

3.  We need to call this in the game loop.  Add a call to this function just after the ```render_title()``` function.

```
    render_score()
```

4.  Try running the game.  You should now see the score displayed in the top left of the screen.

5.  Remember the code we added to print out "found ghost".  Replace that with a call to a new function we are about to create..

```
    ghost_found(ghost)
```

6.  Now lets create the ```ghost_found()``` function that will take a ghost as a parameter.  I'll not go into the details, but we want to hide the ghost by setting "visible" to False and adding 1 to the global score.

```
def ghost_found(ghost):
    global score
    ghost["visible"] = False
    score = score + 1
    return
```

7.  Try running the game now.  Clicking ghost should increase the score.  

![Spooky House Step 9 Screen Shot](/screenshots/step09.png?raw=true "Step 9 Scores")


### Step 10  Lives

In step the last 9 steps we have added most of the code for the game, but we are still lacking one thing...  The ability to lose.  In this step we will add lives and give the game a challenge.  For our game we are going lose a life each time a ghost hides its self.

1. So we need to render the lives the player has.  We could just render a number, similar to the score, but lets do something cooler.  Time for a new function. We are going to draw the lives from the right hand side of the screen in.  First we need the width of the skull we are using for each life.

```
def render_lives():
    skull_width = skull_image.get_rect().width
```

2. Next we will set a local variable called life to the number of lives the player has.  We will use this to count backwards to zero.

```
    life = lives
```   

3. We will add a loop, that subtracts 1 from the life variable whilst it is bigger than zero.

```   
    while(life > 0):
```

4. We can now calculate the screen x position to draw the skull and then use this to blit it to the screen.

```
        skull_x = screen_width - (skull_width + 10) * (life)
        screen.blit(skull_image, (skull_x, 5))
```

5. Last of all at the end of the loop we will subtract 1 from life at the end of the loop.
```
        life = life - 1
    return
```

6.  The complete function should look like this.

```
def render_lives():
    "Draw a skull for each life"
    skull_width = skull_image.get_rect().width
    life = lives
    while(life > 0):
        skull_x = screen_width - (skull_width + 10) * (life)
        screen.blit(skull_image, (skull_x, 5))
        life = life - 1
    return
```

7. Functions are no good unless they get called.  Add this to the game loop under the ```render_score()``` function call.  Try running the game.  If all is good you should see 3 skulls draw at the top right of the screen.

8. Next we will update the ```update_ghosts()``` function.  Add lives to global import statement and subtract 1 from lives each time we set a ghost["visible] = False.  You can see the updated code below.

```
def update_ghosts():
    global hide_ghost_at, show_ghost_at, lives
    "Update the ghost states"

    # if the hide time is in the past, hide the ghosts
    if hide_ghost_at < pygame.time.get_ticks():
        for ghost in ghosts:
            if ghost["visible"] == True:
                ghost["visible"] = False
                show_ghost_at = randomShowTime()
                lives = lives - 1

    # check to see if all ghosts are hidden
    if(all(ghost["visible"] == False for ghost in ghosts)):
        # if show_ghost_at is in the past, show a ghost
        if show_ghost_at < pygame.time.get_ticks():
            ghost_to_turn_on = randint(0, len(ghosts) - 1)
            ghosts[ghost_to_turn_on]["visible"] = True
            hide_ghost_at = randomHideTime()

    return
```

9.  Try running the game.  As long as you click the ghost in time, your lives should remain.  Try not clicking a ghost to see the lives run down.  Let them run down to zero.  As you can see the game as problem.  You can still continue playing with no lives.  We will fix that in the next step.

### Step 11 Game Over

The plan for game over is as follows, add a variable that we will set to True when the lives reach zero.  If this variable if True, we will render a message in the center of screen to let the player know.

1.  Add the following near the ```running = True``` statement.

```
game_over = False
```

2.  Next we will add a function to render the game over message.  We've done similar for the title, but in this case we only want to render the message if ```game_over``` is ```True``` 

```
def render_game_over():
    "Draw the game over"

    if game_over:
        # draw title text to a surface
        surface = large_font.render("Game Over", True, (255, 255, 255))
        # calculate the x postion to center text
        screen_x = (screen_width - surface.get_width()) / 2
        # draw to screen
        screen.blit(surface, (screen_x, 300))
    return
```

3. Next, we need to check the number of lives.  If its zero or less, then we set ```game_over``` to ```False```.  Add the following check in the game loop, near the ```update_ghosts()``` call.

```
    if lives < 1:
        game_over = True
```

4. Last of all, we only need to update the ghosts if we are playing.  Use an if statement to do that in the game loop.

```
    # Update ghosts
    if game_over == False:
        update_ghosts()
```

## Other things to try


Make the game harder as the score increases
Audio and Sound effects
Animation
Different Game Assets



