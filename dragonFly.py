import pygame
from random import *
from gameColors import * # import colors
import pygame
from SpriteSheet import * # import the spritesheet class to be used here

class DragonFly(pygame.sprite.Sprite):
    # This class represents a dragonfly insect to be eaten by the frog. It derives from the "Sprite" class in Pygame.
    def __init__(self,width, height, x,y):
        # Call the parent class (Sprite) constructor
        super().__init__()

        # Pass x and y position for the dragonfly.
        # Set the background color and set it to be transparent
        self.image = pygame.Surface([width, height]).convert()
        self.image.fill(WHITE)
        #self.image.set_colorkey(WHITE)
        self.width = width
        self.height = height
        self.change_x = 0 # set x&y speed vector of dragonfly
        self.change_y = 0
        self.dragonfly_flying_left = [] # this list holds all the images for animated move left of the dragonfly

        #pygame.draw.rect(self.image, GREEN, [0, 0, self.width, self.height]) # use this line of code to see a generic green block in place of the sprite!
        self.loadSprites() # create the list of sprites with this method call

        # Fetch the rectangle object that has the dimensions of the image.
        self.image = self.dragonfly_flying_left[0] # set the dragonfly sprite image that the dragonfly starts with
        self.rect = self.image.get_rect()

        # set x and y positions initially
        self.rect.x = x
        self.rect.y = y

        self.last = pygame.time.get_ticks()  # store number of milliseconds in last
        self.cooldown = 400  # cooldown time (the higher the cooldown, the slower the sprite frame transition will be from one img to the next! test it to see for yourself!)

    def loadSprites(self): # creates the dragonfly sprites
        sprite_sheet = SpriteSheet("Dragonfly Sprite Sheet.png") # load in the sprite sheet
        scaletuple = (50,50) # set scaling width and height

        image = sprite_sheet.get_image(6, 8, 20,15, BLACK) # create the image var for dragonfly (get the x y coordinates,width,height of the image in the SPRITE SHEET picture)
        image = pygame.transform.flip(image, True, False) # FLIP the image
        image = pygame.transform.scale(image, scaletuple)
        self.dragonfly_flying_left.append(image) # load the next flying image to the list

        image = sprite_sheet.get_image(38,8,19,16,BLACK) # next sprite
        image = pygame.transform.flip(image, True, False) # FLIP the image
        image = pygame.transform.scale(image, scaletuple)  # scale the image so it fits with other game sprites (Cars, etc)
        self.dragonfly_flying_left.append(image) # add the image to the list

        image = sprite_sheet.get_image(67,13,23,13,BLACK) # next sprite
        image = pygame.transform.flip(image, True, False) # FLIP the image (so instead of looking left, now it looks in the right direction)
        image = pygame.transform.scale(image, scaletuple)  # scale the image so it fits with other game sprites (Cars, etc)
        self.dragonfly_flying_left.append(image) # add the image to the list

    def moveLeft(self, changeX): # move dragonfly left a certain amount (using x speed vector value)
        self.change_x = changeX # set the x speed vector
        # move left, only if cooldown has been ((self.cooldown) / 1000) seconds since last
        current_time = pygame.time.get_ticks() # store number of milliseconds in current time

        if current_time - self.last >= self.cooldown: # compare the current number of ms minus the last number of ms if its greater than or equal to the cooldown time
            self.last = current_time # change the last number of ms to the current number
            self.rect.x += self.change_x  # move the character to the left

        # adjust the divisor (the operand on the right side of the // sign), the higher the number, the slower the dragonfly will be to update to its next sprite image! (this goes with the cooldown data member above!)
        frame = (self.rect.x // 60) % len(self.dragonfly_flying_left)  # calculate frame for the current image
        self.image = self.dragonfly_flying_left[frame]  # set the dragonfly image to a new image [position is frames value]

    def moveRight(self, changeX): # move dragonfly right a certain amount (using x speed vector value)
        self.change_x = changeX # set the x speed vector
        # move left, only if cooldown has been ((self.cooldown) / 1000) seconds since last
        current_time = pygame.time.get_ticks() # store number of milliseconds in current time

        if current_time - self.last >= self.cooldown: # compare the current number of ms minus the last number of ms if its greater than or equal to the cooldown time
            self.last = current_time # change the last number of ms to the current number
            self.rect.x += self.change_x  # move the character to the left

        # adjust the divisor (the operand on the right side of the // sign), the higher the number, the slower the dragonfly will be to update to its next sprite image! (this goes with the cooldown data member above!)
        frame = (self.rect.x // 60) % len(self.dragonfly_flying_left)  # calculate frame for the current image
        self.image = self.dragonfly_flying_left[frame]  # set the dragonfly image to a new image [position is frames value]

    def teleportAround(self): # moves dragonfly to each goal post randomly (left to right and vice versa)
        moveLeftChoice = 1 # this var represents the choice for the dragonfly to go left
        moveRightChoice = 2 # this var represents the choice for the dragonfly to go left
        if(randint(moveLeftChoice,moveRightChoice) == 1): # check if the random number was 1
            if(self.rect.x == 270): # dragonfly position moved to the right previously
                self.moveLeft(-120) # move the dragonfly to the left(back to its initial position!)
            elif(self.rect.x == 385): # dragonfly is at another position to the right
                self.moveLeft(-115) # move the dragonfly to the left again
            elif(self.rect.x == 500):
                self.moveLeft(-115)
            else: # dragonfly position is at the starting position
                self.moveLeft(0) # dont let dragonfly move to the left so just pass 0 and only its sprite will update
        else: # random number was 2
            if(self.rect.x == 150): # dragonflys position is still at its starting position
                self.moveRight(120) # move the dragonfly to the right!
            elif(self.rect.x == 270): # dragonfly position is somewhere to the right
                self.moveRight(115) # move the dragonfly to the right again!
            elif(self.rect.x == 385): # dragonfly position is somewhere to the right
                self.moveRight(115)
            else:
                self.moveRight(0) # dont let dragonfly move to the right so just pass 0 and only its sprite will update


    def loadDragonFlySprite(self): # load the image of the dragonfly sprite
        sprite_sheet = SpriteSheet("Dragonfly Sprite Sheet.png") # load in the sprite sheet
        scaletuple = (50,50) # set scaling width and height

        image = sprite_sheet.get_image(6,8,20,15, BLACK)  # call method and pass in the args -> x pos , y pos, width, height, and color key for surface
        image = pygame.transform.flip(image, True, False) # FLIP the image (so instead of looking left, now it looks in the right direction)
        image = pygame.transform.scale(image, scaletuple)  # scale the image so it fits with other game sprites (frog, background, etc)
        self.image = image # Load a proper picture of the dragonfly...

    def setXPos(self,x): # set the x position of the dragonfly
        self.rect.x = x

    def setYPos(self,y):  # set the y position of the dragonfly
        self.rect.y = y

    def getXPos(self): # get the x position of the dragonfly
        return self.rect.x

    def getYPos(self):  # get the y position of the dragonfly
        return self.rect.y