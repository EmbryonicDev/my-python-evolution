import pygame
import random

pygame.init()

window = pygame.display.set_mode((640, 480))
robot = pygame.image.load('robot.png')
x = 0
y = 0
x_velocity = 1
y_velocity = 1
clock = pygame.time.Clock()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill((0)*3)
    window.blit(robot, (x, y))
    pygame.display.flip()

    horizontal = True
    if horizontal:
        x += x_velocity
        if x_velocity > 0 and x + robot.get_width() >= 640:
            horizontal = False
            x_velocity = -x_velocity
            print('Horizontal is on: ', horizontal)
        if x_velocity < 0 and x <= 0:
            horizontal = False
            x_velocity = -x_velocity
            print('Horizontal is on: ', horizontal)
    else:
        y += y_velocity
        if y_velocity > 0 and y + robot.get_width() >= 640:
            horizontal = True
            y_velocity = -y_velocity
            print('Horizontal is on: ', horizontal)
        if y_velocity < 0 and y <= 0:
            horizontal = True
            y_velocity = -y_velocity
            print('Horizontal is on: ', horizontal)

    # x += velocity
    # if velocity > 0 and x + robot.get_width() >= 640:
    #     velocity = -velocity
    # if velocity < 0 and x <= 0:
    #     velocity = -velocity

    clock.tick(450)
