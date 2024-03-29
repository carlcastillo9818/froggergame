"""
This program is a game that plays like the popular game "Frogger"
It involves the player (a frog) having to cross
through several streets of traffic (cars) and some paths of grass.  After surviving that, they have to
cross through a river full of logs that are moving along the water.  The frog can traverse using those logs
and reach several caves which are the destination goals.  Each cave rewards points and in addition there
is a dragonfly that moves very fast but if it is caught by the frog then bonus points are rewarded.
If the player loses all their lives, they can submit their score to the leaderboard and end the game or
restart it.

Note: If high score board becomes too full then simply go to the folder that has the game files
,look for highScores.txt and delete some names and scores from it.  Make a backup of the original
highScores.txt file in case you break the game by modifying it and want to restore it to working order.
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
It checks for events occurring like pressing keys down, releasing keys, etc. If any arrow keys are pressed 
and released then the playable characters will stop moving. In addition a collection of key movements are stored and 
if a key is pressed then the playable character can move in any direction.  The function returns a boolean var 
that will end the game if the game is exited or the player presses the escape key, 
otherwise it will continue running the game as long as it is false.
'''
def process_game_events(playableCharacter, endTheGame):
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # check if the game is exited
            endTheGame = True
        elif event.type == pygame.KEYDOWN:  # if a key is held down
            if event.key == pygame.K_ESCAPE:  # Pressing the escape Key will quit the game
                endTheGame = True
        elif event.type == pygame.KEYUP:  # if a key is released
            if event.key == pygame.K_LEFT and playableCharacter.change_x < 0:
                # check if the left arrow key is pressed and released AND if the frogs speed is less than 0
                playableCharacter.stop()  # make the frog stop moving
            if event.key == pygame.K_RIGHT and playableCharacter.change_x > 0:
                # check if the right arrow key is pressed and released AND if the frogs speed is greater than 0
                playableCharacter.stop()
            if event.key == pygame.K_UP and playableCharacter.change_y < 0:
                # check if the up arrow key is pressed and released AND  if the frogs speed is less than 0
                playableCharacter.stop()
            if event.key == pygame.K_DOWN and playableCharacter.change_y > 0:
                # check if the down arrow key is pressed and released AND if the frogs speed is greater than 0
                playableCharacter.stop()

    # KEEP ALL THESE KEY MOVEMENTS INSIDE THE ELIF SO CHARACTER MOVES NON-CONTINOUSLY OTHERWISE IGNORE THIS
    # using elif makes it so if a user presses left and right, game only processes the last direction pressed
    # place keys under the for loop instead if you want CONTINUOUS MOVEMENT LIKE ASTEROIDS OR MARIO

    # event handlers for moving frog using arrow keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        playableCharacter.moveLeft()
    elif keys[pygame.K_RIGHT]:
        playableCharacter.moveRight()
    elif keys[pygame.K_UP]:
        playableCharacter.moveUp()
    elif keys[pygame.K_DOWN]:
        playableCharacter.moveDown()
    return endTheGame # return flag var which can end the game if its value is True

# Continue at Line 166 Carlos! 9-9-21

'''
This function updates all objects that need to be updated, e.g. position changes, physics, all that other stuff.
More specifically, it checks for which enemies need to go left or right.  It adjusts enemy attributes 
like color, speed, and their position. It also adjusts river log attributes like their direction and speed.
It checks for collision between the frog and the following : cars, goal posts, water, left and right sides of the screen, 
and dragonfly. Finally it updates the movable sprites list.
'''
def update_game_objects(screen, SCREEN_WIDTH, playableCharacter, movableSpritesList, enemySpritesList, riverLogSpritesList, insectToEat, goalPosts):
    # --- Game logic should go in this function

    # check for collision between frog and dragonfly
    insectToEat.teleportAround() # call the method to make the insect move to each goal post
    if playableCharacter.getYPos() == insectToEat.getYPos():  # check if the frogs y position is equal to the dragonfly y position (at the same y coordinate level)
        pixels = 20  # number of pixels to add to the player or insect x pos
        if (insectToEat.getXPos() < playableCharacter.getXPos() < (
                insectToEat.getXPos() + pixels)) or (
                insectToEat.getXPos() < (playableCharacter.getXPos() + pixels) < (
                insectToEat.getXPos() + pixels)):
            playableCharacter.bonusHighScore() # give a bonus high score to the frog
            playableCharacter.setXPos(300)  # move the frog back to its default position
            playableCharacter.setYPos(840)

    # check for collision between frog and each goal post
    for index,goal in enumerate(goalPosts):
        leftPixels = 16  # number of left pixels (to be added to the x positions)
        rightPixels = 35 # number of right pixels (to be added to the x positions)
        if goal.getXPos() - leftPixels <= playableCharacter.getXPos() <= goal.getXPos() + rightPixels and playableCharacter.getYPos() == goal.getYPos():
            '''check if the frogs x position is in between the current goals x position and the x position + an amount of extra 
            pixels and they have the same y coordinate. Imagine a box within a bigger box so it makes more sense.'''
            playableCharacter.increaseHighScore() # increase the current score
            playableCharacter.setXPos(300)  # move the frog back to its default position
            playableCharacter.setYPos(840)

    for index,goal in enumerate(goalPosts):
        # check if the frog lands in the rocks or the first row of water (next to each goal post)
        if playableCharacter.getYPos() == goal.getYPos(): # frog and goal posts have same Y coordinate
            if 0 <= playableCharacter.getXPos() < 150: # frog is within the left side of the goal posts (the water)
                playableCharacter.decreaseFrogLives() # frog loses a life
                playableCharacter.setXPos(300)  # reset frogs position to its initial position
                playableCharacter.setYPos(840)
            elif 190 <= playableCharacter.getXPos() < 248: # frog hit the first rock
                playableCharacter.decreaseFrogLives()
                playableCharacter.setXPos(300)  # reset frogs position to its initial position
                playableCharacter.setYPos(840)
            elif 300 <= playableCharacter.getXPos() < 360: # frog hit the second rock
                playableCharacter.decreaseFrogLives()
                playableCharacter.setXPos(300)  # reset frogs position to its initial position
                playableCharacter.setYPos(840)
            elif 420 <= playableCharacter.getXPos() < 494: # frog hit the third rock
                playableCharacter.decreaseFrogLives()
                playableCharacter.setXPos(300)  # reset frogs position to its initial position
                playableCharacter.setYPos(840)
            elif 540 <= playableCharacter.getXPos() <= 700:# frog is within the right side of the goal posts (the Water)
                playableCharacter.decreaseFrogLives()
                playableCharacter.setXPos(300)  # reset frogs position to its initial position
                playableCharacter.setYPos(840)

    # check for collision between frog and moving river logs
    for index,log in enumerate(riverLogSpritesList):
        pixels = 50 # number of pixels to add to the players x position or the logs x position
        if playableCharacter.getYPos() == log.getYPos():  # check if the frogs y position is equal to the logs y position (at the same y coordinate level)
            if (log.getXPos() < playableCharacter.getXPos() < (log.getXPos() + pixels)) or (
                    log.getXPos() < (playableCharacter.getXPos() + pixels) < (log.getXPos() + pixels)):
                playableCharacter.setXPos(log.getXPos()) # set frogs x pos to the logs x pos
                if log.getXPos() > 690 or log.getXPos() < -55:
                    # as soon as log leaves the screen (the left or right sides)
                    playableCharacter.setXPos(300) # move the frog back to its default position
                    playableCharacter.setYPos(840)
                    if playableCharacter.getFrogLivesCount() > 0:
                        # as long as the frog has more than 0 lives
                        playableCharacter.decreaseFrogLives() # Frog loses a life
                    else:
                        # frog has no more lives
                        endScreen(screen) # call the game over screen function
            else:
                # Frog isnt on a log which means it must be touching the water blocks near the log, so reset frogs position
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
                log.changeSpeed(randint(2,3)) #adjust speed
                log.setXPos(700)   # set x position of the river log to come before the right side of the screen
        else:  # remainder is 0 so logs will come from the left side of the screen, hence they will move RIGHT
            log.moveRight()  # make the river log move to the right
            if log.getXPos() > SCREEN_WIDTH:  # check if the river logs x position is greater than the right side of the screen
                log.changeSpeed(randint(2, 3))  # adjust speed
                log.setXPos(-50)  # set x position of the log to come before the left side of the screen

    # enumerate gets the index with the element as you iterate through the list of automobiles
    for index, car in enumerate(enemySpritesList):
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

    # left wall boundary prevents frog from leaving the screen in the grass and road portion of the level only
    if playableCharacter.getXPos() < 0 and playableCharacter.getYPos() > 400:
        playableCharacter.setXPos(0)
    # right wall boundary prevents frog from leaving the screen in the grass and road portion of the level only
    if playableCharacter.getXPos() > 640 and playableCharacter.getYPos() > 400:
        playableCharacter.setXPos(640)
    if playableCharacter.getYPos() > 840:  # bottom boundary
        playableCharacter.setYPos(840)
    if playableCharacter.getYPos() < 0:  # top boundary
        playableCharacter.setYPos(0)


    movableSpritesList.update()  # update the sprites in the list (this list gets updated because the sprites in here all move around)
    # because all the enemy cars are in this list, you dont need to update the other list (which has the same vehicles)

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
    backgroundObjectsList.draw(screen)  # background objects come first
    # Let's draw all the sprites in one go. (the ones from the sprites list will go above background objects)
    movableSpritesList.draw(screen)
    '''note from 2/18:  DO NOT ADD your background to the sprites list
        BECAUSE when the draw method is called above, it will draw your
        frog to the screen AS WELL AS the background so your background will
        end up covering the frog and you wont know unless your frog is
        a different color besides green. I tested it and removed the background
        from the sprites list in an earlier part of the program.  If you want to
        see what happens then add it back to the sprites list, it will cause
        issues so be careful.  Keep the background separate from the sprites list
        which should only hold the sprites that will be above the background'''
    # --- Go ahead and update the ENTIRE screen with what we've drawn.
    pygame.display.flip()


'''
This function creates road blocks using a tileset and all the road blocks are placed
in several rows and columns which are determined by the x coordinates and y coordinates of the blocks.
'''
def makeRoads(screen, x_pos, y_pos, color, width, height, road_list,num_of_objs):
    original_y_coord = y_pos # holds original y coordinate for the respective road block
    for i in range(11): # the total number of iterations in which pairs of road blocks will be created (1 = 2 road blocks, 2 = 4 road blocks, etc)
        for x in range(num_of_objs): # create two road blocks every iteration of this loop (one on top and one on bottom)
            road_list.append(RectBackground(screen, color, width, height, x_pos,y_pos, "road"))  # add each road block to the road list
            y_pos -= 60  # get ready to place the next block above the previous block (the result will be a pair of blocks)
        y_pos = original_y_coord # reset the y coordinate to what it was when the function was first called (different for each set of road blocks!)
        x_pos += 65 # update the x coordinate to the right


'''
This function features a start screen menu in a loop. This game loop checks if the user hits the start button,
if so, then it will let them start the game. If they hit the quit button, 
it will end the game and close the game window. '''
def startMenu(screen):
    LEFT = 1 # This var represents left mouse button as a num value
    # start menu game loop
    run = True  # Used in the game loop below, true until the user clicks the close button or escape key.
    while run:
        mouseXPosition, mouseYPosition = pygame.mouse.get_pos() # retrieve x and y position of the mouse!!!
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # if user closes the window by pressing RED X button
                run = False
                sys.exit()  # stops the program so surface cannot be changed after quitting
            if event.type == pygame.MOUSEBUTTONDOWN: # checks if mouse button is being clicked
                if event.button == LEFT: # checks if the LEFT mouse button was clicked
                    if 170 <= mouseXPosition <= 541 and 280 <= mouseYPosition <= 385: # user is clicking within the START block
                        # start the main game loop (ends this loop and proceeds to the main game loop)
                        run = False
                    elif 170 <= mouseXPosition <= 542 and 480 <= mouseYPosition <= 586:# user is clicking within the QUIT block
                        # close the game
                        sys.exit()
        screen.fill(BLACK)  # clears the old screen and allows new things to be drawn
        displayStartScreenText(screen)  # call the method to display start screen text
        pygame.display.update()  # updates the ENTIRE screen (no args were passed)


"""This function provides the text to be displayed in the start menu screen.
The title of the game, the start text, and quit text will be displayed 
on the screen!"""
def displayStartScreenText(screen):
    backgroundImg = pygame.image.load("images/frogbg.jpg") # background image loaded into the start screen
    screen.blit(backgroundImg, (0, 0)) # draw background to the screen
    font = pygame.font.Font("fonts/press_start_2p/PressStart2P.ttf", 70)  # set type of font and the font size

    gameTitle = font.render("FROGGER", True, WHITE) # displays game title
    titleRectangle = pygame.draw.rect(screen, DARK_GREEN, pygame.Rect(100, 100, 500, 150), 0) # draw rectangle box behind title text

    startMessage = font.render("Start", True, WHITE)  # displays start text
    startRectangle = pygame.draw.rect(screen, BLACK, pygame.Rect(170, 280, 375, 110), 0) # draw rectangle box behind start text

    quitMessage = font.render("Quit", True, WHITE)  # displays start text
    quitRectangle = pygame.draw.rect(screen, BLACK, pygame.Rect(170, 480, 375, 110), 0) # draw rectangle box behind quit text

    screen.blit(startMessage, (190, 300))  # draw the start msg to the screen
    screen.blit(quitMessage, (205, 500)) # draw the quit msg to the screen
    screen.blit(gameTitle, (110,140)) # draw the game title to the screen


''' This function features a game over screen in a loop. This game loop checks if the user hits the continue button,
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
                break # exit loop
            if event.type == pygame.KEYDOWN:  # if the user presses down on a key
                if event.key == pygame.K_n:  # Pressing the n Key will quit the game
                    run = False
                    sys.exit() # stops the program so surface cannot be changed after quitting
                    break
                elif event.key == pygame.K_y: # Pressing the y key will reset the game
                    main() # call the main method to run again (acts like the game was reset after a game over!)
                    break
        screen.fill(BLACK) # clears the old screen and allows new things to be drawn
        displayEndScreenText(screen) # call the method to display a game over text
        pygame.display.update() # updates the ENTIRE screen (no args were passed)


"""This function provides the text to be displayed in the game over screen.
A game over and continue text prompts will be rendered and 
blitted to the screen!"""
def displayEndScreenText(screen):
    font = pygame.font.Font("fonts/press_start_2p/PressStart2P.ttf", 55)  # set type of font and the font size
    gameOverMessage = font.render("Game Over!", True, WHITE)  # display that the game is over

    font2 = pygame.font.Font("fonts/press_start_2p/PressStart2P.ttf", 30)  # set type of font and the font size
    continueMessage = font2.render("Continue? (Y/N)", True, WHITE)  # display continue msg

    sprite_sheet = SpriteSheet("images/GreenFrog.png") # sprite sheet to retrieve the frog image from
    scaletuple = (80, 80)  # set scaling width and height for the frog img
    frogimage = sprite_sheet.get_image(0, 0, 24, 15, WHITE)  # create starting image the frog starts with
    frogimage = pygame.transform.scale(frogimage, scaletuple)  # scale the image to be bigger in game over screen

    screen.blit(gameOverMessage, (100, 300))  # draw the game over msg to the screen
    screen.blit(continueMessage, (150, 400))  # draw the game over msg to the screen
    screen.blit(frogimage, (310,200)) # draw the frog image to the screen above the game over message


''' This function creates grass blocks using tileset and it places them on several
rows and columns which are determined by the x and y coordinates.
'''
def createGrassBlocks(screen, screenWidth, grassList, grass_x_coord, grass_y_coord):
    for x in range(11):
        grassList.append(RectBackground(screen, GREEN, screenWidth, 60, grass_x_coord, grass_y_coord,"grass"))  # add each block to this list
        grass_x_coord += 65  # update the x coordinate for next block


''' This function creates water blocks using tileset and it places them on several
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


'''This function allows for background music to be loaded in and played during the main game
infinitely.   If you have music or atmospheric sound effects you want to play in your game's background,
you can use the music function of Pygame's mixer module. In your setup section, load the music file:
The -1 value tells Pygame to loop the music file infinitely. You can set it to
anything from 0 and beyond to define how many times the music should loop before stopping. '''
def playFroggerMusic():
    pygame.mixer.music.load("sounds/pixelland.mp3") # load music
    pygame.mixer.music.play(-1) # play music infinitely


'''This function reads the high scores from the text file, sorts them, then returns the list 
to the displayHighScores function to be read and 
displayed on screen!!!'''
def readHighScoresFromFile():
    filename = "highScores.txt" # name of the file to read data from
    scores = [] # sorted list of scores and their matching user names

    # before reading all the contents in the file, make sure that all the names and their scores are SORTED
    # after sorting, read the contents and DISPLAY them to the screen

    with open(filename, "r") as inFile:  # open file in read mode
        for line in inFile: # go line by line in the file
            name, score = line.split(',') # splits the line into two variables with the comma as the separator value
            score = int(score) # converts the score to an integer so it can be sorted properly
            scores.append((name, score)) # add the name and score to the new list

    # sort the list with the key. The key tells the method to sort by the score in each TUPLE -> (name, score) in descending order!
    scores.sort(key=lambda s: s[1], reverse = True)

    return scores


'''This function displays a high score screen after the player runs out of lives and this
screen is displayed before the game over screen.  After reading the high scores text file, it displays 
several scores along with several names including the players name and the 
players score which were captured in the input name screen.'''
def displayHighScores(screen):
    allPlayersInfo = []# list variable that holds all the scores and names
    allPlayersInfo = readHighScoresFromFile() # call the function to read all the high scores with each player name from the score file

    # custom background for this screen
    bg = pygame.image.load("images/spacebackground.png")

    # label font object uses custom font and custom size for text labels
    labelFont = pygame.font.Font("fonts/press_start_2p/PressStart2P.ttf", 40)
    headerRect = pygame.Rect(0,0,240,100) # header rectangle
    highScoresHeader = labelFont.render("All High Scores", True, WHITE)    # high score header label

    # list of labels
    listOfPlayerLabels = []

    # secondary font which is used for the player name and scores being displayed
    labelFont2 = pygame.font.Font("fonts/press_start_2p/PressStart2P.ttf", 20)
    # several labels that each display a player name and player score from the file
    for name, score in allPlayersInfo: # loop through the list of tuples
        currentPlayerLabel = labelFont2.render(name + "          " + str(score), False, WHITE)
        listOfPlayerLabels.append(currentPlayerLabel) # add each label to the list

    # font object uses custom font and custom size for text labels
    labelFont3 = pygame.font.Font("fonts/press_start_2p/PressStart2P.ttf", 55)

    # create a rectangle for user to continue to the game over screen
    continueRect = pygame.Rect(100, 650, 500, 150)
    # this label tells the user to submit their name (and score)
    continueLabel = labelFont3.render("Continue", True, WHITE)

    # new game loop
    while True:
        for event in pygame.event.get():
            # if user types QUIT then the screen will close
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if continueRect.collidepoint(event.pos):  # detect mouse position over the rectangle
                    # when user clicks on the continue rectangle, take them to the game over screen!
                    endScreen(screen)

        screen.fill(BLACK) # set background color of screen
        screen.blit(bg, (0, 0))  # add custom background to the screen

        # draw continue button rectangle
        pygame.draw.rect(screen, BLUE, continueRect)

        # display a label to the screen that instructs the user to submit their name (and score)
        screen.blit(continueLabel, (120, 700))  # blit this label to the screen
        # display label to the screen that shows header text
        screen.blit(highScoresHeader, (75, 10))

        playerlabelXPos = 150
        playerlabelYPos = 75
        # blit and display each players name and score labels to the screen with the loop
        for player in listOfPlayerLabels:
            screen.blit(player, (playerlabelXPos, playerlabelYPos))
            playerlabelYPos += 20

        # display.flip() will update only a portion of the screen (not full area)
        pygame.display.flip()


''' This function saves the players high score and player name to a file of
high scores and the player names.'''
def savePersonalHighScore(screen, playerName, playerScore):
    filename = "highScores.txt" # name of the file to save data to

    # open the high scores file and APPEND the users name and the users score to the EXISTING file
    # You dont have to worry about closing it manually, the with keyword does that at the end automatically
    with open(filename, 'a') as outFile:
        # store the python data into a file
        outFile.write(playerName + ", " + str(playerScore))
        outFile.write("\n")
    displayHighScores(screen) # call the next function to display all high scores in a new screen


'''This function displays the personal score of the player after the game ends and allows
for the player to enter their custom name in a text box. '''
def inputHighScoreScreen(screen, playerFrog):
    # custom background for this screen
    bg = pygame.image.load("images/spacebackground.png")

    # basic font for user typed
    usertypingFont = pygame.font.Font("fonts/press_start_2p/PressStart2P.ttf", 100)
    user_text = '' # user text will be blank initially
    nameLimit = 2 # the users input text size cannot surpass this number (subscript size)

    # create rectangle for user to enter their name
    input_rect = pygame.Rect(200, 170, 240, 100)

    # create a rectangle for user to SUBMIT their name (score will also be submitted!)
    submitRect = pygame.Rect(240,400,240,100)

    labelFont = pygame.font.Font("fonts/press_start_2p/PressStart2P.ttf", 40)  # set type of font and the font size of the screen text labels
    submitLabel = labelFont.render("Submit", True, WHITE) # tells the user to submit their name (and score)

    labelFont2 = pygame.font.Font("fonts/press_start_2p/PressStart2P.ttf", 33)  # set type of font and the font size of the screen text labels
    userScoreLabel = labelFont2.render("Your High Score ", True, WHITE) # a prompt that displays a text above the high score

    labelFont3 = pygame.font.Font("fonts/press_start_2p/PressStart2P.ttf", 33)  # set type of font and the font size of the screen text labels
    userScoreLabel2 = labelFont3.render("was " + str(playerFrog.getFrogHighScore()), True, WHITE) # the actual players high score in label form

    labelFont4 = pygame.font.Font("fonts/press_start_2p/PressStart2P.ttf", 30)  # set type of font and the font size of the screen text labels
    enterYourNameLabel = labelFont4.render("Enter your name below", True, WHITE)  # tell the user to enter their name

    # new game loop
    while True:
        for event in pygame.event.get():
            # if user types QUIT then the screen will close
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if submitRect.collidepoint(event.pos): # detect mouse position over the rectangle
                    if len(user_text) == 0: # check length of text input
                        user_text = 'ABC'
                    # call the function to save users inputted name and their high score
                    savePersonalHighScore(screen, user_text, playerFrog.getFrogHighScore())

            if event.type == pygame.KEYDOWN: # user is pressing down some key on the keyboard
                # Check for backspace key press
                if event.key == pygame.K_BACKSPACE:
                    # get text input from 0 to -1 i.e. end.
                    user_text = user_text[:-1]
                # Unicode standard is used for string
                # formation
                else: # must be another key getting pressed that isnt the backspace
                    if not len(user_text) > nameLimit:  # name is under the NAME LENGTH LIMIT so just add the new text to it
                        user_text += event.unicode
                    # if users text passes a certain number then dont let them enter anymore characters.
                    # they can still backspace however and this will undo the limitation


        # it will set background color of screen
        screen.fill(BLACK)
        screen.blit(bg, (0,0)) # add custom background to the screen

        # draw user input rectangle and argument passed which should be on screen
        pygame.draw.rect(screen, BLUE, input_rect)
        text_surface = usertypingFont.render(user_text, True, (255, 255, 255))

        # draw submit button rectangle
        pygame.draw.rect(screen,BLUE,submitRect)

        # render text surface (where players text will appear) at position stated in arguments
        screen.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))
        # display a label to the screen that instructs the user to enter their name
        screen.blit(enterYourNameLabel, (45, 80))  # blit the label to the screen
        # display a label to the screen that instructs the user to submit their name (and score)
        screen.blit(submitLabel, (243, 422))  # blit this label to the screen
        screen.blit(userScoreLabel, (115,600)) # displays a prompt that says high score
        screen.blit(userScoreLabel2, (250, 660)) # displays the players high score under the prompt

        # set width of textfield so that text cannot get outside of user's text input
        input_rect.w = max(300, text_surface.get_width() + 10)

        # display.flip() will update only a portion of the
        # screen to updated, not full area
        pygame.display.flip()


def main():
    SCREEN_HEIGHT = 900  # Set the width and height of the screen [width, height]
    SCREEN_WIDTH = 700

    # setup pygame and screen size and caption below
    pygame.init()
    pygame.mixer.init()

    size = (SCREEN_WIDTH, SCREEN_HEIGHT)  # create a size var holding screen width and height
    screen = pygame.display.set_mode(size)  # initialize the screen
    pygame.display.set_caption("My Frogger Game")  # set a title for the game window

    startMenu(screen) # call the start menu screen function
    playFroggerMusic()    # call the play music function

    # This will be a list that will contain all the character sprites for the game.
    all_sprites_list = pygame.sprite.Group()

    # This will be a list that will contain all the roads, grass fields, and rivers for the game
    all_background_locations = pygame.sprite.Group()

    # This will be a list that will contain all the ENEMY automobile sprites for the game.
    all_enemy_automobiles = pygame.sprite.Group()
    all_riverLogs = pygame.sprite.Group() # A list that contains all the river objects (logs) for the game

    # A list that contains all the goal related objects (caves/rocks) for the game
    all_goalPosts = pygame.sprite.Group()

    # create your main character object (a frog in this case!)
    # set frogs color,x,y positions, width,height, (in that order).
    # Y pos has to be 840 because its the y coordinate OF THE TOP LEFT PIXEL of the character!
    playerFrog = Frog(DARK_GREEN,300,840, 60,60)

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
    font = pygame.font.Font("fonts/VarelaRound-Regular.ttf", 20)

    # -------- Main Program Loop -----------
    while not done:
        done = process_game_events(playerFrog, done) # process game events (like the frog moving)
        update_game_objects(screen, SCREEN_WIDTH, playerFrog, all_sprites_list, all_enemy_automobiles, all_riverLogs, dragonFly, all_goalPosts) # update the screen and game objects
        draw_game_objects(screen, all_sprites_list, all_background_locations) # draw game objects to the screen

        #fps = font.render(str(int(clock.get_fps())), True, pygame.Color('white'))  # render fps counter
        livesShown = font.render("Lives : " + str(playerFrog.getFrogLivesCount()), True, BLACK,WHITE)  # render lives counter
        scoreShown = font.render("High Score : " + str(playerFrog.getFrogHighScore()), True, BLACK, WHITE) # render score counter

        if playerFrog.getFrogLivesCount() <= 0: # players lives are 0 or less than 0
            inputHighScoreScreen(screen, playerFrog) # change screen to the personal high score input screen
            displayHighScores() # this function changes the screen to display all high scores from all players
            endScreen(screen) # change screens to the game over screen

        #screen.blit(fps, (50, 50))  # draw the fps counter to the screen
        screen.blit(livesShown, (0,0))  # draw the lives counter and score to the screen
        screen.blit(scoreShown, (0,40))

        pygame.display.update()  # update entire screen

        # --- Limit to 60 frames per second
        clock.tick(60) # changed this to 6 to test out collision on 5-22-21, make sure to change it back to 60 when possible
    # Close the window and quit.
    pygame.quit()


main()


