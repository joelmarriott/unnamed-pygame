import pygame

class Tile:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        # Make rect to check for rough collision
        self.rect = pygame.Rect(x, y, 78, 39)

        self.left = False
        self.right = False
        self.selected = False

    def update(self, map, move):
        "Check for hover and set selected if so"
        self.selected = False
        x, y = pygame.mouse.get_pos()
        if self.rect.collidepoint((x, y)):
            # The mask needs relative coordinates
            x -= self.rect.x
            y -= self.rect.y
            ## Exact mask of image using (lack of) transparency
            if map.top_image_mask.get_at((x, y)):
                self.selected = True
                move = (self.rect.x+30, self.rect.y+15)
        if move:
            return move
        else:
            return False

    def draw(self, map, screen):
        "Draw the tile on the screen"
        pos = self.rect.x, self.rect.y
        screen.blit(map.top_image, pos)
        if self.left:
            screen.blit(map.left_image, pos)
        if self.right:
            screen.blit(map.right_image, pos)
        if self.selected:
            screen.blit(map.cursor, pos)