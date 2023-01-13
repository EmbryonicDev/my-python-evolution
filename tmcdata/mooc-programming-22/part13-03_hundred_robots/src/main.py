import pygame

pygame.init()
screen = pygame.display.set_mode((640, 480))

robot = pygame.image.load('robot.png')

screen.fill((0, 0, 0))

y = 100
x = robot.get_width()
for i in range(10):
    for j in range(10):
        screen.blit(robot, (x+40*j, y))
    x += 10
    y += 20

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
