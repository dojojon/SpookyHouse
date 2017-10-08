# PyGame Halloween House 

We are going to learn how to program a "Spooky House" halloween game using Python and Pygame.

![Spooky House Screen Shot](/Game_Screen_Shot.png?raw=true "Spooky House")

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
The assets_low directory contains a set of assets from running the game at a lower screen resolution.  You will need to change screen resolution set up in step 1 and the `asset_path` variable added in step 3.  Details in the instructions

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
screen = pygame.display.set_mode((800, 600))
```

You can change the game resolution here.  The above code creates a screen 800 pixels wide by 600 pixels high.   If you want to run the low resolution version change the values as shown below.  

```
screen = pygame.display.set_mode((600, 480))
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



### Step 2
Write some text to the screen

### Step 3
Draw a sprite to the screen
    House
    Sky 

### Step 4
Read the ghost data

### Step 5
Draw all ghost

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



