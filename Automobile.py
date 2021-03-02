import pygame
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

#this class is used to make automobiles for my frogger game (but could be used in other games too!)
class Automobile(pygame.sprite.Sprite):
    # This class represents a car/truck/vehicle with wheels. It derives from the "Sprite" class in Pygame.

    def __init__(self, color, width, height, speed):
        # Call the parent class (Sprite) constructor
        super().__init__()

        # Pass in the color of the car, and its x and y position, width and height.
        # Set the background color and set it to be transparent
        self.image = pygame.Surface([width, height])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)

        # Initialise attributes of the car.
        self.width = width
        self.height = height
        self.color = color
        self.speed = speed

        # Draw the automobile (a rectangle!)
        pygame.draw.rect(self.image, self.color, [0, 0, self.width, self.height])

        # Instead we could load a proper picture of the automobile...
        # self.image = pygame.image.load("car.png").convert_alpha()

        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()

    def moveRight(self, speed):
        self.rect.x += self.speed * speed / 20

    def moveLeft(self, speed):
        self.rect.x -=  self.speed * speed / 20


    def changeSpeed(self, speed):
        self.speed = speed

    def repaint(self, color):
        self.color = color
        pygame.draw.rect(self.image, self.color, [0, 0, self.width, self.height])

    def setXPos(self,x): # set the x position of the rectangle field
        self.rect.x = x

    def setYPos(self,y):  # set the y position of the rectangle field
        self.rect.y = y