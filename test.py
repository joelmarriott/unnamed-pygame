import pygame
from pygame.locals import *
from map import Map

pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((640, 480))
map = Map(15, 15, [320, 100])
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    screen.fill((230, 250, 255))

    map.update(map)
    map.draw(map, screen)

    pygame.display.flip()
    clock.tick(60) # limit the framerate
