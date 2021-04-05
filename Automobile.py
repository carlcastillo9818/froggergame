import pygame
from SpriteSheet import * # import the spritesheet class to be used here


# Define constants (colors, speed, etc.)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0,0,255)
RED = (255,0,0)
YELLOW = (255,255,0)
PURPLE = (255,0,255)
ORANGE = (255, 165, 0)
#this class is used to make automobiles for my frogger game (but could be used in other games too!)
class Automobile(pygame.sprite.Sprite):
    # This class represents a car/truck/vehicle with wheels. It derives from the "Sprite" class in Pygame.
    def __init__(self, color, width, height, speed,x,y, direction):
        # Call the parent class (Sprite) constructor
        super().__init__()

        # Pass in the color of the car, width and height, and its x and y position,.
        # Set the background color and set it to be transparent
        self.image = pygame.Surface([width, height])
        self.image.fill(WHITE)
       #self.image.set_colorkey(WHITE)

        # Initialise attributes of the car.
        self.width = width
        self.height = height
        self.color = color
        # Set speed vector of automobile
        self.change_x = speed

        # set direction of the car (indicates whether car image will face to the left or right!)
        self.direction = direction

        # Draw the automobile (a rectangle!)
        #pygame.draw.rect(self.image, self.color, [0, 0, self.width, self.height])


        self.repaint(self.color) # call this function to load in the correct colored car (color arg provides the color that the car SHOULD BE)

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
        # 4/5/21
        '''
        NEXT TIME: WORK ON ADDING THE REST OF THE DIFFERENT COLOR CAR SPRITE IMAGES SO EACH TIME
        A NEW CAR COMES OUT OF THE LEFT
        OR RIGHT WALL THEN IT WILL BE A DIFFERENT COLORED CAR SPRITE! MOVE ON FROM USING THE SIMPLE RECTANGLE SHAPES!
        '''

        sprite_sheet = SpriteSheet("Isometric_vehicles2/mid_blue.png")
        if(color == RED):
            # create sprite sheet holding all the car sprites (RED)
            sprite_sheet = SpriteSheet("Isometric_vehicles2/red.png")
        elif (color == BLUE):
            # create sprite sheet holding all the car sprites (BLUE)
            sprite_sheet = SpriteSheet("Isometric_vehicles2/light_blue.png")
        elif (color == GREEN):
            # create sprite sheet holding all the car sprites (GREEN)
            sprite_sheet = SpriteSheet("Isometric_vehicles2/green.png")
        elif (color == YELLOW):
            sprite_sheet = SpriteSheet("Isometric_vehicles2/yellow.png")
        elif (color == PURPLE):
            sprite_sheet = SpriteSheet("Isometric_vehicles2/purple.png")
        elif (color == ORANGE):
            sprite_sheet = SpriteSheet("Isometric_vehicles2/orange.png")

        if (self.direction == "Right"):  # make car image face to the right
            # retrieve the image with the x coord, y coord, width, height
            image = sprite_sheet.get_image(131, 14, 59, 37, BLACK)
            image = pygame.transform.flip(image, True, False)  # FLIP the image (so instead of looking left, now it looks in the right direction)
            image = pygame.transform.scale(image, (60, 60))  # scale the image so it fits with other game sprites (frog, background, etc)
            # Load a proper picture of the automobile...
            self.image = image
        elif (self.direction == "Left"):  # make car image face to the left
            image = sprite_sheet.get_image(131, 14, 59, 37, BLACK)
            image = pygame.transform.scale(image, (60, 60))  # scale the image so it fits with other game sprites (frog, background, etc)
            # Load a proper picture of the automobile...
            self.image = image


    def setXPos(self,x): # set the x position of the automobile
        self.rect.x = x

    def setYPos(self,y):  # set the y position of the automobile
        self.rect.y = y