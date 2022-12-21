import pygame
import os
from tile import Tile

class Map:
    def __init__(self, width, height, origin):
        self.top_image = pygame.image.load(os.path.join('Assets', 'Tile.png'))
        self.left_image = pygame.image.load(os.path.join('Assets', 'TileLeft.png'))
        self.right_image = pygame.image.load(os.path.join('Assets', 'TileRight.png'))
        self.cursor = pygame.image.load(os.path.join('Assets', 'Hover.png'))
        # Create the Mask for the tile
        # (only activate when the selected pixel is non-transparent)
        self.top_image_mask = pygame.mask.from_surface(self.top_image)

        ## x and y co-ordinates of the origin adjusted by the amount of tiles it is drawing
        origin[0] -= 38*width
        origin[1] += 19*height
        self.map = []
        for x in range(width):
            for y in range(height):
                tile_x, tile_y = origin
                ## Witchcraft to decide tile placement
                tile_x += 38*x + 38*y
                tile_y += 19*y - 19*x
                self.map.append(Tile(tile_x, tile_y))
                ## Draw the side textures if needed
                if not x:
                    self.map[-1].left = True
                if y+1 == height:
                    self.map[-1].right = True

    def update(self, map):
        "Check/Update state of all existing tiles"
        move = False
        for tile in self.map:
            move = tile.update(map, move)
        return move

    def draw(self, map, screen):
        "Re-draw tiles onto the screen"
        for tile in sorted(self.map, key=lambda tile: tile.selected):
            tile.draw(map, screen)

    def get_target(self, pos):
        "Find a valid target tile"
        x, y = pos
        for tile in self.map:
            if x in range(tile.x-39, tile.x+39):
                if y in range(tile.y-20, tile.y+20):
                    pos = (tile.x, tile.y)
        return pos