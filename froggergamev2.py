"""
     Pygame frogger game (1.3 build)

    TODO LIST:
    1. ADD MOVING LOGS IN THE WATER FOR FROG TO JUMP ONTO AND NAVIGATE ACROSS TO THE GOAL
    2. ADD SOMETHING TO THE GOAL LIKE A FLAG OR A FRUIT OR SOMETHING FOR THE FROG TO TOUCH AND END THE GAME
    3. FIND A WAY TO ADD SOUNDS (FOR THE CAR, OR BACKGROUND MUSIC, OR FROG SOUNDS)


    6-6-21 Work on adjusting lives system so it doesnt
    go into the negative values.  It will just be a game over when it reaches 0.
    Added a game over screen!  Added a music file to the folder of the game so implement that
    when you can.

    6-6-21 Implemented working collision between all cars and the frog finally!

    5-18-21 Working on the points/lives system (I went with lives)

    5/4/21 - MADE SCREEN TALLER AND WIDER AND THEN ADJUSTED EVERYTHING TO SCALE! I ADDED ANOTHER ROAD AND ANOTHER GRASS SECTION.
    I ADDED A GOAL SPOT AT THE TOP (CURRENTLY PURPLE).


     4/24/21 Took a break from this project since I did so much earlier this month.  Still working on fixing
     animations for the frog so thaht when it moves left and right, the animations loop smoothly and the frog
     doesnt get stuck on one sprite image.

    4/10/21 CHANGE HOW THE FROG MOVES (USE TIME DELAY FROM SAMPLEMOVEMENT2 TO HELP YOU AS REFERENCE) (Finished this!)

    4/9/21 started working on making frog sprite pictures update BLOCK BY BLOCK.  run the program to see.

    
    4/9/21 I put a hold on the collision detection.  Instead I started working on making the frog
    move as if its moving along an invisible grid.  It still moves continously in any direction
    BUT now it moves as if its moving BLOCK BY BLOCK.  Run the samplemovement2 python file
    to see an example of the block by block movement.

    4/6/21 Started working on collision detection between frog and car1 and car2

    4/6/21 Optimized the repaint function so its shorter than before but still produces same result.  Also added an FPS counter
    to track fps drops.

    4/5/21 Succeeded in ADDING THE REST OF THE DIFFERENT COLOR CAR SPRITE IMAGES SO EACH TIME A NEW CAR COMES OUT OF THE LEFT
    OR RIGHT WALL THEN ITS A DIFFERENT COLORED CAR SPRITE! I MOVED ON FROM USING THE SIMPLE RECTANGLE SHAPES!

    3/27/21  Added another water rectangle to the game, added up/down animations for the frog, added INITIAL car image for each car.


    3/21/21 Added water rectangle, another car, and another road to the game!


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

    3/17/21 REPLACED GREEN BLOCK WITH A FROG SPRITE that I FOUND online!  Added animations to Frog Character only (for now!)


 3/9/21 WROTE A FUNCTION TO HANDLE CREATION OF ROADS AND ANOTHER FUNCTION TO HANDLE CREATION OF ROAD MARKS SEPARATELY!

3/2/21 ADDED ANOTHER ROAD AND MORE ROADMARKS.  FIND A WAY TO MAKE THE PROCESS OF CREATING THEM EASIER! THEN MOVE ON
TO THE OBJECTIVES BELOW.

    3/1/21 LAST THING YOU WORKED ON WAS ROADMARKS (THE YELLOW MARKS ON THE ROADS)


    2/28/21 NEXT TIME, WORK ON THE COLLISION DETECTION BETWEEN EACH CAR AND FROG,
     ADD ROADS, ADD BETTER SPACING BETWEEN EVERY SPRITE, FIND OR MAKE YOUR OWN CAR SPRITES, AND FIND A WAY TO ADD
     SOUNDS (FOR THE CAR, OR BACKGROUND MUSIC, OR FROG SOUNDS), AND ADD A POINT SYSTEM TO KEEP TRACK OF PLAYER SCORE,
     AND MAKE YOUR OWN BACKGROUND WITH ROADS AND DIRT AND GRASS AND WATER...THATS IT FOR NOW LOL.

     ALSO RUN THE GAME NEXT TIME TO SEE YOUR PROGRESS BEFORE MAKING ANY CHANGES
"""
import pygame, sys
from Frog import *
from Automobile import *
from random import *
from RectBackground import *
from gameColors import *

