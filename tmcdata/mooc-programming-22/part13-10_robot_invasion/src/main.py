import pygame
import random

pygame.init()

width = 640
height = 480
window = pygame.display.set_mode((width, height))
robot = pygame.image.load('robot.png')
clock = pygame.time.Clock()


# Get random coordinates for individual bot (outside / above the window)
def get_coords():
    return [random.randint(0, width-robot.get_width()),
            random.randint(-height, 0-robot.get_height())]


# Get random x / y coordinates for first 10 bots
random_coords = [get_coords() for i in range(10)]


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill((0)*3)

    for c in random_coords:
        window.blit(robot, c)
        # Bot reaches the bottom of the window
        if c[1] + robot.get_height() == height:
            # Determine horizontal direction
            if c[0] > width / 2:
                # Go right if bot is on right side of window
                c[0] += 1
            else:
                # Go left if bot is on left side of window
                c[0] -= 1
            # Get new random coordinates when bot exits the window
            if c[0] > width or c[0] < 0 - robot.get_width():
                c[0], c[1] = get_coords()
        # Keep moving down
        else:
            c[1] += 1

    pygame.display.flip()
    clock.tick(60)
