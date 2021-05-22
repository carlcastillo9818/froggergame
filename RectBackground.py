import pygame
from gameColors import * # import colors

# This class is used to make any sort of rectangular backgrounds (long rectangles of grass, roads, water streams, etc)
class RectBackground(pygame.sprite.Sprite):
    def __init__(self, surface, color,width,height,x,y):
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


        # Draw the rect background(a rectangle!)
        self.rect = pygame.draw.rect(self.image, self.color, [0,0, self.width, self.height])

        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()

        # set x and y positions initially
        self.rect.x = x
        self.rect.y = y

    def setXPos(self, x):  # set the x position of the rectangle field
        self.rect.x = x

    def setYPos(self, y):  # set the y position of the rectangle field
        self.rect.y = y