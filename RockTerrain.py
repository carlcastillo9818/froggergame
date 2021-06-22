import pygame
from gameColors import * # import colors
from SpriteSheet import * # import the spritesheet class to be used here

# This class is used to make the rocks near the frog home goals
class RockTerrain(pygame.sprite.Sprite):
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

        self.loadRockSprite() # call this function to set the rock sprite image

        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()

        # set x and y positions initially
        self.rect.x = x
        self.rect.y = y

    def setXPos(self, x):  # set the x position of the rectangle field
        self.rect.x = x

    def setYPos(self, y):  # set the y position of the rectangle field
        self.rect.y = y


    def loadRockSprite(self):  # load the image of the rock
        sprite_sheet = SpriteSheet("Kauzz Cave Tiles/Environment.png")  # load in the sprite sheet
        image = sprite_sheet.get_image(340, 135, 43, 42, BLACK) # call method and pass in the args -> x pos , y pos, width, height, and color key for surface
        image = pygame.transform.scale(image,(60, 60))  # scale the image so it fits with other game sprites (frog, background, etc)
        self.image = image
