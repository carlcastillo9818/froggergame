import pygame
from gameColors import * # import colors
from SpriteSheet import * # import the spritesheet class to be used here

# This class is used to make the frog homes (goals of the game)
class FrogHome(pygame.sprite.Sprite):
    def __init__(self, surface, width,height,x,y):
        super().__init__() # call parent class constructor first

        # Initialise attributes of the rect background
        # Pass in the width and height, and its x and y position,.
        # Set the background color and set it to be transparent
        self.image = pygame.Surface([width, height]).convert()
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)
        self.width = width
        self.height = height

        self.loadFrogHomeSprite() # call this function to set the frog home sprite image
        #pygame.draw.rect(self.image, GREEN, [0, 0, self.width, self.height]) creates a green block in place of the sprite for TESTING!

        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()

        # set x and y positions initially
        self.rect.x = x
        self.rect.y = y

    def setXPos(self, x):  # set the x position
        self.rect.x = x

    def setYPos(self, y):  # set the y position
        self.rect.y = y

    def getXPos(self): # get the x position
        return self.rect.x

    def getYPos(self):  # get the y position
        return self.rect.y

    def loadFrogHomeSprite(self):  # load the image of the frogs home (should look like a cave like in the real frogger game)
        sprite_sheet = SpriteSheet("Kauzz Cave Tiles/Environment.png")  # load in the sprite sheet
        image = sprite_sheet.get_image(31, 15, 56, 51, BLACK) # call method and pass in the args -> x pos , y pos, width, height, and color key for surface
        image = pygame.transform.scale(image,(60, 60))  # scale the image so it fits with other game sprites (frog, background, etc)
        self.image = image
