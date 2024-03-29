"""
This module is used to pull individual sprites from sprite sheets.

I got this class file from progrmaarcadegames.com so credits to them
for this class file. It was appropriate to use in my game.
"""
import pygame
from gameColors import * # import colors

class SpriteSheet():
    """ Class used to grab images out of a sprite sheet. """

    def __init__(self, file_name):
        """ Constructor. Pass in the file name of the sprite sheet. """

        # Load the sprite sheet.
        self.sprite_sheet = pygame.image.load(file_name).convert_alpha()

    def get_image(self, x, y, width, height, color):
        """ Grab a single image out of a larger spritesheet
            Pass in the x, y location of the sprite
            and the width and height of the sprite. Also pass in the color key for the surface"""

        # Create a new blank image
        image = pygame.Surface([width, height]).convert()

        # Copy the sprite from the large sheet onto the smaller image
        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))


        # Assuming white works as the transparent color
        #Set the current color key for the Surface. When blitting this Surface onto a destination,
        # any pixels that have the same color as the colorkey will be transparent.
        image.set_colorkey(color)

        # Return the image
        return image
