import pygame

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)


def draw_stick_figure(screen, x, y):
    # Head
    pygame.draw.ellipse(screen, BLACK, [1 + x, y, 10, 10], 0)

    # Legs
    pygame.draw.line(screen, BLACK, [5 + x, 17 + y], [10 + x, 27 + y], 2)
    pygame.draw.line(screen, BLACK, [5 + x, 17 + y], [x, 27 + y], 2)

    # Body
    pygame.draw.line(screen, RED, [5 + x, 17 + y], [5 + x, 7 + y], 2)

    # Arms
    pygame.draw.line(screen, RED, [5 + x, 7 + y], [9 + x, 17 + y], 2)
    pygame.draw.line(screen, RED, [5 + x, 7 + y], [1 + x, 17 + y], 2)


# Setup
pygame.init()

# Set the width and height of the screen [width,height]
size = [700, 500]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Game")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Hide the mouse cursor
pygame.mouse.set_visible(0)

# Speed in pixels per frame
x_speed = 0
y_speed = 0

# Current position
x_coord = 10
y_coord = 10

state = "PLAYING"

# -------- Main Program Loop -----------
while not done:
    # --- Event Processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            # User pressed down on a key
    if(state == "PLAYING"):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            x_speed = 1
            y_speed = 0
        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            x_speed = -1
            y_speed = 0
        if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            x_speed = 0
            y_speed = -1
        if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            x_speed = 0
            y_speed = 1

        if event.type == pygame.KEYUP and event.key == pygame.K_RIGHT:
            x_speed = 0
            y_speed =0
        if event.type == pygame.KEYUP and event.key == pygame.K_LEFT:
            x_speed = 0
            y_speed =0
        if event.type == pygame.KEYUP and event.key == pygame.K_UP:
            x_speed = 0
            y_speed =0
        if event.type == pygame.KEYUP and event.key == pygame.K_DOWN:
            x_speed = 0
            y_speed =0
    # --- Game Logic

    # Move the object according to the speed vector.
    x_coord += (x_speed * 5)
    y_coord += (y_speed * 5)

    # --- Drawing Code

    # First, clear the screen to WHITE. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(WHITE)

    draw_stick_figure(screen, x_coord, y_coord)


    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # Limit frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()

