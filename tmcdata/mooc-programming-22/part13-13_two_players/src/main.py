import pygame

pygame.init()

width, height = 2160, 1440
window = pygame.display.set_mode((width, height))

robot = pygame.image.load('robot.png')
clock = pygame.time.Clock()

robot1_coords = [width*0.25, height*0.25-(robot.get_height()/2)]
robot2_coords = [width*0.75, height*0.75-(robot.get_height()/2)]
r1_right, r1_left, r1_up, r1_down, r2_right, r2_left, r2_up, r2_down = False, False, False, False, False, False, False, False


while True:
    def move_robot(robot_coords: list, left, right, up, down):
        if right and robot_coords[0] <= width - robot.get_width():
            robot_coords[0] += 2
        if left and robot_coords[0] >= 0:
            robot_coords[0] -= 2
        if down and robot_coords[1] <= height - robot.get_height():
            robot_coords[1] += 2
        if up and robot_coords[1] >= 0:
            robot_coords[1] -= 2

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            # Move robot1 up / down / right / left on key down
            if event.key == pygame.K_LEFT:
                r2_left = True
            if event.key == pygame.K_RIGHT:
                r2_right = True
            if event.key == pygame.K_UP:
                r2_up = True
            if event.key == pygame.K_DOWN:
                r2_down = True
            # Move robot2 up / down / right / left on key down
            if event.key == pygame.K_a:
                r1_left = True
            if event.key == pygame.K_d:
                r1_right = True
            if event.key == pygame.K_w:
                r1_up = True
            if event.key == pygame.K_s:
                r1_down = True

        # Stop moving robot on key up
        if event.type == pygame.KEYUP:
            # Robot1
            if event.key == pygame.K_LEFT:
                r2_left = False
            if event.key == pygame.K_RIGHT:
                r2_right = False
            if event.key == pygame.K_UP:
                r2_up = False
            if event.key == pygame.K_DOWN:
                r2_down = False
            # Robot2
            if event.key == pygame.K_a:
                r1_left = False
            if event.key == pygame.K_d:
                r1_right = False
            if event.key == pygame.K_w:
                r1_up = False
            if event.key == pygame.K_s:
                r1_down = False

    move_robot(robot1_coords, r1_left, r1_right, r1_up, r1_down)
    move_robot(robot2_coords, r2_left, r2_right, r2_up, r2_down)

    window.fill((0)*3)
    window.blit(robot, (robot1_coords))
    window.blit(robot, (robot2_coords))

    pygame.display.flip()
    clock.tick(60)
