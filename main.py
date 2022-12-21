import os
import pygame
from map import Map

pygame.init()

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Unnamed Pygame")

DARK_GREY = (50,50,50)

FPS = 60

map = Map(7, 7, [420, 100])

def draw_window():
    WIN.fill(DARK_GREY)
    map.update(map)
    map.draw(map, WIN)
    pygame.display.update()


def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        draw_window()
    
    main()


if __name__ == "__main__":
    main()