import pygame
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

#this class is used to make automobiles for my frogger game (but could be used in other games too!)
class Automobile(pygame.sprite.Sprite):
    # This class represents a car/truck/vehicle with wheels. It derives from the "Sprite" class in Pygame.
    def __init__(self, color, width, height, speed,x,y):
        # Call the parent class (Sprite) constructor
        super().__init__()

        # Pass in the color of the car, width and height, and its x and y position,.
        # Set the background color and set it to be transparent
        self.image = pygame.Surface([width, height])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)

        # Initialise attributes of the car.
        self.width = width
        self.height = height
        self.color = color
        # Set speed vector of automobile
        self.change_x = speed

        # Draw the automobile (a rectangle!)
        pygame.draw.rect(self.image, self.color, [0, 0, self.width, self.height])

        # Load a proper picture of the automobile...
        # self.image = pygame.image.load("car.png").convert_alpha()

        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()

        # set x and y positions initially
        self.rect.x = x
        self.rect.y = y

    def moveRight(self): # move automobile right
        self.rect.x += self.change_x

    def moveLeft(self): # move automobile left
        self.rect.x -= self.change_x


    def changeSpeed(self, speed): # adjust speed
        self.change_x = speed

    def repaint(self, color): # change the color of the automobile
        self.color = color
        pygame.draw.rect(self.image, self.color, [0, 0, self.width, self.height])

    def setXPos(self,x): # set the x position of the automobile
        self.rect.x = x

    def setYPos(self,y):  # set the y position of the automobile
        self.rect.y = y