# dont need this anymore -> from Background import *


'''
This function process input keys pressed by the player (moving the frog in different directions for instance).
It runs a for loop that runs when events occur like pressing keys down, releasing keys.  Pressing the escape key
will allow the game to end.  If any arrow keys are pressed and released then the playable characters will stop moving.
After the for loop, a collection of key movements are stored and if a key is pressed then the playable character will 
move left,right,up,or down.  The function returns a boolean var that will end the game if the game is exitted or the player
presses the escape key, otherwise it will continue running the game as long as it is false.
'''
def process_game_events(playableCharacter, endTheGame):
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            endTheGame = True
        elif event.type == pygame.KEYDOWN:  # if the key is held down
            if event.key == pygame.K_ESCAPE:  # Pressing the escape Key will quit the game
                endTheGame = True
        elif event.type == pygame.KEYUP:  # if the key is released
            if event.key == pygame.K_LEFT and playableCharacter.change_x < 0:  # check if the left arrow key is pressed and released AND check if the frogs speed is less than 0
                playableCharacter.stop()  # make the frog stop moving (This sets its speed to 0 so its resting)
            if event.key == pygame.K_RIGHT and playableCharacter.change_x > 0:  # check if the right arrow key is pressed and released AND check if the frogs speed is greater than 0
                playableCharacter.stop()  # make the frog stop moving (This sets its speed to 0 so its resting)
            if event.key == pygame.K_UP and playableCharacter.change_y < 0:
                playableCharacter.stop()
            if event.key == pygame.K_DOWN and playableCharacter.change_y > 0:
                playableCharacter.stop()

    keys = pygame.key.get_pressed()  # KEEP ALL THESE Key MOVEMENTS INSIDE THE ELIF SO CHARACTER MOVES NON-CONTINOUSLY OTHERWISE IGNORE THIS
    if keys[pygame.K_LEFT]:
        print("You went left by " + str(playableCharacter.change_x))  # shows how many times you are moving the character to the left (testing)
        playableCharacter.moveLeft()
    elif keys[pygame.K_RIGHT]:  # using elif makes it so if a user presses left and right, game only processes the last direction pressed
        print("You went right by " + str(playableCharacter.change_x))  # shows how many times you are moving the character to the right (testing)
        playableCharacter.moveRight()
    elif keys[pygame.K_UP]:
        print("You went up by " + str(playableCharacter.change_y))  # shows how many times you are moving the character to the left (testing)
        playableCharacter.moveUp()
    elif keys[pygame.K_DOWN]:
        print("You went down by " + str(playableCharacter.change_y))  # shows how many times you are moving the character to the left (testing)
        playableCharacter.moveDown()
    # event handlers for moving frog using arrow keys above ^^^
    # place keys under the for loop instead if you want CONTINUOUS MOVEMENT LIKE ASTEROIDS OR MARIO

    return endTheGame


