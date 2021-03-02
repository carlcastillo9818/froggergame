import pygame

# This class is used to make IMAGE BACKGROUNDS (with images pulled from the internet) for my games
class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        super().__init__() # call parent class constructor first

        self.image = pygame.image.load(image_file) # pass in your image file to the image field

        # Alt way
        # self.image = pygame.image.load("car.png").convert_alpha()

        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location