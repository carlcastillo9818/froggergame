from random import choice
from gameColors import * # import colors
import pygame
from SpriteSheet import * # import the spritesheet class to be used here

#this class is used to make automobiles for my frogger game (but could be used in other games too!)
class Automobile(pygame.sprite.Sprite):
    # This class represents a car/truck/vehicle with wheels. It derives from the "Sprite" class in Pygame.
    def __init__(self, width, height, speed,x,y, direction):
        # Call the parent class (Sprite) constructor
        super().__init__()

        # Pass in the color of the car, width and height, and its x and y position,.
        # Set the background color and set it to be transparent
        self.image = pygame.Surface([width, height]).convert()
        self.image.fill(WHITE)
       #self.image.set_colorkey(WHITE)

        # Initialise attributes of the car.
        self.width = width
        self.height = height
        # Set speed vector of automobile
        self.change_x = speed

        # set direction of the car (indicates whether car image will face to the left or right!)
        self.direction = direction

        # Draw the automobile (a rectangle!)
        #pygame.draw.rect(self.image, self.color, [0, 0, self.width, self.height])


        self.repaint() # call this function to set random color for the automobile object

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

    def repaint(self): # change the color of the automobile (corresponding sprite sheet for the car)

        '''
         4/5/21 ADDED THE REST OF THE DIFFERENT COLOR CAR SPRITE IMAGES SO EACH TIME
        A NEW CAR COMES OUT OF THE LEFT
        OR RIGHT WALL THEN IT WILL BE A DIFFERENT COLORED CAR SPRITE! MOVED ON FROM USING THE SIMPLE RECTANGLE SHAPES!
        '''

        # list of all file locations for each sprite sheet (diff colors)
        myCarSpriteList = ["images/Isometric_vehicles2/red.png", "images/Isometric_vehicles2/light_blue.png", "images/Isometric_vehicles2/green.png", "images/Isometric_vehicles2/yellow.png", "images/Isometric_vehicles2/orange.png", "images/Isometric_vehicles2/white.png", "images/Isometric_vehicles2/mid_blue.png"]
        sprite_sheet = SpriteSheet(choice(myCarSpriteList)) # randomly select a sprite sheet

        self.direction_image(sprite_sheet) # call method with the sprite sheet that was randomly picked

    def direction_image(self, spritesheet): # adjusts sprite image direction based on direction arg
        image = spritesheet.get_image(131, 14, 59, 37, BLACK) # call method and pass in the args -> x pos , y pos, width, height, and color key for surface
        if (self.direction == "Right"):  # make car image face to the right
            # retrieve the image with the x coord, y coord, width, height
            image = pygame.transform.flip(image, True, False)  # FLIP the image (so instead of looking left, now it looks in the right direction)
            image = pygame.transform.scale(image, (60, 60))  # scale the image so it fits with other game sprites (frog, background, etc)
        elif (self.direction == "Left"):  # make car image face to the left
            image = pygame.transform.scale(image, (60, 60))  # scale the image so it fits with other game sprites (frog, background, etc)

        # Load a proper picture of the automobile...
        self.image = image

    def setXPos(self,x): # set the x position of the automobile
        self.rect.x = x

    def setYPos(self,y):  # set the y position of the automobile
        self.rect.y = y

    def getXPos(self): # get the x position of the automobile
        return self.rect.x

    def getYPos(self):  # get the y position of the automobile
        return self.rect.y