import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, speed, color, x, y):
        super().__init__()
        ## self.image is a transparent background rectangle on which to paint the player
        self.image = pygame.Surface((10, 10))
        self.image.set_colorkey((12,34,56))
        self.image.fill((12,34,56))
        ## Player drawn using passed colour, with a width radius of 3
        pygame.draw.circle(self.image, color, (5, 5), 3)
        ## A rectangle to reference the player with
        self.rect = self.image.get_rect()

        ## Initial position and speed setting
        self.pos = pygame.Vector2(x, y)
        self.set_target((x, y))
        self.speed = speed

    def set_target(self, pos):
        "Set the destination"
        self.target = pygame.Vector2(pos)

    def update(self):
        "Update the location and actually move"
        move = self.target - self.pos
        move_length = move.length()

        if move_length < self.speed:
            self.pos = self.target
        elif move_length != 0:
            move.normalize_ip()
            move = move * self.speed
            self.pos += move

        ## Moving the object using a built in rect function
        self.rect.topleft = list(int(v) for v in self.pos)