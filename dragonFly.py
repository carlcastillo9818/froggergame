import pygame
from random import choice
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

        # Initialise attributes of the dragonfly.
        self.width = width
        self.height = height

        #pygame.draw.rect(self.image, GREEN, [0, 0, self.width, self.height]) # use this line of code to see a generic green block in place of the sprite!

        self.loadDragonFlySprite() # call this function to set the dragonfly sprite.  Comment this out if you wish to see a green block instead of the sprite for whatever reason (testing)

        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()

        # set x and y positions initially
        self.rect.x = x
        self.rect.y = y

    def loadDragonFlySprite(self): # load the image of the dragonfly sprite
        sprite_sheet = SpriteSheet("Dragonfly Sprite Sheet.png") # load in the sprite sheet
        image = sprite_sheet.get_image(6,8,20,15, BLACK)  # call method and pass in the args -> x pos , y pos, width, height, and color key for surface
        image = pygame.transform.scale(image, (50, 50))  # scale the image so it fits with other game sprites (frog, background, etc)
        self.image = image # Load a proper picture of the dragonfly...

    def setXPos(self,x): # set the x position of the dragonfly
        self.rect.x = x

    def setYPos(self,y):  # set the y position of the dragonfly
        self.rect.y = y

    def getXPos(self): # get the x position of the dragonfly
        return self.rect.x

    def getYPos(self):  # get the y position of the dragonfly
        return self.rect.y