
"""
     Pygame frogger game (1.1 build)

    3/1/21 LAST THING YOU WORKED ON WAS ROADMARKS (THE YELLOW MARKS ON THE ROADS)

    2/28/21 NEXT TIME, WORK ON THE COLLISION DETECTION BETWEEN EACH CAR AND FROG,
     ADD ROADS, ADD BETTER SPACING BETWEEN EVERY SPRITE, FIND OR MAKE YOUR OWN CAR SPRITES, AND FIND A WAY TO ADD
     SOUNDS (FOR THE CAR, OR BACKGROUND MUSIC, OR FROG SOUNDS), AND ADD A POINT SYSTEM TO KEEP TRACK OF PLAYER SCORE,
     AND MAKE YOUR OWN BACKGROUND WITH ROADS AND DIRT AND GRASS AND WATER...THATS IT FOR NOW LOL.

     ALSO RUN THE GAME NEXT TIME TO SEE YOUR PROGRESS BEFORE MAKING ANY CHANGES
"""
import pygame
from Frog import *
from Background import *
from Automobile import *
from random import *
from RectBackground import *

# Define some colors (constants)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
ORANGE = (255, 165, 0)
BLUE = (0,0,255)
YELLOW = (255,255,0)
PURPLE = (255,0,255)
RED = (255,0,0)
DARK_GREEN = (0,100,0)
colorList = (RED, BLUE, GREEN, ORANGE, YELLOW, PURPLE) # these colors will be randomly picked from to generate different car colors

# setup
pygame.init()

# Set the width and height of the screen [width, height]
SCREEN_HEIGHT = 500
SCREEN_WIDTH = 700
size = (SCREEN_WIDTH, SCREEN_HEIGHT)

screen = pygame.display.set_mode(size) # intialize the screen object
pygame.display.set_caption("My Frogger Game") # set a title for the game window

all_sprites_list = pygame.sprite.Group() # This will be a list that will contain all the character sprites we intend to use in our game.
all_background_locations = pygame.sprite.Group() # This will be a list that will contain all the roads, grass fields, and rivers we need for our game
all_enemy_automobiles = pygame.sprite.Group() # This will be a list that will contain all the ENEMY automobile sprites we intend to use in our game.


# create your main character object (a frog in this case!)
playerFrog = Frog(DARK_GREEN, 30,30) # set frogs color,width,height
playerFrog.setXPos(300) # set x,y positions
playerFrog.setYPos(470) # y has to be 470 because its the y coordinate OF THE TOP LEFT PIXEL of the character!


# speed var for the automobiles!
speed = 5
#create an automobile object
car1 = Automobile(ORANGE, 80, 60, randint(20, 30))
car1.rect.x = -100
car1.rect.y = 380
car2 = Automobile(PURPLE, 80, 60, randint(20, 30))
car2.rect.x = -100
car2.rect.y = 200
car3 = Automobile(GREEN, 80, 60, randint(20, 30))
car3.rect.x = -100
car3.rect.y = 100

# create custom background object (the background of the game) EXCLUDE THIS, I DECIDED TO MAKE MY OWN BACKGROUND 3/1/21
#gameBackground = Background('backgroundForGame(MadebyMe)V1.png', [0,0])


# make a RectBackground object (in this case its a long patch of grass)
grass1 = RectBackground(screen, GREEN, SCREEN_WIDTH,60)
grass1.rect.x = 0
grass1.rect.y = 440

# make a RectBackground object (in this case its a road)
road1 = RectBackground(screen, BLACK, SCREEN_WIDTH,60)
road1.rect.x = 0
road1.rect.y = 380

# Add the frog to the list of objects
all_sprites_list.add(playerFrog)
# add the cars to the list of objects
all_sprites_list.add(car1)
all_sprites_list.add(car2)
all_sprites_list.add(car3)
all_background_locations.add(grass1) # add  grass to background locations list (sprite list)
all_background_locations.add(road1) # add road to background locations list (sprite list)

x_pos = 30 # initial x pos value for yellow road marks
y_pos = 405 # initial y pos value for yellow road marks
for x in range(10): # Run a for loop to create multiple yellow mark background rect objects
    # make a RectBackground object (this is the yellow marks that go on the road)
    roadmarks = RectBackground(screen, YELLOW, 30, 10)
    roadmarks.rect.x = x_pos
    roadmarks.rect.y = y_pos
    all_background_locations.add(roadmarks) # store each road mark in this list
    x_pos += 100 # update the x pos for the next yellow road marks

all_enemy_automobiles.add(car1) # add the car to the list of automobiles
all_enemy_automobiles.add(car2) # add the car to the list of automobiles
all_enemy_automobiles.add(car3) # add the car to the list of automobiles


# Loop until the user clicks the close button.
done = False
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:  # Pressing the x Key will quit the game
                done = True

    keys = pygame.key.get_pressed() # KEEP ALL THESE K MOVEMENTS INSIDE THE ELIF SO CHARACTER MOVES NON-CONTINOUSLY OTHERWISE IGNORE THIS
    if keys[pygame.K_LEFT]:
        playerFrog.moveLeft(5)
    elif keys[pygame.K_RIGHT]: # using elif makes it so if a user presses left and right, game only processes the last direction pressed
        playerFrog.moveRight(5)
    elif keys[pygame.K_UP]:
        playerFrog.moveUp(5)
    elif keys[pygame.K_DOWN]:
        playerFrog.moveDown(5)
    # place keys under the for loop instead if you want CONTINUOUS MOVEMENT LIKE ASTEROIDS OR MARIO


    # --- Game logic should go here
    # Game Logic
    for car in all_enemy_automobiles:
        car.moveRight(speed)
        if(car.rect.x > SCREEN_WIDTH):
            car.changeSpeed(randint(20,30)) # randint and choice come from the random library but you dont need to include the word random in front because I imported * from random
            car.repaint(choice(colorList))
            car.rect.x = -50

    if(playerFrog.rect.x < 0): # left wall boundary
        playerFrog.rect.x = 0
    if(playerFrog.rect.x > 670): # right wall boundary
        playerFrog.rect.x = 670
    if(playerFrog.rect.y > 470): # bottom boundary
        playerFrog.rect.y = 470
    if(playerFrog.rect.y < 0): # top boundary
        playerFrog.rect.y = 0

    ''' event handlers for moving frog using arrow keys above ^^^.'''

    all_sprites_list.update() # update the sprites in the list (this list gets updated because the sprites in here all move around)
    # because all the enemy cars are in this list, you dont need to update the other list (which has the same cars)

    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(WHITE)

    # CUSTOM BACKGROUND screen.blit(gameBackground.image, gameBackground.rect)


    # --- Drawing code should go here

    all_background_locations.draw(screen) # draw all background locations (grass, road, water) in one go.

    # Now let's draw all the sprites in one go. (the ones from the sprites list will go above background)
    all_sprites_list.draw(screen)

    '''
     note from 2/18:  DO NOT ADD your background to the sprites list
    BECAUSE when the draw method is called above, it will draw your
    frog to the screen AS WELL AS the background so your background will
    end up covering the frog and you wont know unless your frog is
    a different color besides green. I tested it and removed the background
    from the sprites list in an earlier part of the program.  If you want to
    see what happens then add it back to the sprites list, it will cause
    issues so be careful.  Keep the background separate from the sprites list
    which should only hold the sprites that will be above the background
    '''

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()