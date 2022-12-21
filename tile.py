import pygame

class Tile:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        # make rect to check for rough collision
        self.rect = pygame.Rect(x, y, 40, 48)

        self.left = False
        self.right = False
        self.selected = False

    def update(self, map):
        self.selected = False
        x, y = pygame.mouse.get_pos()
        if self.rect.collidepoint((x, y)):
            # the mask needs relative coordinates
            x -= self.rect.x
            y -= self.rect.y
            if map.top_image_mask.get_at((x, y)):
                self.selected = True

    def draw(self, map, screen):
        pos = self.rect.x, self.rect.y
        screen.blit(map.top_image, pos)
        if self.left:
            screen.blit(map.left_image, pos)
        if self.right:
            screen.blit(map.right_image, pos)
        if self.selected:
            screen.blit(map.cursor, pos)