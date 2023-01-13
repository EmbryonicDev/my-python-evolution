import pygame
import random

pygame.init()
screen = pygame.display.set_mode((640, 480))
screen.fill((0, 0, 0))
robot = pygame.image.load('robot.png')
width, height = robot.get_width(), robot.get_height()


def get_coordinates():
    return (random.randint(0, 640-width), random.randint(0, 480-height))


for i in range(1000):
    screen.blit(robot, (get_coordinates()))

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
