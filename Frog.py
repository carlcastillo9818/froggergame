import pygame

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

#this class is used to make a Frog character for my frogger game (but could be used in other games too!)
class Frog(pygame.sprite.Sprite):
    def __init__(self, color, width ,height):
        super().__init__() # call parent class constructor first

        # Pass in the color of the car, and its x and y position, width and height.
        # Set the background color and set it to be transparent
        self.image = pygame.Surface([width, height])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)

        # Draw the car (a rectangle!)
        pygame.draw.rect(self.image, color, [0, 0, width, height])

        # Instead we could load a proper pic of a car...
        # self.image = pygame.image.load("car.png").convert_alpha()

        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()

    def moveRight(self, pixels): # move character right by n pixels
        self.rect.x += pixels

    def moveLeft(self, pixels): # move character left by n pixels
        self.rect.x -= pixels

    def moveUp(self, pixels):# move character up by n pixels
        self.rect.y -= pixels

    def moveDown(self, pixels):# move character down by n pixels (comment out this function later)
        self.rect.y += pixels

