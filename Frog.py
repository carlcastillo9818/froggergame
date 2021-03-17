import pygame
from SpriteSheet import * # import the spritesheet class to be used here

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

#this class is used to make a Frog character for my frogger game (but could be used in other games too!)
class Frog(pygame.sprite.Sprite):
    def __init__(self, color, x , y, width = 0,height = 0):
        super().__init__() # call parent class constructor first

        sprite_sheet = SpriteSheet("GreenFrog.png")

        # Pass in the color of the frog, width and height, and x and y position.
        # Set the background color and set it to be transparent
        self.image = pygame.Surface([width, height])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)
        self.width = width
        self.height = height
        self.color = color

        # Draw the basic green rectangle (represents frog initally) (hide this for now after importing frog image 3-17-21)
        #pygame.draw.rect(self.image, self.color, [0, 0, self.width, self.height])

        # Load a proper pic of a frog...
        self.image = sprite_sheet.get_image(0,0,26,16)
        self.image = pygame.transform.scale(self.image, (60,60))

        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()

        # set x and y positions initially
        self.rect.x = x
        self.rect.y = y


    def moveRight(self, pixels): # move frog right by n pixels
        self.rect.x += pixels

    def moveLeft(self, pixels): # move frog left by n pixels
        self.rect.x -= pixels

    def moveUp(self, pixels):# move frog up by n pixels
        self.rect.y -= pixels

    def moveDown(self, pixels):# move frog down by n pixels (comment out this function later)
        self.rect.y += pixels

    def setXPos(self,x): # set the x position of frog
        self.rect.x = x

    def setYPos(self,y):  # set the y position of frog
        self.rect.y = y