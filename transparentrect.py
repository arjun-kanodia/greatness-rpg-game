import pygame
import sys

pygame.init
screen=pygame.display.set_mode((800,600))
pygame.display.set_caption('Transparent Rectangle Example')

WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
rect_surface=pygame.Surface((100,100), pygame.SRCALPHA)
pygame.draw.rect(rect_surface, (155, 0, 100, 0), (0, 0, 200, 100))


running = True
while running:
    screen.fill(GREEN)

    screen.blit(rect_surface, (255, 255))

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit