import pygame
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# This class is used to make any sort of rectangular backgrounds (long rectangles of grass, roads, water streams, etc)
class RectBackground(pygame.sprite.Sprite):
    def __init__(self, surface, color,width,height):
        super().__init__() # call parent class constructor first

        # Initialise attributes of the rect background

        # Pass in the color of the rect background, and its x and y position, width and height.
        # Set the background color and set it to be transparent
        self.image = pygame.Surface([width, height])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)
        self.width = width
        self.height = height
        self.color = color


        # Draw the rect background(a rectangle!)
        self.road = pygame.draw.rect(self.image, self.color, [0,0, self.width, self.height])

        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()
