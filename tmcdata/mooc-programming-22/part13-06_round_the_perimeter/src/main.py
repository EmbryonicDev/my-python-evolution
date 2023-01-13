import pygame
import random

pygame.init()

window = pygame.display.set_mode((640, 480))
robot = pygame.image.load('robot.png')
x, y = 0, 0
x_velocity, y_velocity = 1, 1
horizontal = True
clock = pygame.time.Clock()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill((0)*3)
    window.blit(robot, (x, y))
    pygame.display.flip()

    if horizontal:
        x += x_velocity
        if (x_velocity > 0 and x + robot.get_width() >= 640 or
                x_velocity < 0 and x <= 0):
            horizontal = False
            x_velocity = -x_velocity
    else:
        y += y_velocity
        if (y_velocity > 0 and y + robot.get_height() >= 480 or
                y_velocity < 0 and y <= 0):
            horizontal = True
            y_velocity = -y_velocity

    clock.tick(60)
