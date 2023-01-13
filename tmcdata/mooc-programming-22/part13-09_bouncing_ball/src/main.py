import pygame
import random

pygame.init()

# Randomly choose default or random mode
is_random = random.choice([True, False])

# Shared variables
width, height, = 640, 480
window = pygame.display.set_mode((width, height))
ball = pygame.image.load('ball.png')

# Default mode settings
screen_color = (0, 0, 0)
x, y = width / 2 - ball.get_width(), height / 2 - ball.get_height()
x_velocity, y_velocity = 1, 1
console_message = 'Default mode was randomly selected!'
clock = pygame.time.Clock()

# Random mode settings
if is_random:
    x = random.randint(0, width - ball.get_width())
    y = random.randint(0, height - ball.get_width())
    screen_color = (
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255)
    )
    x_velocity, y_velocity = random.choice([-1, 1]), random.choice([-1, 1])
    console_message = 'Random mode was randomly selected!'

print(console_message)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill(screen_color)
    window.blit(ball, (x, y))
    pygame.display.flip()

    # Change direction if ball hits side
    if x == 0 or x + ball.get_width() == width:
        x_velocity = - x_velocity
    if y == 0 or y + ball.get_width() == height:
        y_velocity = - y_velocity

    x += x_velocity
    y += y_velocity
    clock.tick(140)
