"""
Sample Python/Pygame Programs
Simpson College Computer Science
http://programarcadegames.com/
http://simpson.edu/computer-science/
"""

import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0,255,0)

class Player(pygame.sprite.Sprite):
    """ The class is the player-controlled sprite. """

    def __init__(self, x, y):
        """Constructor function"""
        # Call the parent's constructor
        super().__init__()

        # Set height, width
        self.image = pygame.Surface([50, 50])
        self.image.fill('blue')
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.last = pygame.time.get_ticks() # store number of milliseconds in last
        self.cooldown = 300 # cooldown time

    def moveUp(self):
        # move up, only if cooldown has been ((self.cooldown) / 1000) seconds since last
        current_time = pygame.time.get_ticks() # store number of milliseconds in current time
        print("Current time " + str(current_time) + " - last recorded time " + str(self.last))
        print("Condition is : " + str(current_time - self.last >= self.cooldown))
        if current_time - self.last >= self.cooldown: # compare the current number of ms minus the last number of ms if its greater than or equal to the cooldown time
            self.last = current_time # change the last number of ms to the current number
            player.rect.y -= 50 # move the character up
    def moveDown(self):
        # move up, only if cooldown has been ((self.cooldown) / 1000) seconds since last
        current_time = pygame.time.get_ticks() # store number of milliseconds in current time
        if current_time - self.last >= self.cooldown: # compare the current number of ms minus the last number of ms if its greater than or equal to the cooldown time
            self.last = current_time # change the last number of ms to the current number
            player.rect.y += 50 # move the character down

    def moveLeft(self):
        # move up, only if cooldown has been ((self.cooldown) / 1000) seconds since last
        current_time = pygame.time.get_ticks() # store number of milliseconds in current time
        if current_time - self.last >= self.cooldown: # compare the current number of ms minus the last number of ms if its greater than or equal to the cooldown time
            self.last = current_time # change the last number of ms to the current number
            player.rect.x -= 50 # move the character left

    def moveRight(self):
        # move up, only if cooldown has been ((self.cooldown) / 1000) seconds since last
        current_time = pygame.time.get_ticks() # store number of milliseconds in current time
        if current_time - self.last >= self.cooldown: # compare the current number of ms minus the last number of ms if its greater than or equal to the cooldown time
            self.last = current_time # change the last number of ms to the current number
            player.rect.x += 50 # move the character left

# Call this function so the Pygame library can initialize itself
pygame.init()

# Create an 800x600 sized screen
screen = pygame.display.set_mode([800, 600])

# Set the title of the window
pygame.display.set_caption('Move Sprite With Keyboard')

# Create the player paddle object
player = Player(0, 550)



all_sprites_list = pygame.sprite.Group()
all_sprites_list.add(player)




clock = pygame.time.Clock()
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.moveLeft()
            elif event.key == pygame.K_RIGHT:
                player.moveRight()
            elif event.key == pygame.K_UP:
                player.moveUp()
            elif event.key == pygame.K_DOWN:
                player.moveDown()

    keys = pygame.key.get_pressed()
    if(keys[pygame.K_UP]):
        player.moveUp()
    elif(keys[pygame.K_DOWN]):
        player.moveDown()
    elif(keys[pygame.K_LEFT]):
        player.moveLeft()
        print("left")
    elif(keys[pygame.K_RIGHT]):
        player.moveRight()
        print("right")

    if(player.rect.x < 0):
        player.rect.x = 0
    if(player.rect.x > 750):
        player.rect.x = 750
    if(player.rect.y > 550):
        player.rect.y = 550
    # -- Draw everything
    # Clear screen
    screen.fill(WHITE)
    tilefloor = pygame.draw.rect(screen, GREEN, [0, 550, 2000, 50]) # surface, color, x,y,width,height

    # Draw sprites
    all_sprites_list.draw(screen)

    # Flip screen
    pygame.display.flip()

    # Pause
    clock.tick(40)

pygame.quit()