'''
This function updates all objects that need to be updated, e.g. position changes, physics, all that other stuff.
More specifically, it runs a for loop that goes through the enemy sprites list, checks for which enemies need to go
left and which need to go right.  It adjusts enemy attributes like color, speed, x position along the way.  
Then it checks wall boundaries and finally it updates the movable sprites list.
'''
def update_game_objects(screen, SCREEN_WIDTH, playableCharacter, movableSpritesList, enemySpritesList):
    # --- Game logic should go here
    for index, car in enumerate(enemySpritesList):  # enumerate gets the index with the element as you iterate through the list of automobiles
        if (index % 2 != 0):  # check if the index / 2 remainder is NOT 0, if true then every ODD index or vehicle should come from the right side of the screen and MOVE LEFT
            car.moveLeft()  # make the car drive to the left
            if (car.rect.x < -100):  # check if the cars x position is less than the left side of the screen (0 or any neg value)
                # randint and choice come from the random library but you dont need to include the word random in front because I imported * from random
                car.changeSpeed(randint(6, 8))
                car.repaint() # make the car a different color each time it passes the screen to make it look like a new car is coming
                car.setXPos(800)   # set x position of the car to come before the right side of the screen
        else:  # remainder is 0 so cars will come from the left side of the screen, hence they will move RIGHT
            car.moveRight()  # make the car drive to the right
            if (car.rect.x > SCREEN_WIDTH):  # check if the cars x position is greater than the right side of the screen
                car.changeSpeed(randint(6, 8))
                car.repaint()  # make the car a different color each time it passes the screen to make it look like a new car is coming
                car.setXPos(-50)   # set x position of the car to come before the left side of the screen

        pixels = 51 # number of pixels to add to the players x position or the cars x position
        # collision using x and y coordinates (works better compared to the old one)
        if (playableCharacter.getYPos() == car.getYPos()):  # check if the frogs y position is equal to the cars y position (at the same y coordinate level)
            if ((playableCharacter.getXPos() > car.getXPos() and playableCharacter.getXPos() < (car.getXPos() + pixels)) or ((playableCharacter.getXPos() + pixels) > car.getXPos() and (playableCharacter.getXPos() + pixels) < (car.getXPos() + pixels))):
                '''Check if the frogs x position is greater than the cars x position (meaning part of the frog is to the right)
                AND that the frogs x position is also less than the cars x position plus some 
                pixels (meaning part of the frog is to the left but INSIDE of the car so that means collision occurs).
                The other condition to check is if the frogs x position plus some pixels is GREATER than the cars x position
                (meaning part of the frog is to the right) AND the frogs x position plus some pixels is LESS than the cars x position plus some pixels
                (meaning that part of the frog is to the left but INSIDE of the car so that means collision occurs)'''
                print("Players X position is " + str(playableCharacter.getXPos()) + " and car " + str(index) + " x position is " + str(car.getXPos()))
                playableCharacter.setXPos(300)  # reset frogs position to the starting position at the beginning of the game
                playableCharacter.setYPos(840)
                playableCharacter.decreaseFrogLives()  # decrease the frogs lives after its been hit

    if (playableCharacter.rect.x < 0):  # left wall boundary
        playableCharacter.rect.x = 0
    if (playableCharacter.rect.x > 640):  # right wall boundary
        playableCharacter.rect.x = 640
    if (playableCharacter.rect.y > 840):  # bottom boundary
        playableCharacter.rect.y = 840
    if (playableCharacter.rect.y < 0):  # top boundary
        playableCharacter.rect.y = 0

    movableSpritesList.update()  # update the sprites in the list (this list gets updated because the sprites in here all move around)
    # because all the enemy cars are in this list, you dont need to update the other list (which has the same cars)

    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(WHITE)

    # blit the CUSTOM BACKGROUND
    # screen.blit(backgroundimg, (0, 0))


'''
This function draws background objects to the screen, movable sprites to the screen, and then
updates the entire screen with whats been drawn.  
'''
def draw_game_objects(screen, movableSpritesList, backgroundObjectsList):  # render things on screen

    # --- Drawing code should go here
    backgroundObjectsList.draw(screen)
    # Let's draw all the sprites in one go. (the ones from the sprites list will go above background)
    movableSpritesList.draw(screen)

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

    # --- Go ahead and update the ENTIRE screen with what we've drawn.
    pygame.display.flip()


'''
This function runs a for loop that creates background road objects (black roads and yellow road marks for example),
stores them in a list, and depending on the color argument, it changes x and y positions accordingly
'''
def makeRoads(screen, x_pos, y_pos, color, width, height, bg_list,num_of_objs):  # creates each background object FOR THIS SPECIFIC GAME (frogger)
    for x in range(num_of_objs):
        background_obj = RectBackground(screen, color, width, height, x_pos,y_pos)  # set surface, color, width, height, x pos, y pos
        bg_list.add(background_obj)
        if (color == BLACK):  # black will always be associated with background object that is a ROAD
            y_pos -= 60  # adjust black rectangles as necessary
        elif (color == YELLOW):  # yellow will always be associated with background object that is a ROAD MARK
            x_pos += 100  # adjust yellow rectangles as necessary

