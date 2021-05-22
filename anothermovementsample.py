import pygame
import sys

class Character(object):
    def __init__(self, x=0, y=0, speed=0):
        self.x = x
        self.y = y
        self.speed = speed
        self.image = pygame.image.load('GreenFrog.png')

    def get_size(self):
        return self.image.get_size()

    def draw(self):
        display.blit(self.image, (self.x, self.y))


pygame.init()
(width, height) = (800, 600)
display = pygame.display.set_mode((width, height))
pygame.display.set_caption('Platforms')
clock = pygame.time.Clock()
hero = Character(speed=5)
hero_width, hero_height = hero.get_size()
hero.x = width/2.0 - hero_width/2.0
hero.y = height/2.0 - hero_height/2.0
black = (0,0,0)
pressed_keys = {"left": False, "right": False, "up": False, "down": False}

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                pressed_keys["left"] = True
            if event.key == pygame.K_RIGHT:
                pressed_keys["right"] = True
            if event.key == pygame.K_UP:
                pressed_keys["up"] = True
            if event.key == pygame.K_DOWN:
                pressed_keys["down"] = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                pressed_keys["left"] = False
            if event.key == pygame.K_RIGHT:
                pressed_keys["right"] = False
            if event.key == pygame.K_UP:
                pressed_keys["up"] = False
            if event.key == pygame.K_DOWN:
                pressed_keys["down"] = False

    if pressed_keys["left"]:# == True is implied here
        hero.x -= hero.speed
    if pressed_keys["right"]:
        hero.x += hero.speed
    if pressed_keys["up"]:
        hero.y -= hero.speed
    if pressed_keys["down"]:
        hero.y += hero.speed

    display.fill(black)
    hero.draw()
    pygame.display.update()
    clock.tick(60)