import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))
robot = pygame.image.load('robot.png')
x1, y1, x2, y2, velocity1, velocity2 = 0, 40, 0, 140, 1, 2
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill((0)*3)
    window.blit(robot, (x1, y1))
    window.blit(robot, (x2, y2))
    pygame.display.flip()

    x1 += velocity1
    if x1 == 0 or x1 + robot.get_width() == 640:
        velocity1 = -velocity1
    x2 += velocity2
    if x2 == 0 or x2 + robot.get_width() == 640:
        velocity2 = -velocity2

    clock.tick(60)
