import pygame
import random

pygame.init()
robot = pygame.image.load('robot.png')
width, height, robot_width, robot_height = 640, 480, robot.get_width(), robot.get_height()
window = pygame.display.set_mode((width, height))
x, y = width/2-(robot_width/2), height/2-(robot_height/2)


while True:
    for event in pygame.event.get():
        if (event.type == pygame.MOUSEBUTTONDOWN and
                x <= event.pos[0] <= x+robot_width and
                y <= event.pos[1] <= y+robot_height
            ):
            x = random.randint(0, width-robot_width)
            y = random.randint(0, height-robot_height)

        if event.type == pygame.QUIT:
            exit()

    window.fill((0)*3)
    window.blit(robot, (x, y))
    pygame.display.flip()
