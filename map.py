import pygame
import os
from tile import Tile

class Map:
    def __init__(self, width, height, origin):
        self.top_image = pygame.image.load(os.path.join('Assets', 'top.png'))
        self.left_image = pygame.image.load(os.path.join('Assets', 'left.png'))
        self.right_image = pygame.image.load(os.path.join('Assets', 'right.png'))
        self.cursor = pygame.image.load(os.path.join('Assets', 'cursor.png'))
        # create the Mask for the top image
        # (only activate when the selected pixel is non-transparent)
        self.top_image_mask = pygame.mask.from_surface(self.top_image)

        origin[0] -= 20*width
        origin[1] += 5*height
        self.map = []
        for x in range(width):
            for y in range(height):
                tile_x, tile_y = origin
                tile_x += 20*x + 20*y
                tile_y += 10*y - 10*x
                self.map.append(Tile(tile_x, tile_y))
                # draw the sides textures if needed
                if not x:
                    self.map[-1].left = True
                if y+1 == height:
                    self.map[-1].right = True

    def update(self, map):
        for tile in self.map:
            tile.update(map)

    def draw(self, map, screen):
        for tile in sorted(self.map, key=lambda tile: tile.selected):
            tile.draw(map, screen)