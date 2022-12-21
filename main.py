import os
import pygame

pygame.init()

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Unnamed Pygame")

TILE = pygame.image.load(os.path.join("Assets", "Tile.png"))

DARK_GREY = (50,50,50)

FPS = 60


def draw_world():
    draw_tile_line(527,137,3)
    draw_tile_line(452,137,5)
    draw_tile_line(300,175,7)
    draw_tile_line(338,156,7)
    draw_tile_line(376,137,7)
    draw_tile_line(300,213,5)
    draw_tile_line(300,251,3)


def draw_tile_line(x, y, amount):
    tiles = 0
    while tiles < amount:
        place_tile(x, y)
        tiles += 1
        x += 38
        y += 19


def place_tile(x,y):
    WIN.blit(TILE, (x, y))


def draw_window():
    WIN.fill(DARK_GREY)
    draw_world()
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