import os
import pygame
from map import Map
from player import Player

pygame.init()

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Unnamed Pygame")

DARK_GREY = (50,50,50)

FPS = 60

map = Map(7, 7, [420, 100])
group = pygame.sprite.Group(
    Player(1.5, pygame.Color('red'), map.map[0].x+35, map.map[0].y+15),
    Player(3.0, pygame.Color('orange'), map.map[0].x+35, map.map[0].y+15),
    Player(4.5, pygame.Color('dodgerblue'), map.map[0].x+35, map.map[0].y+15))


def draw_window():
    WIN.fill(DARK_GREY)
    map.update(map)
    map.draw(map, WIN)

    group.update()
    group.draw(WIN)
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
            if event.type == pygame.MOUSEBUTTONDOWN:
                for player in group.sprites():
                    player.set_target(pygame.mouse.get_pos())
        draw_window()
    main()


if __name__ == "__main__":
    main()