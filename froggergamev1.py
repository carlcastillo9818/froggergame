
"""
     Pygame frogger game (1.1 build)

3/2/21 ADDED ANOTHER ROAD AND MORE ROADMARKS.  FIND A WAY TO MAKE THE PROCESS OF CREATING THEM EASIER! THEN MOVE ON
TO THE OBJECTIVES BELOW.

    3/1/21 LAST THING YOU WORKED ON WAS ROADMARKS (THE YELLOW MARKS ON THE ROADS)

    2/28/21 NEXT TIME, WORK ON THE COLLISION DETECTION BETWEEN EACH CAR AND FROG,
     ADD ROADS, ADD BETTER SPACING BETWEEN EVERY SPRITE, FIND OR MAKE YOUR OWN CAR SPRITES, AND FIND A WAY TO ADD
     SOUNDS (FOR THE CAR, OR BACKGROUND MUSIC, OR FROG SOUNDS), AND ADD A POINT SYSTEM TO KEEP TRACK OF PLAYER SCORE,
     AND MAKE YOUR OWN BACKGROUND WITH ROADS AND DIRT AND GRASS AND WATER...THATS IT FOR NOW LOL.

     ALSO RUN THE GAME NEXT TIME TO SEE YOUR PROGRESS BEFORE MAKING ANY CHANGES
"""
import pygame
from Frog import *
# dont need this anymore -> from Background import *
from Automobile import *
from random import *
from RectBackground import *

# Define constants (colors, speed, etc.)
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
SPEED = 5  # speed var for the automobiles!

# setup below
pygame.init()

# Set the width and height of the screen [width, height]
SCREEN_HEIGHT = 500
SCREEN_WIDTH = 700
size = (SCREEN_WIDTH, SCREEN_HEIGHT)

screen = pygame.display.set_mode(size) # intialize the screen
pygame.display.set_caption("My Frogger Game") # set a title for the game window
# create custom background object (the background of the game) EXCLUDE THIS, I DECIDED TO MAKE MY OWN BACKGROUND 3/1/21
#gameBackground = Background('backgroundForGame(MadebyMe)V1.png', [0,0])

all_sprites_list = pygame.sprite.Group() # This will be a list that will contain all the character sprites we intend to use in our game.
all_background_locations = pygame.sprite.Group() # This will be a list that will contain all the roads, grass fields, and rivers we need for our game
all_enemy_automobiles = pygame.sprite.Group() # This will be a list that will contain all the ENEMY automobile sprites we intend to use in our game.

# create your main character object (a frog in this case!)
playerFrog = Frog(DARK_GREEN, 30,30, 300, 470) # set frogs color,width,height, x,y positions (in that order). Y pos has to be 470 because its the y coordinate OF THE TOP LEFT PIXEL of the character!

#create automobile objects
car1 = Automobile(ORANGE, 80, 60, randint(20, 30), -100, 380)
car2 = Automobile(PURPLE, 80, 60, randint(20, 30), -100, 320)
car3 = Automobile(GREEN, 80, 60, randint(20, 30), -100, 100)

# make RectBackground objects
grass1 = RectBackground(screen, GREEN, SCREEN_WIDTH,60, 0, 440) #set surface, color, width, height, x pos, y pos

all_sprites_list.add(playerFrog)# Add the frog to the list of sprites
all_sprites_list.add(car1) # add the cars to the list of sprites
all_sprites_list.add(car2)
all_sprites_list.add(car3)
all_enemy_automobiles.add(car1) # add the car to the list of automobiles
all_enemy_automobiles.add(car2) # add the car to the list of automobiles
all_enemy_automobiles.add(car3) # add the car to the list of automobiles
all_background_locations.add(grass1) # add  grass to background locations list (sprite list)

road_x_pos = 0 # x position for road rectangle
road_y_pos = 380 # y position for road rectangle
for x in range(2):
    road = RectBackground(screen, BLACK, SCREEN_WIDTH, 60, road_x_pos , road_y_pos) #set surface, color, width, height, x pos, y pos
    all_background_locations.add(road)
    road_y_pos -= 60

roadmark_x_pos = 30 # initial x pos value for yellow road marks
roadmark_y_pos = 405 # initial y pos value for yellow road marks
for x in range(10): # Run a for loop to create multiple yellow mark background rect objects
    roadmarks = RectBackground(screen, YELLOW, 30, 10, roadmark_x_pos,roadmark_y_pos) # make a RectBackground object (this is the yellow marks that go on the road).  Set surface, color, width, height, x pos, y pos
    all_background_locations.add(roadmarks) # store each road mark in this list
    roadmark_x_pos += 100 # update the x pos for the next yellow road marks

roadmark_x_pos = 30 # initial x pos value for yellow road marks
roadmark_y_pos = 350 # initial y pos value for yellow road marks
for x in range(10): # Run a for loop to create multiple yellow mark background rect objects
    roadmarks = RectBackground(screen, YELLOW, 30, 10, roadmark_x_pos,roadmark_y_pos) # make a RectBackground object (this is the yellow marks that go on the road).  Set surface, color, width, height, x pos, y pos
    all_background_locations.add(roadmarks) # store each road mark in this list
    roadmark_x_pos += 100 # update the x pos for the next yellow road marks

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

    for car in all_enemy_automobiles:
        car.moveRight(SPEED)
        if(car.rect.x > SCREEN_WIDTH):
            car.changeSpeed(randint(20,30)) # randint and choice come from the random library but you dont need to include the word random in front because I imported * from random
            car.repaint(choice(colorList)) # make the car a different color each time it passes the screen to make it look like a new car is coming
            car.setXPos(-50) # set x position of the car to come before the left side of the screen

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