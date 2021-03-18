
"""
     Pygame frogger game (1.3 build)

    3/18/21 I added the frogs walking left and walking right animations into the game!
    I still have to add another road, add more cars, then add a little pond at the top of the level.
    Also I still have to add UP and DOWN frog animations into the game (Use sprite sheet)
    (make it a generic blue color for now).  Also I still have to add a scoreboard at the top.
    Perhaps I can also add custom sprites for the automobiles too.

    For my NEXT GAME, I will make the character from scratch (my own custom sprites).  For this game, I will
    borrow the Frog sprites from the game Tomba to finish this project faster.


    3/18/21 I eliminated the speed parameter for the vehicles moving left or right because the formula looked
    too complex for what I'm trying to do.  I also eliminated the SPEED constant in my main program as a result.
    I went into the Automobile class and changed self.speed to self.change_x because its more clear that way
    that the variable is changing the SPEED of the X vector (left and right).  I adjusted the moveleft,moveright,
    and changespeed methods as needed.


    3/17/21 I added a frog sprite image to my game for my frog character.  Now go to this link
    http://programarcadegames.com/python_examples/en/sprite_sheets/ and look at how the dev
    creates walking animations for his character then do something similar to that.  Use lists,
    image property, and appending to the list to make two lists (one for moving left "animations" and one for moving
    right "animations")
    Use the frog sprite sheet from  here https://www.spriters-resource.com/fullview/145236/
    Also add another road, add more cars, then add a little pond at the top of the level
    (make it a generic blue color for now)

    3/17/21 REPLACE GREEN BLOCK WITH A FROG SPRITE that you will find online!  Add animations to Frog Character only (for now!)


 3/9/21 WRITE A FUNCTION TO HANDLE CREATION OF ROADS AND ANOTHER FUNCTION TO HANDLE CREATION OF ROAD MARKS SEPARATELY!

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
from Automobile import *
from random import *
from RectBackground import *


# dont need this anymore -> from Background import *

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
colorList = (RED, BLUE, GREEN, ORANGE, YELLOW, PURPLE, WHITE) # colors are randomly picked to generate different car colors
SCREEN_HEIGHT = 500  # Set the width and height of the screen [width, height]
SCREEN_WIDTH = 700

def process_game_events(playerFrog, done): # process input and other stuff
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN: # if the key is held down
            if event.key == pygame.K_ESCAPE:  # Pressing the escape Key will quit the game
                done = True
        elif event.type == pygame.KEYUP: # if the key is released
            if event.key == pygame.K_LEFT and playerFrog.change_x < 0: # check if the left arrow key is pressed and released AND check if the frogs speed is less than 0
                playerFrog.stop() # make the frog stop moving (This sets its speed to 0 so its resting)
            if event.key == pygame.K_RIGHT and playerFrog.change_x > 0: # check if the right arrow key is pressed and released AND check if the frogs speed is greater than 0
                playerFrog.stop() # make the frog stop moving (This sets its speed to 0 so its resting)
    keys = pygame.key.get_pressed()  # KEEP ALL THESE K MOVEMENTS INSIDE THE ELIF SO CHARACTER MOVES NON-CONTINOUSLY OTHERWISE IGNORE THIS
    if keys[pygame.K_LEFT]:
        print("You went left by " + str(playerFrog.change_x))  # shows how many times you are moving the character to the left (testing)
        playerFrog.moveLeft()
    elif keys[pygame.K_RIGHT]:  # using elif makes it so if a user presses left and right, game only processes the last direction pressed
        print("You went right by " + str(playerFrog.change_x)) # shows how many times you are moving the character to the right (testing)
        playerFrog.moveRight()
    elif keys[pygame.K_UP]:
        playerFrog.moveUp(4)
    elif keys[pygame.K_DOWN]:
        playerFrog.moveDown(4)

    # place keys under the for loop instead if you want CONTINUOUS MOVEMENT LIKE ASTEROIDS OR MARIO
    return done

# update all objects that need to be updated, e.g. position changes, physics, all that other stuff
def update_game_objects(screen, SCREEN_WIDTH, playerFrog, all_sprites_list, all_enemy_automobiles):
     # --- Game logic should go here
    for index, car in enumerate(all_enemy_automobiles): # enumerate gets the index with the element as you iterate through the list of automobiles
        if(index % 2 != 0): # check if the index / 2 remainder is NOT 0, if true then every ODD index or vehicle should come from the right side of the screen and MOVE LEFT
            car.moveLeft() # make the car drive to the left
            if(car.rect.x < -100): # check if the cars x position is less than the left side of the screen (0 or any neg value)
                # randint and choice come from the random library but you dont need to include the word random in front because I imported * from random
                car.changeSpeed(randint(6, 8))
                # make the car a different color each time it passes the screen to make it look like a new car is coming
                car.repaint(choice(colorList))
                # set x position of the car to come before the right side of the screen
                car.setXPos(800)

        else: # remainder is 0 so cars will come from the left side of the screen, hence they will move RIGHT
            car.moveRight() # make the car drive to the right
            if(car.rect.x > SCREEN_WIDTH): # check if the cars x position is greater than the right side of the screen
                # randint and choice come from the random library but you dont need to include the word random in front because I imported * from random
                car.changeSpeed(randint(6, 8))
                # make the car a different color each time it passes the screen to make it look like a new car is coming
                car.repaint(choice(colorList))
                # set x position of the car to come before the left side of the screen
                car.setXPos(-50)

    if(playerFrog.rect.x < 0):  # left wall boundary
        playerFrog.rect.x = 0
    if(playerFrog.rect.x > 640):  # right wall boundary
        playerFrog.rect.x = 640
    if(playerFrog.rect.y > 440):  # bottom boundary
        playerFrog.rect.y = 440
    if(playerFrog.rect.y < 0):  # top boundary
        playerFrog.rect.y = 0

    ''' event handlers for moving frog using arrow keys above ^^^.'''

    all_sprites_list.update()  # update the sprites in the list (this list gets updated because the sprites in here all move around)
    # because all the enemy cars are in this list, you dont need to update the other list (which has the same cars)

    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(WHITE)

    # CUSTOM BACKGROUND screen.blit(gameBackground.image, gameBackground.rect)

def draw_game_objects(screen, all_background_locations, all_sprites_list): #render things on screen

    # --- Drawing code should go here

    # draw all background locations (grass, road, water) in one go.
    all_background_locations.draw(screen)

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


def makeMultipleBackgroundObjects(screen, x_pos, y_pos, color, width,height, bg_list, num_of_objs): # creates each background object FOR THIS SPECIFIC GAME (frogger)
    for x in range(num_of_objs):
        background_obj = RectBackground(screen, color,width,height, x_pos, y_pos)# set surface, color, width, height, x pos, y pos
        bg_list.add(background_obj)
        if(color == BLACK): # black will always be associated with background object that is a ROAD
            y_pos -= 60 # adjust black rectangles as necessary
        elif(color == YELLOW): # yellow will always be associated with background object that is a ROAD MARK
            x_pos += 100 # adjust yellow rectangles as necessary


def main():
    # setup below
    pygame.init()

    size = (SCREEN_WIDTH, SCREEN_HEIGHT) # create a size var holding screen width and height
    screen = pygame.display.set_mode(size) # intialize the screen
    pygame.display.set_caption("My Frogger Game") # set a title for the game window


    # EXCLUDE THIS, I DECIDED TO MAKE MY OWN BACKGROUND 3/1/21 create custom background object (the background of the game)
    #gameBackground = Background('backgroundForGame(MadebyMe)V1.png', [0,0])

    all_sprites_list = pygame.sprite.Group() # This will be a list that will contain all the character sprites we intend to use in our game.
    all_background_locations = pygame.sprite.Group() # This will be a list that will contain all the roads, grass fields, and rivers we need for our game
    all_enemy_automobiles = pygame.sprite.Group() # This will be a list that will contain all the ENEMY automobile sprites we intend to use in our game.

    # create your main character object (a frog in this case!)
    playerFrog = Frog(DARK_GREEN, 300, 440) # set frogs color,x,y positions, width,height, (in that order). Y pos has to be 440 because its the y coordinate OF THE TOP LEFT PIXEL of the character!
    print(playerFrog.rect.x)
    print(playerFrog.rect.y)

    #create automobile objects (color, width, height, speed, x pos, y pos)
    car1 = Automobile(ORANGE, 80, 60, randint(6, 8), -100, 380)
    car2 = Automobile(PURPLE, 80, 60, randint(6, 8), 700, 320)
    car3 = Automobile(GREEN, 80, 60, randint(6, 8), -100, 200)

    # make multiple RectBackground objects (surface, xpos, ypos, color, width, height, background list, number of objects)
    makeMultipleBackgroundObjects(screen, 0, 380, BLACK, SCREEN_WIDTH, 60, all_background_locations, 2)
    makeMultipleBackgroundObjects(screen,30, 405, YELLOW, 30,10, all_background_locations, 10)
    makeMultipleBackgroundObjects(screen, 30, 350, YELLOW, 30, 10, all_background_locations, 10)
    makeMultipleBackgroundObjects(screen, 0, 200, BLACK, SCREEN_WIDTH, 60, all_background_locations, 1)
    makeMultipleBackgroundObjects(screen,30, 225, YELLOW, 30,10, all_background_locations, 10)
    # set surface, color, width, height, x pos, y pos of GRASS rectangle
    grass1 = RectBackground(screen, GREEN, SCREEN_WIDTH, 60, 0, 440)
    grass2 = RectBackground(screen, GREEN, SCREEN_WIDTH, 60, 0, 260)

    all_sprites_list.add(playerFrog,car1,car2,car3) # add all game sprites to the list of game sprites
    all_enemy_automobiles.add(car1,car2,car3) # add the cars to the list of automobiles
    all_background_locations.add(grass1, grass2) # add grass object to background locations list


    # Loop until the user clicks the close button.
    done = False
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    # -------- Main Program Loop -----------
    while not done:
        done = process_game_events(playerFrog, done)
        update_game_objects(screen, SCREEN_WIDTH, playerFrog, all_sprites_list, all_enemy_automobiles)
        draw_game_objects(screen, all_background_locations, all_sprites_list)
        # --- Limit to 60 frames per second
        clock.tick(60)

    # Close the window and quit.
    pygame.quit()
main()
