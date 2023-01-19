import pygame

pygame.init()
display = pygame.display.set_mode((640, 480))
display.fill((0, 0, 0))
pygame.display.set_caption("Great Adventure")

# Shapes
pygame.draw.rect(display, (0, 255, 0), (50, 100, 200, 250))
pygame.draw.circle(display, (255, 0, 0), (200, 150), 40)
pygame.draw.line(display, (0, 0, 255), (80, 120), (300, 160), 2)

# Text
game_font = pygame.font.SysFont('Arial', 24)
text = game_font.render('Moikka!', True, (255, 0, 0))
display.blit(text, (100, 50))

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
