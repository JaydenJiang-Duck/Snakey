import pygame
import sys
import random

pygame.init()

W, H = 800, 800
FONT = pygame.font.SysFont("Arial", 20)

screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("Simulation")
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    clock.tick(10)