import pygame
import random

pygame.init()
width, height = 640, 480
window = pygame.display.set_mode((width, height))
robot = pygame.image.load('robot.png')
rock = pygame.image.load('rock.png')
clock = pygame.time.Clock()
x, y = 0, height-robot.get_height()
to_right = False
to_left = False
points = 0
lives = 6
add_num = 2
rock_speed = 1
game_font = pygame.font.SysFont('Arial', 36)
game_over_font = pygame.font.SysFont('Arial', 48)


def get_coords():
    return [random.randint(0, width-rock.get_width()),
            random.randint(-height, 0-rock.get_height())]


rock_coords = [get_coords() for i in range(5)]


while True:
    for event in pygame.event.get():
        # Move robot left / right
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_left = True
            if event.key == pygame.K_RIGHT:
                to_right = True

        # Stop moving robot on key up
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                to_left = False
            if event.key == pygame.K_RIGHT:
                to_right = False

        # Exit program
        if event.type == pygame.QUIT:
            exit()

    # Text
    points_text = game_font.render(f"Points: {points}", True, (255, 0, 0))
    lives_text = game_font.render(f"Lives: {'+'*lives}", True, (255, 0, 0))
    game_over_text = game_over_font.render(
        f"Game Over!", True, (255, 0, 0))
    game_won_text = game_over_font.render(
        f"You Won!!!", True, (255, 0, 0))

    window.fill((0)*3)
    window.blit(robot, (x, y))

    # Game won
    if points >= 100:
        window.blit(game_won_text, (width/2-(game_won_text.get_width())/2,
                                    height/2-(game_won_text.get_height())/2))
        x += add_num
        if x == 0 or x == width - robot.get_width():
            add_num *= -1

    if lives > 0:
        # send rocks down
        if points < 100:
            for c in rock_coords:
                window.blit(rock, c)
                # Rock hits robot
                if (c[1] >= height-(robot.get_height()+rock.get_height()) and
                        x-robot.get_width() <= c[0] <= x+robot.get_width()):
                    points += 1
                    # Increase rock speed for every 10 points
                    if points % 10 == 0:
                        rock_speed += 1
                    c[0], c[1] = get_coords()
                # Rock reaches the bottom of the window
                if c[1] >= height:
                    c[0], c[1] = get_coords()
                    lives -= 1
                # Keep moving down
                else:
                    c[1] += rock_speed
    else:
        # Display game over text
        window.blit(game_over_text, (width/2-(game_over_text.get_width())/2,
                    height/2-(game_over_text.get_height())/2))
        # bounce robot between sides
        x += add_num
        if x == 0 or x == width - robot.get_width():
            add_num *= -1

    # Disallow robot movement outside the window
    if to_right and x <= width - robot.get_width():
        x += 6
    if to_left and x >= 0:
        x -= 6

    pygame.display.set_caption('Catching Rocks')
    window.blit(points_text, (width-points_text.get_width(), 0))
    window.blit(lives_text, (0, 0))

    pygame.display.flip()
    clock.tick(60)
