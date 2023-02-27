import pygame
import math
import random
from datetime import datetime

    # solid red circle
width, height = 2000, 2000
center = width/2, height/2
radius = center[1]
radius_list = {'sec': radius*0.8, 'min': radius *
               0.8, 'hour': radius*.55, 'digit': radius - 30}

pygame.init()
window = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
# for hours, minutes and seconds
clock60 = dict(zip(range(60), range(0, 360, 6)))


def get_clock_pos(clock_dict, clock_hand, key):
    x = center[0] + radius_list[key] * \
        math.cos(math.radians(clock_dict[clock_hand]) - math.pi / 2)
    y = center[1] + radius_list[key] * \
        math.sin(math.radians(clock_dict[clock_hand]) - math.pi / 2)
    return x, y


def get_random_coords():
    return (random.randint(0, 255), random.randint(
        0, 255), random.randint(0, 255))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("You've quit the game...")
            exit()

    window.fill(get_random_coords())

    # Main circle
    pygame.draw.circle(window, (get_random_coords()), (center), radius*0.95)
    # Smaller circle for watch face
    pygame.draw.circle(window, (get_random_coords()), (center), radius*0.925)
    # Small circle in middle
    pygame.draw.circle(window, (get_random_coords()), center, radius*0.05)

    now = datetime.now()
    hour, minute, second = ((now.hour % 12) * 5 +
                            now.minute // 12) % 60, now.minute, now.second
    # seconds hand
    pygame.draw.line(window, (get_random_coords()), center,
                     get_clock_pos(clock60, second, 'sec'), 3)
    # minutes hand
    pygame.draw.line(window, (get_random_coords()), center,
                     get_clock_pos(clock60, minute, 'min'), 4)
    # hour hand
    pygame.draw.line(window, (get_random_coords()), center,
                     get_clock_pos(clock60, hour, 'hour'), 6)

    pygame.display.flip()
    clock.tick(1)
