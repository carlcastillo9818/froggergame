"""
     Pygame frogger game (1.9 build)

    TODO:
    Finish the start menu screen.
    Fill text files with credits to all those artists I mentioned.
    Adding frog sounds (optional)
    Check collisions between the frog and the goal posts AGAIN (just to be safe).
    Check the water blocks at the very top row because currently the frog can still land on them without drowning.
    Adjust the size of the lives and score counters at the top left if you think they are too small.
    Move all tilesets and spritesheets into the new folder I created just for those files.

    7-15-21 Started working on a start menu or title screen before the game starts.  Still need to do the following tasks
    listed above in the TODO list.

    7-10-21 Tuned the collision between the frog, the dragonfly, and each goal post. Added tilesets for water blocks,
    grass blocks, and road blocks. Placed the new blocks into the game and they look good.
     Credits to StremArt for the grass tileset, credits to TearofTheStar for the water
    tileset.  I added background music to the game (credits to Kevin MacLeod). I also added
     text files to give credits to all those artists I mentioned, it is located in the game folder.
    For next time, consider adding frog sounds (optional), check the
    collisions between the frog and the goal posts AGAIN (just to be safe), also check the water blocks at the very top
    row because currently the frog can still land on them without drowning.  Adjust the size of the lives and score
    counters at the top left if you think they are too small.  Move all tilesets and spritesheets into the new
    folder I created just for those files.  The last thing to add would be a start menu
    or title screen before the game starts, check google for that.

    7-8-21 Focus on fine tuning the collision between the frog, the dragonfly, and each goal post.  Make sure high scores
    get updated and lives get updated correctly.  After all that is finished then you can focus on implementing sound
    and MAYBE a start menu but its not necessary for this project.

    6-??-21 Next time, work on making the dragonfly move from goalpost to goalpost so that the player has to be careful when
    moving their frog to the goals.  If the frog succeeds in getting the dragonfly, the players high score should go up.
    If the frog misses the dragonfly, they will fall into the goalpost (frog home) and be reset to the starting position
    , and if they are out of lives then its GAME OVER!

    6-22-21 Added code for if log goes off screen, frog goes back to starting position and loses a life.
    Also added code for if log goes off screen and frog has 1 life, then it goes to game over screen.  Made the water
    dangerous for the frog to land in and if the frog does touch it then it drowns, loses a life, and if it has 1 life
    left then it results in a game over when that life is removed.  Added one static dragonfly (non moving for now).
    (CREDITS TO ELTHEN FOR THE DRAGONFLY IMAGE AND CREDITS TO KAUZZ FOR THE CAVE ROCKS IMAGES)

    6-20-21 ADDED SEVERAL MOVING LOGS IN THE WATER FOR FROG TO JUMP ONTO AND NAVIGATE ACROSS TO THE GOAL.  ALSO
    I CREATED A NEW CLASS CALLED RIVERLOG SO I COULD MAKE LOG OBJECTS TO ADD TO A LIST OF LOGS BELOW. ADDED A SPRITE SHEET
    TO BE USED FOR THE LOGS CALLED RPG NATURE TILESET (CREDITS TO STEALTHIX FOR MAKING THE TILESET, YOUR ART IS GREAT.)

    6-6-21 Fixed lives system so it doesnt
    go into the negative values.  It will just be a game over when it reaches 0.
    Added a game over screen!  Added a music file to the folder of the game so implement that
    when you can. (Finished all this)

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
import os
import pygame, sys
from Frog import *
from Automobile import *
from RiverLog import *
from frogHome import *
from random import *
from RectBackground import *
from gameColors import *
from RockTerrain import *
from dragonFly import *

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
More specifically, it checks for which enemies need to go left and which need to go right.  It adjusts enemy attributes 
like color, speed, x position along the way. It also adjusts river log attributes like their direction and speed.  
Then it checks wall boundaries and finally it updates the movable sprites list.
'''
def update_game_objects(screen, SCREEN_WIDTH, playableCharacter, movableSpritesList, enemySpritesList, riverLogSpritesList, insectToEat, goalPosts):
    # --- Game logic should go in this function

    '''Next time, work on making the dragonfly move from goalpost to goalpost so that the player has to be careful when
    moving their frog to the goals.  If the frog succeeds in getting the dragonfly, the players high score should go up
    by a bonus amount in addition to reaching the goal posts which also raises the high score. If the frog misses the dragonfly,
    they can still earn points by reaching one of the goalposts (frog home) and be reset to the starting position
    , and if they are out of lives then its GAME OVER!'''

    # check for collision between frog and dragonfly
    insectToEat.teleportAround() # call the method to make the insect move to each goal post
    if playableCharacter.getYPos() == insectToEat.getYPos():  # check if the frogs y position is equal to the dragonfly y position (at the same y coordinate level)
        pixels = 20  # number of pixels to add to the players x position or the logs x position
        if (insectToEat.getXPos() < playableCharacter.getXPos() < (
                insectToEat.getXPos() + pixels)) or (
                insectToEat.getXPos() < (playableCharacter.getXPos() + pixels) < (
                insectToEat.getXPos() + pixels)):
            playableCharacter.bonusHighScore() # give a bonus high score to the frog (in addition to their regular high score)
            playableCharacter.setXPos(300)  # move the frog back to its default position
            playableCharacter.setYPos(840)


    # check for collision between frog and each goal post
    for index,goal in enumerate(goalPosts):
        pixels = 10  # number of pixels to add to the players x position or the goals x position
        if playableCharacter.getYPos() == goal.getYPos():  # check if the frogs y position is equal to the caves y position (at the same y coordinate level)
            if (goal.getXPos() < playableCharacter.getXPos() < (goal.getXPos() + pixels)) or (
                    goal.getXPos() < (playableCharacter.getXPos() + pixels) < (goal.getXPos() + pixels)):
                playableCharacter.increaseHighScore() # increase the frogs high score
                playableCharacter.setXPos(300)  # move the frog back to its default position
                playableCharacter.setYPos(840)

    # check for collision between frog and moving river logs
    for index,log in enumerate(riverLogSpritesList):
        pixels = 100 # number of pixels to add to the players x position or the logs x position
        if playableCharacter.getYPos() == log.getYPos():  # check if the frogs y position is equal to the logs y position (at the same y coordinate level)
            if (playableCharacter.getXPos() > log.getXPos() and playableCharacter.getXPos() < (log.getXPos() + pixels)) or ((playableCharacter.getXPos() + pixels) > log.getXPos() and (playableCharacter.getXPos() + pixels) < (log.getXPos() + pixels)):
                playableCharacter.setXPos(log.getXPos()) # set frogs x pos to the logs x pos
                if log.getXPos() > 690 or log.getXPos() < -55: # as soon as log leaves the screen (the left or right sides)
                    playableCharacter.setXPos(300) # move the frog back to its default position
                    playableCharacter.setYPos(840)
                    if playableCharacter.getFrogLivesCount() > 0: # as long as the frog has more than 0 lives
                        playableCharacter.decreaseFrogLives() # Frog loses a life
                    else: # frog has no more lives
                        endScreen(screen) # call the game over screen function
            else:
                '''Frog isnt on a log which means it must be touching the water blocks near the log, so reset frogs position'''
                playableCharacter.setXPos(300)  # reset frogs position to the starting position at the beginning of the game
                playableCharacter.setYPos(840)
                if playableCharacter.getFrogLivesCount() > 0:  # as long as the frog has more than 0 lives
                    playableCharacter.decreaseFrogLives()  # Frog loses a life
                else:  # frog has no more lives
                    endScreen(screen)  # call the game over screen function

        if index % 2 != 0:  # check if the index / 2 remainder is NOT 0, if true then every ODD index or water log should come from the right side of the screen and MOVE LEFT
            log.moveLeft()  # make the log move to the left
            if log.getXPos() < -100:  # check if the logs x position is less than the left side of the screen (0 or any neg value)
                # randint and choice come from the random library but you dont need to include the word random in front because I imported * from random
                log.changeSpeed(randint(3,4)) #adjust speed
                log.setXPos(700)   # set x position of the river log to come before the right side of the screen
        else:  # remainder is 0 so logs will come from the left side of the screen, hence they will move RIGHT
            log.moveRight()  # make the river log move to the right
            if log.getXPos() > SCREEN_WIDTH:  # check if the river logs x position is greater than the right side of the screen
                log.changeSpeed(randint(3, 4))  # adjust speed
                log.setXPos(-50)  # set x position of the log to come before the left side of the screen


    for index, car in enumerate(enemySpritesList):  # enumerate gets the index with the element as you iterate through the list of automobiles
        if index % 2 != 0:  # check if the index / 2 remainder is NOT 0, if true then every ODD index or vehicle should come from the right side of the screen and MOVE LEFT
            car.moveLeft()  # make the car drive to the left
            if car.rect.x < -100:  # check if the cars x position is less than the left side of the screen (0 or any neg value)
                # randint and choice come from the random library but you dont need to include the word random in front because I imported * from random
                car.changeSpeed(randint(6, 8)) #adjust speed
                car.repaint() # make the car a different color each time it passes the screen to make it look like a new car is coming
                car.setXPos(800)   # set x position of the car to come before the right side of the screen
        else:  # remainder is 0 so cars will come from the left side of the screen, hence they will move RIGHT
            car.moveRight()  # make the car drive to the right
            if car.rect.x > SCREEN_WIDTH:  # check if the cars x position is greater than the right side of the screen
                car.changeSpeed(randint(6, 8)) # adjust speed
                car.repaint()  # make the car a different color each time it passes the screen to make it look like a new car is coming
                car.setXPos(-50)   # set x position of the car to come before the left side of the screen

        pixels = 51 # number of pixels to add to the players x position or the cars x position
        # collision using x and y coordinates
        if playableCharacter.getYPos() == car.getYPos():  # check if the frogs y position is equal to the cars y position (at the same y coordinate level)
            if (car.getXPos() < playableCharacter.getXPos() < (car.getXPos() + pixels)) or (
                    car.getXPos() < (playableCharacter.getXPos() + pixels) < (car.getXPos() + pixels)):
                '''Check if the frogs x position is greater than the cars x position (meaning part of the frog is to the right)
                AND that the frogs x position is also less than the cars x position plus some 
                pixels (meaning part of the frog is to the left but INSIDE of the car so that means collision occurs).
                The other condition to check is if the frogs x position plus some pixels is GREATER than the cars x position
                (meaning part of the frog is to the right) AND the frogs x position plus some pixels is LESS than the cars x position plus some pixels
                (meaning that part of the frog is to the left but INSIDE of the car so that means collision occurs)'''
                playableCharacter.setXPos(300)  # reset frogs position to the starting position at the beginning of the game
                playableCharacter.setYPos(840)
                playableCharacter.decreaseFrogLives()  # decrease the frogs lives after its been hit

    if playableCharacter.getXPos() < 0 and playableCharacter.getYPos() > 400:  # left wall boundary prevents frog from leaving the screen in the grass and road portion of the level only
        playableCharacter.setXPos(0)
    if playableCharacter.getXPos() > 640 and playableCharacter.getYPos() > 400:  # right wall boundary prevents frog from leaving the screen in the grass and road portion of the level only
        playableCharacter.setXPos(640)
    if playableCharacter.getYPos() > 840:  # bottom boundary
        playableCharacter.setYPos(840)
    if playableCharacter.getYPos() < 0:  # top boundary
        playableCharacter.setYPos(0)

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

    # --- Drawing code should go in this function
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
This function creates road blocks using a tileset and all the road blocks are placed
in several rows and columns which are determined by the x coordinates and y coordinates of the blocks.
'''
def makeRoads(screen, x_pos, y_pos, color, width, height, road_list,num_of_objs):  # creates each background object FOR THIS SPECIFIC GAME (frogger)
    original_y_coord = y_pos # holds original y coordinate for the respective road block

    for i in range(11): # the total number of iterations in which pairs of road blocks will be created (1 = 2 road blocks, 2 = 4 road blocks, etc)
        for x in range(num_of_objs): # create two road blocks every iteration of this loop
            road_list.append(RectBackground(screen, color, width, height, x_pos,y_pos, "road"))  # add each road block to the road list
            y_pos -= 60  # get ready to place the next block above the previous block (the result will be a pair of blocks)
        y_pos = original_y_coord # reset the y coordinate to what it was when the function was first called (different for each set of road blocks!)
        x_pos += 65 # update the x coordinate to the right

'''
This function features a start screen menu in a loop. This game loop checks if the user hits the start button,
if so, then it will let them start the game. If they hit the quit button, 
it will end the game and close the game window. '''
def startMenu(screen):
    # new game loop
    run = True  # Used in the game loop below, true until the user clicks the close button or escape key.
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # if user closes the window by pressing RED X button
                run = False
                sys.exit()  # stops the program so surface cannot be changed after quitting
                break
            if event.type == pygame.KEYDOWN:  # if the user presses down on a key
                if event.key == pygame.K_n:  # Pressing the n Key will quit the game
                    run = False
                    sys.exit()  # stops the program so surface cannot be changed after quitting
                    break
                elif event.key == pygame.K_y:  # Pressing the y key will reset the game
                    main()  # call the main method to run again (acts like the game was reset after a game over!)
                    break
        screen.fill(BLACK)  # clears the old screen and allows new things to be drawn
        displayStartScreenText(screen)  # call the method to display a game over screen
        pygame.display.update()  # updates the ENTIRE screen (no args were passed)

"""This function provides the text to be displayed in the start menu screen.
The title of the game, the start text, and quit text will be displayed on the screen!"""
def displayStartScreenText(screen):
    backgroundImg = pygame.image.load("images/frogbg.jpg") # background image loaded into the start screen
    screen.blit(backgroundImg, (0, 0)) # draw background to the screen

    font = pygame.font.Font("fonts/VarelaRound-Regular.ttf", 100)  # set type of font and the font size

    gameTitle = font.render("FROGGER", True, WHITE) # displays game title
    titleRectangle = pygame.draw.rect(screen, BLACK, pygame.Rect(100, 100, 500, 110), 0) # draw rectangle box behind start text

    startMessage = font.render("Start", True, WHITE)  # displays start text
    startRectangle = pygame.draw.rect(screen, BLACK, pygame.Rect(200, 300, 250, 110), 0) # draw rectangle box behind start text

    quitMessage = font.render("Quit", True, WHITE)  # displays start text
    quitRectangle = pygame.draw.rect(screen, BLACK, pygame.Rect(200, 500, 250, 110), 0) # draw rectangle box behind start text

    screen.blit(startMessage, (210, 300))  # draw the start msg to the screen
    screen.blit(quitMessage, (210, 500)) # draw the quit msg to the screen
    screen.blit(gameTitle, (100,100)) # draw the game title to the screen

'''
This function features a game over screen in a loop. This game loop checks if the user hits the continue button,
if so, then it will let them play again. If they hit the quit button, 
it will end the game and close the game window.'''
def endScreen(screen):
    pygame.mixer.music.stop() # stop the music
    # new game loop
    run = True # Used in the game loop below, true until the user clicks the close button or escape key.

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # if user closes the window by pressing RED X button
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
        displayEndScreenText(screen) # call the method to display a game over screen
        pygame.display.update() # updates the ENTIRE screen (no args were passed)

"""This function provides the text to be displayed in the game over screen.
A game over and continue text prompts will be rendered and blitted to the screen!"""
def displayEndScreenText(screen):
    font = pygame.font.Font("fonts/VarelaRound-Regular.ttf", 100)  # set type of font and the font size
    gameOverMessage = font.render("Game Over!", True, WHITE)  # display that the game is over

    font2 = pygame.font.Font("fonts/VarelaRound-Regular.ttf", 50)  # set type of font and the font size
    continueMessage = font2.render("Continue? (Y/N)", True, WHITE)  # display continue msg

    sprite_sheet = SpriteSheet("images/GreenFrog.png") # sprite sheet to retrieve the frog image from
    scaletuple = (80, 80)  # set scaling width and height for the frog img
    frogimage = sprite_sheet.get_image(0, 0, 24, 15, WHITE)  # create starting image the frog starts with
    frogimage = pygame.transform.scale(frogimage, scaletuple)  # scale the image to be bigger in game over screen

    screen.blit(gameOverMessage, (100, 300))  # draw the game over msg to the screen
    screen.blit(continueMessage, (150, 400))  # draw the game over msg to the screen
    screen.blit(frogimage, (310,200)) # draw the frog image to the screen above the game over message

'''
This function creates grass blocks using tileset and it places them on several
rows and columns which are determined by the x and y coordinates.
'''
def createGrassBlocks(screen, screenWidth, grassList, grass_x_coord, grass_y_coord):
    for x in range(11):
        grassList.append(RectBackground(screen, GREEN, screenWidth, 60, grass_x_coord, grass_y_coord,"grass"))  # add each block to this list
        grass_x_coord += 65  # update the x coordinate for next block

'''
This function creates water blocks using tileset and it places them on several
rows and columns which are determined by the x and y coordinates.
'''
def createWaterBlocks(screen, screenWidth, waterList, water_x_coord, water_y_coord):
    # run nested loops to build the water blocks (remember there are several rows and columns!)
    for x in range(7):
        for x in range(11):
            waterList.append(RectBackground(screen, BLUE, screenWidth, 420, water_x_coord,water_y_coord, "water")) # add each block to the list
            water_x_coord += 65 # update x coordinate for next block
        water_x_coord = 0 # reset the x coordinate when moving to the next row of blocks
        water_y_coord += 60 # update the y coordinate when starting the next row of blocks


'''
This function allows for background music to be loaded in and played during the main game
infinitely.
'''
def playFroggerMusic():
    '''
    If you have music or atmospheric sound effects you want to play in your game's background,
    you can use the music function of Pygame's mixer module. In your setup section, load the music file:
    The -1 value tells Pygame to loop the music file infinitely. You can set it to
    anything from 0 and beyond to define how many times the music should loop before stopping.'''
    pygame.mixer.music.load("sounds/pixelland.mp3")
    pygame.mixer.music.play(-1)


def main():
    SCREEN_HEIGHT = 900  # Set the width and height of the screen [width, height]
    SCREEN_WIDTH = 700

    # setup pygame and screen size and caption below
    pygame.init()
    pygame.mixer.init()

    size = (SCREEN_WIDTH, SCREEN_HEIGHT)  # create a size var holding screen width and height
    screen = pygame.display.set_mode(size)  # intialize the screen
    pygame.display.set_caption("My Frogger Game")  # set a title for the game window

    startMenu(screen) # call the start menu screen function

    # background = pygame.image.load("backgroundForGame(V2).png") # my custom background for my game

    # EXCLUDE THIS, I DECIDED TO MAKE MY OWN BACKGROUND 3/1/21 create custom background object (the background of the game)
    # gameBackground = Background('backgroundForGame(MadebyMe)V1.png', [0,0])

    # call the play music function
    playFroggerMusic()

    all_sprites_list = pygame.sprite.Group()  # This will be a list that will contain all the character sprites for the game.
    all_background_locations = pygame.sprite.Group()  # This will be a list that will contain all the roads, grass fields, and rivers for the game
    all_enemy_automobiles = pygame.sprite.Group()  # This will be a list that will contain all the ENEMY automobile sprites for the game.
    all_riverLogs = pygame.sprite.Group() # A list that contains all the river objects (logs) for the game
    all_goalPosts = pygame.sprite.Group()   # A list that contains all the goal related objects (caves/rocks) for the game

    # create your main character object (a frog in this case!)
    playerFrog = Frog(DARK_GREEN, 300,850, 60,60)  # set frogs color,x,y positions, width,height, (in that order). Y pos has to be 840 because its the y coordinate OF THE TOP LEFT PIXEL of the character!

    # create dragonfly object (this will be the object that gets eaten by the frog to build their high score!!!)
    dragonFly = DragonFly(50,50,150,0)

    # create automobile objects (width, height, speed, x pos, y pos, direction of car image)
    car1 = Automobile(80, 60, randint(6, 7), -100, 780, "Right")
    car2 = Automobile(80, 60, randint(6, 7), 700, 720, "Left")
    car3 = Automobile(80, 60, randint(6, 7), -100, 600, "Right")
    car4 = Automobile(80, 60, randint(6, 7), 700, 540, "Left")
    car5 = Automobile(80, 60, randint(6,7), -100, 480, "Right")

    # create moving log objects (width, height, speed, x pos, y pos, direction of log img)
    log1 = RiverLog(80,80,randint(3,4),100,360, "Right")
    log2 = RiverLog(80,80,randint(3,4), 700, 300, "Left")
    log3 = RiverLog(80,80,randint(3,4), 100, 240, "Right")
    log4 = RiverLog(80,80,randint(3,4), 700, 180, "Left")
    log5 = RiverLog(80,80,randint(3,4), 700, 120, "Right")
    log6 = RiverLog(80, 80, randint(3, 4), 700, 60, "Left")

    #make multiple road objects (surface, xpos, ypos, color, width, height, background list, number of objects)
    roadList = []
    makeRoads(screen, 0, 780, BLACK, SCREEN_WIDTH, 60, roadList, 2)
    makeRoads(screen, 0, 600, BLACK, SCREEN_WIDTH, 60, roadList, 3)

    grass1 = [] # list of grass blocks in the first row (the one on the bottom)
    grass2 = [] # second row grass blocks
    grass3 = [] # third row  grass blocks
    createGrassBlocks(screen, SCREEN_WIDTH, grass1, 0, 840) # call function to make each tileset grass block
    createGrassBlocks(screen, SCREEN_WIDTH, grass2, 0, 660) # args -> screen, screenWidth, grassList,x_coord, y_coord
    createGrassBlocks(screen, SCREEN_WIDTH, grass3, 0, 420)

    water1 = [] # list of water blocks
    createWaterBlocks(screen, SCREEN_WIDTH, water1, 0, 0) # call func to make waterblock, args -> screen, screenWidth, waterList, water_x_coord, water_y_coord

    # goal platforms (cave-like objects where the frog needs to go to collect flies to build a high score)
    goalspot1 = FrogHome(screen, 400,400,150,0) # pass args : surface, width, height, x , y
    goalspot2 = FrogHome(screen, 400, 400, 265,0)
    goalspot3 = FrogHome(screen, 400, 400, 380, 0)
    goalspot4 = FrogHome(screen, 400, 400, 495, 0)

    # rock terrain objects (will be located near the goal spots)
    rock1 = RockTerrain(screen, 400,400,205,0) # pass args : surface, width, height, x , y
    rock2 = RockTerrain(screen, 400,400,320,0)
    rock3 = RockTerrain(screen, 400,400,435,0)

    # add all objects to the correct lists here
    all_sprites_list.add(car1, car2, car3, car4, car5,log1,log2, log3, log4,log5,log6,playerFrog,dragonFly)  # add all moving game objects to the list of game sprites
    all_enemy_automobiles.add(car1, car2, car3, car4,car5)  # add the cars to the list of automobiles
    all_background_locations.add(grass1, grass2, grass3, water1,roadList, goalspot1, goalspot2,goalspot3, goalspot4,rock1,rock2, rock3)  # add grass and water objects to background locations list '''
    all_riverLogs.add(log1, log2,log3,log4,log5,log6) # add log objects to the list of river logs
    all_goalPosts.add(goalspot1,goalspot2, goalspot3,goalspot4) # add all the goal objects to the goal list

    # Used in the main game Loop, false until the user clicks the close button or escape key.
    done = False

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    # a font for the on screen text (two parameters -> filename (a .ttf font file), font size)
    font = pygame.font.Font("fonts/VarelaRound-Regular.ttf", 15)

    # -------- Main Program Loop -----------
    while not done:
        done = process_game_events(playerFrog, done) # process game events (like the frog moving)
        update_game_objects(screen, SCREEN_WIDTH, playerFrog, all_sprites_list, all_enemy_automobiles, all_riverLogs, dragonFly, all_goalPosts) # update the screen and game objects
        draw_game_objects(screen, all_sprites_list, all_background_locations) # draw game objects to the screen

        #fps = font.render(str(int(clock.get_fps())), True, pygame.Color('white'))  # render fps counter
        livesShown = font.render("Lives : " + str(playerFrog.getFrogLivesCount()), True, BLACK,WHITE)  # render lives counter
        scoreShown = font.render("High Score : " + str(playerFrog.getFrogHighScore()), True, BLACK, WHITE) # render score counter

        if playerFrog.getFrogLivesCount() <= 0: # players lives are 0 or less than 0
            endScreen(screen) # change screens to the game over screen

        #screen.blit(fps, (50, 50))  # draw the fps counter to the screen
        screen.blit(livesShown, (0,0))  # draw the lives counter to the screen
        screen.blit(scoreShown, (0,40))

        pygame.display.update()  # update entire screen

        # --- Limit to 60 frames per second
        clock.tick(30) # changed this to 6 to test out collision on 5-22-21, make sure to change it back to 60 when possible
    # Close the window and quit.
    pygame.quit()
main()
