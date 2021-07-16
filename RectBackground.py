import pygame
from gameColors import * # import colors
from SpriteSheet import *

# This class is used to make any sort of rectangular backgrounds (long rectangles of grass, roads, water streams, etc)
class RectBackground(pygame.sprite.Sprite):
    def __init__(self, surface, color,width,height,x,y, blocktype = "none"):
        super().__init__() # call parent class constructor first

        # Initialise attributes of the rect background

        # Pass in the color of the rect background,  width and height, and its x and y position,.
        # Set the background color and set it to be transparent
        self.image = pygame.Surface([width, height]).convert()
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)
        self.width = width
        self.height = height
        self.color = color
        self.blockType = blocktype # holds the optional arg for a block type (grass, water, sand, etc.)
        self.loadTileSet() # call this method which checks whether to use a tileset sprite sheet or not
        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()

        # set x and y positions initially
        self.rect.x = x
        self.rect.y = y

    '''this method will check the rectbackground objects block type (grass, water, etc) and generate 
    the correct sprite tileset to use for it which will be displayed in the game.'''
    def loadTileSet(self):
        if(self.blockType == "none"):
            self.rect = pygame.draw.rect(self.image, self.color, [0, 0, self.width, self.height])
        else:
            scaletuple = (65, 60)  # set scaling width and height
            if(self.blockType == "grass"):
                spritesheet = SpriteSheet("images/LongGrassTiles.png")
                image = spritesheet.get_image(0, 0, 64, 64,BLACK)  # create the image var for dragonfly (get the x y coordinates,width,height of the image in the SPRITE SHEET picture)
                image = pygame.transform.smoothscale(image, scaletuple)
                self.image = image
            elif(self.blockType == "water"):
                spritesheet = SpriteSheet("images/WaterTile.png")
                image = spritesheet.get_image(34,34,32,32,BLACK)
                image = pygame.transform.scale(image, scaletuple)
                self.image = image
            elif(self.blockType == "road"):
                spritesheet = SpriteSheet("images/RoadTile.png")
                image = spritesheet.get_image(0,0,31,28,BLACK)
                image = pygame.transform.scale(image, scaletuple)
                self.image = image

    def setXPos(self, x):  # set the x position of the rectangle field
        self.rect.x = x

    def setYPos(self, y):  # set the y position of the rectangle field
        self.rect.y = y