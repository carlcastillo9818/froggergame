import pygame
from SpriteSheet import * # import the spritesheet class to be used here

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

#this class is used to make a Frog character for my frogger game (but could be used in other games too!)
class Frog(pygame.sprite.Sprite):
    def __init__(self, color, x , y, width = 0,height = 0):
        super().__init__() # call parent class constructor first

        # Pass in the color of the frog, width and height, and x and y position.
        # Set the background color and set it to be transparent
        self.image = pygame.Surface([width, height])
        self.image.fill(WHITE)
        #self.image.set_colorkey(WHITE)
        self.width = width
        self.height = height
        self.color = color
        # set speed vector of player
        self.change_x = 0
        self.change_y = 0
        # this list holds all the images for animated walk left of the Frog
        self.frog_walking_left = []
        # this list holds all the images for animated walk right of the frog
        self.frog_walking_right = []
        # this list holds all the images for animated walking up of the frog
        self.frog_walking_up = []
        # this list holds all the images for animated walking down of the frog
        self.frog_walking_down = []

        # create sprite sheet object holding the frog sprite sheet images in it
        sprite_sheet = SpriteSheet("GreenFrog.png")

        #get the LEFT direction images
        image = sprite_sheet.get_image(0,0,24,15, WHITE) # create starting image the frog starts with
        image = pygame.transform.scale(image, (60,60))  # scale the image so it fits with other game sprites (Cars, etc)
        self.frog_walking_left.append(image) # add the starting image to the list (moving left)
        image = sprite_sheet.get_image(0, 48, 30,24, WHITE) # create the image var for left walking (get the coordinates,width,height of the image in the SPRITE SHEET picture)
        image = pygame.transform.scale(image, (60, 60))
        self.frog_walking_left.append(image) # load the next LEFT walking image to the list (moving left)
        image = sprite_sheet.get_image(34,54, 34,17, WHITE)
        image = pygame.transform.scale(image,(60,60))
        self.frog_walking_left.append(image)

        # get the RIGHT direction images
        image = sprite_sheet.get_image(0,0,24,15, WHITE) # create starting image the frog starts with
        image = pygame.transform.flip(image, True, False) # FLIP the image (so instead of looking left, now it looks in the right direction)
        image = pygame.transform.scale(image, (60,60)) # scale the image so it fits with other game sprites (Cars, etc)
        self.frog_walking_right.append(image) # add the starting image to the list (moving right)
        image = sprite_sheet.get_image(0, 48, 30,24, WHITE) # create the image var for right walking (get the x coord, y coord,width,height of the image in the SPRITE SHEET picture)
        image = pygame.transform.flip(image, True, False)
        image = pygame.transform.scale(image, (60, 60))
        self.frog_walking_right.append(image) # load the next right walking image to the list (moving right)
        image = sprite_sheet.get_image(34,54, 34,17, WHITE)
        image = pygame.transform.flip(image, True, False)
        image = pygame.transform.scale(image,(60,60))
        self.frog_walking_right.append(image)

        #get the UP direction images
        image = sprite_sheet.get_image(0,0,24,15, WHITE) # create starting image the frog starts with
        image = pygame.transform.scale(image, (60,60)) # scale the image so it fits with other game sprites (Cars, etc)
        self.frog_walking_up.append(image) # add the starting image to the list (moving up)
        image = sprite_sheet.get_image(0, 48, 30,24, WHITE) # create the image var for up walking (get the x coord, y coord,width,height, color key of the image in the SPRITE SHEET picture)
        image = pygame.transform.scale(image, (60,60)) # scale the image so it fits with other game sprites (Cars, etc)
        self.frog_walking_up.append(image) # load the next up walking image to the list(moving up)
        image = sprite_sheet.get_image(34,54, 34,17, WHITE)
        image = pygame.transform.scale(image,(60,60))
        self.frog_walking_up.append(image)

        #get the DOWN direction images
        image = sprite_sheet.get_image(0,0,24,15, WHITE) # create starting image the frog starts with
        image = pygame.transform.flip(image, True, False) # FLIP the image (so instead of looking left, now it looks in the right direction)
        image = pygame.transform.scale(image, (60,60)) # scale the image so it fits with other game sprites (Cars, etc)
        self.frog_walking_down.append(image) # add the starting image to the list (moving down)
        image = sprite_sheet.get_image(0, 48, 30,24, WHITE) # create the image var for down walking (get the x coord, y coord,width,height of the image in the SPRITE SHEET picture)
        image = pygame.transform.flip(image, True, False)
        image = pygame.transform.scale(image, (60, 60))
        self.frog_walking_down.append(image) # load the next down walking image to the list (moving down)
        image = sprite_sheet.get_image(34,54, 34,17, WHITE)
        image = pygame.transform.flip(image, True, False)
        image = pygame.transform.scale(image,(60,60))
        self.frog_walking_down.append(image)


        # Draw the basic green rectangle (hide this after importing frog image 3-17-21)
        #pygame.draw.rect(self.image, self.color, [0, 0, self.width, self.height])

        # Load a proper pic of a frog...
        self.image = self.frog_walking_left[0] # set the frog image that the frog starts with
        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect() # set a reference to the image rect

        # set x and y positions initially
        self.rect.x = x
        self.rect.y = y


    def moveRight(self): # move frog right (using x speed vector value)
        self.change_x = 5 # set the x speed vector
        self.rect.x += self.change_x # apply the speed to the x position

        '''To calculate the frame (could be 1,2,or a higher number) use the calculation below:
        The lower the frame number, the quicker you will go through the frog animations.
        The higher the frame number, the slower (but more clearly) you will go through the frog animations. 
        Adjust as necessary.

        You divide your current position (self.rect.x) by 60 using INTEGER division.  
        You take that result and divide it by the length of the walking_right image list.
        After that, you take the remainder which will be the frame number and assign it to
        the frame variable!
        '''
        frame = (self.rect.x // 50) % len(self.frog_walking_right) # calculate frame for the current image
        self.image = self.frog_walking_right[frame]  # set the frogs image to a new image [position is frames value]

        print(self.rect.x) # check current x position after moving (change_x) speed

    def moveLeft(self): # move frog left (using the x speed vector value)
        self.change_x = -5 # set the x speed vector
        self.rect.x += self.change_x # apply the speed to the x position

        '''To calculate the frame (could be 1,2,or a higher number) use the calculation below:
        The lower the frame number, the quicker you will go through the frog animations.
        The higher the frame number, the slower (but more clearly) you will go through the frog animations. 
        Adjust as necessary.
        
        You divide your current position (self.rect.x) by 60 using INTEGER division.  
        You take that result and divide it by the length of the walking_left image list.
        After that, you take the remainder which will be the frame number and assign it to
        the frame variable!
        '''
        frame = (self.rect.x // 50) % len(self.frog_walking_left) # calculate frame for the current image
        self.image = self.frog_walking_left[frame] # set the frogs image to a new image [position is frames value]

        print(self.rect.x) # check current x position after moving (change_x) speed

    def moveUp(self):# move frog up (using the y speed vector value)
        self.change_y = -5
        self.rect.y += self.change_y

        frame = (self.rect.y // 40) % len(self.frog_walking_up)  # calculate frame for the current image
        self.image = self.frog_walking_up[frame]  # set the frogs image to a new image [position is frames value]

        print(self.rect.y)  # check current y position after moving (change_y) speed

    def moveDown(self):# move frog down (using the y speed vector value)
        self.change_y = 5
        self.rect.y += self.change_y

        frame = (self.rect.y // 40) % len(self.frog_walking_down)  # calculate frame for the current image
        self.image = self.frog_walking_down[frame]  # set the frogs image to a new image [position is frames value]

        print(self.rect.y)  # check current y position after moving (change_y) speed

    def setXPos(self,x): # set the x position of frog
        self.rect.x = x

    def setYPos(self,y):  # set the y position of frog
        self.rect.y = y

    def stop(self):# Called when the user lets off the keyboard.
        if (self.change_x > 0):
            self.image = self.frog_walking_right[0]  # set the frogs resting image state to the default image (looking to the right)
        elif(self.change_x < 0):
            self.image = self.frog_walking_left[0]  # set the frogs resting image state to the default image (looking to the left)
        elif(self.change_y < 0):
            self.image = self.frog_walking_up[0] # set the frogs resting image state to the default image (looking to the left)
        elif(self.change_y > 0):
            self.image = self.frog_walking_down[0]

        self.change_x = 0  # set speed vectors to 0 (Frog has zero speed)
        self.change_y = 0