'''
This function has a new game loop. This game loop checks if the user hits a certain button,
if so, then it will bring them to a new game. If they hit another certain button, 
it will end the game and close the game window.'''
def endScreen(screen):
    # new game loop
    run = True # Used in the secondary game Loop, true until the user clicks the close button or escape key.

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                sys.exit()  # stops the program so surface cannot be changed after quitting
                break
            if event.type == pygame.KEYDOWN:  # if the user presses down on a key
                if event.key == pygame.K_n:  # Pressing the n Key will quit the game
                    run = False
                    sys.exit() # stops the program so surface cannot be changed after quitting
                    break
                elif event.key == pygame.K_y: # Pressing the y key will reset the game
                    main() # call the main method to run again (acts like the game was reset after a game over!)
                    break
        screen.fill(BLACK) # clears the old screen and allows new things to be drawn


        displayEndScreenText(screen)

        pygame.display.update() # updates the entire screen (no args were passed)

"""This function provides the text to be displayed in the game over screen.
A game over and continue text prompts will be rendered and blitted to the screen!"""
def displayEndScreenText(screen):
    font = pygame.font.Font("VarelaRound-Regular.ttf", 100)  # set type of font and the font size
    gameOverMessage = font.render("Game Over!", True, WHITE)  # display that the game is over

    font2 = pygame.font.Font("VarelaRound-Regular.ttf", 50)  # set type of font and the font size
    continueMessage = font2.render("Continue? (Y/N)", True, WHITE)  # display continue msg

    sprite_sheet = SpriteSheet("GreenFrog.png") # sprite sheet to retrieve the frog image from
    scaletuple = (80, 80)  # set scaling width and height for the frog img
    frogimage = sprite_sheet.get_image(0, 0, 24, 15, WHITE)  # create starting image the frog starts with
    frogimage = pygame.transform.scale(frogimage, scaletuple)  # scale the image to be bigger in game over screen

    screen.blit(gameOverMessage, (100, 300))  # draw the game over msg to the screen
    screen.blit(continueMessage, (150, 400))  # draw the game over msg to the screen
    screen.blit(frogimage, (310,200)) # draw the frog image to the screen above the game over message

