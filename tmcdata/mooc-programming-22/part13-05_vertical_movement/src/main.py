import pygame
import random

pygame.init()

window = pygame.display.set_mode((640, 480))
robot = pygame.image.load('robot.png')
x = 0
y = 0
velocity = 1
clock = pygame.time.Clock()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill((0)*3)
    window.blit(robot, (x, y))
    pygame.display.flip()

    x += velocity
    if velocity > 0 and x + robot.get_width() >= 640:
        velocity = -velocity
    if velocity < 0 and x <= 0:
        velocity = -velocity

    clock.tick(60)
