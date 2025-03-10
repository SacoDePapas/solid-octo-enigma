import pygame
import sys
from grid import Grid
from blocks import *


pygame.init()
dark_blue = (44,44,127)


screen = pygame.display.set_mode((300,600))
pygame.display.set_caption("Tetris-peer-to-peer")
clock = pygame.time.Clock()

game_grid = Grid()

block = Tblock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(dark_blue)
    game_grid.draw(screen)
    block.draw(screen)

    pygame.display.update()
    clock.tick(60)