def main():
    SCREEN_HEIGHT = 900  # Set the width and height of the screen [width, height]
    SCREEN_WIDTH = 700

    # setup pygame and screen size and caption below
    pygame.init()
    size = (SCREEN_WIDTH, SCREEN_HEIGHT)  # create a size var holding screen width and height
    screen = pygame.display.set_mode(size)  # intialize the screen
    pygame.display.set_caption("My Frogger Game")  # set a title for the game window

    # background = pygame.image.load("backgroundForGame(V2).png") # my custom background for my game

    # EXCLUDE THIS, I DECIDED TO MAKE MY OWN BACKGROUND 3/1/21 create custom background object (the background of the game)
    # gameBackground = Background('backgroundForGame(MadebyMe)V1.png', [0,0])

    all_sprites_list = pygame.sprite.Group()  # This will be a list that will contain all the character sprites we intend to use in our game.
    all_background_locations = pygame.sprite.Group()  # This will be a list that will contain all the roads, grass fields, and rivers we need for our game
    all_enemy_automobiles = pygame.sprite.Group()  # This will be a list that will contain all the ENEMY automobile sprites we intend to use in our game.

    # create your main character object (a frog in this case!)
    playerFrog = Frog(DARK_GREEN, 300,840, 60,60)  # set frogs color,x,y positions, width,height, (in that order). Y pos has to be 440 because its the y coordinate OF THE TOP LEFT PIXEL of the character!
    print(playerFrog.rect.x)
    print(playerFrog.rect.y)

    # create automobile objects (width, height, speed, x pos, y pos, direction of car image)
    car1 = Automobile(80, 60, randint(6, 7), -100, 780, "Right")
    car2 = Automobile(80, 60, randint(6, 7), 700, 720, "Left")
    car3 = Automobile(80, 60, randint(6, 7), -100, 600, "Right")
    car4 = Automobile(80, 60, randint(6, 7), 700, 540, "Left")
    car5 = Automobile(80, 60, randint(6,7), -100, 480, "Right")


    # make multiple road objects (surface, xpos, ypos, color, width, height, background list, number of objects)
    makeRoads(screen, 0, 780, BLACK, SCREEN_WIDTH, 60, all_background_locations, 2)
    makeRoads(screen, 30, 805, YELLOW, 30, 10, all_background_locations, 7)
    makeRoads(screen, 30, 750, YELLOW, 30, 10, all_background_locations, 7)
    makeRoads(screen, 0, 600, BLACK, SCREEN_WIDTH, 60, all_background_locations, 2)
    makeRoads(screen, 30, 625, YELLOW, 30, 10, all_background_locations, 7)
    makeRoads(screen, 30, 565, YELLOW, 30, 10, all_background_locations, 7)
    makeRoads(screen, 0, 480, BLACK, SCREEN_WIDTH, 60, all_background_locations, 1)
    makeRoads(screen, 30, 505, YELLOW, 30, 10, all_background_locations, 7)


    # grass rectangles -> pass args:  surface, color, width, height, x pos, y pos
    grass1 = RectBackground(screen, GREEN, SCREEN_WIDTH, 60, 0, 840)
    grass2 = RectBackground(screen, GREEN, SCREEN_WIDTH, 60, 0, 660)
    grass3 = RectBackground(screen, GREEN, SCREEN_WIDTH, 60, 0, 420)

    # water rectangle -> pass args:  surface, color, width, height, x pos, y pos
    water1 = RectBackground(screen, BLUE, SCREEN_WIDTH, 420, 0, 0)

    # goal rectangle (where the frog needs to go to end the game and win!!!!
    goalspot = RectBackground(screen, PURPLE, SCREEN_WIDTH / 2,60,175,0)

    # add all objects to the correct lists here
    all_sprites_list.add(playerFrog, car1, car2, car3, car4, car5)  # add all game sprites to the list of game sprites
    all_enemy_automobiles.add(car1, car2, car3, car4,car5)  # add the cars to the list of automobiles
    all_background_locations.add( grass1, grass2, grass3, water1,goalspot)  # add grass and water objects to background locations list '''

    # Used in the main game Loop, false until the user clicks the close button or escape key.
    done = False

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    # a font for the on screen text (two parameters -> filename (a .ttf font file), font size)
    font = pygame.font.Font("VarelaRound-Regular.ttf", 30)

    # -------- Main Program Loop -----------
    while not done:
        done = process_game_events(playerFrog, done) # process game events (like the frog moving)
        update_game_objects(screen, SCREEN_WIDTH, playerFrog, all_sprites_list, all_enemy_automobiles) # update the screen and game objects
        draw_game_objects(screen, all_sprites_list, all_background_locations) # draw game objects to the screen

        fps = font.render(str(int(clock.get_fps())), True, pygame.Color('white'))  # render fps counter
        livesShown = font.render("Lives : " + str(playerFrog.getFrogLivesCount()), True, BLACK,WHITE)  # render lives counter

        if(playerFrog.getFrogLivesCount() <= 0): # players lives are 0 or less than 0
            endScreen(screen) # change screens to the game over screen

        screen.blit(fps, (50, 50))  # draw the fps counter to the screen
        screen.blit(livesShown, (0,0))  # draw the lives counter to the screen

        pygame.display.update()  # update entire screen



        # --- Limit to 60 frames per second
        clock.tick(60) # changed this to 6 to test out collision on 5-22-21, make sure to change it back to 60 when possible
    # Close the window and quit.
    pygame.quit()
main()
