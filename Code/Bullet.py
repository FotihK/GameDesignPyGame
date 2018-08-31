import pygame
import Image_File as IF
import Globals as GB
from Globals import Dir


class Bullet(pygame.sprite.Sprite):
    def __init__(self, coord, dir):
        pygame.sprite.Sprite.__init__(self)
        self.image = IF.PEW
        self.rect = self.image.get_rect()
        self.rect.center = coord
        self.speed = [0, 0]
        print("B: ", dir)
        if dir == Dir.E:
            self.speed = [GB.B_SPEED, 0]
        elif dir == Dir.NE:
            self.speed = [GB.B_SPEED, -GB.B_SPEED]
        elif dir == Dir.N:
            self.speed = [0, -GB.B_SPEED]
        elif dir == Dir.NW:
            self.speed = [-GB.B_SPEED, -GB.B_SPEED]
        elif dir == Dir.W:
            self.speed = [-GB.B_SPEED, 0]
        elif dir == Dir.SW:
            self.speed = [-GB.B_SPEED, GB.B_SPEED]
        elif dir == Dir.S:
            self.speed = [0, GB.B_SPEED]
        elif dir == Dir.SE:
            self.speed = [GB.B_SPEED, GB.B_SPEED]

    def update(self):
        self.rect.centerx += self.speed[0]
        self.rect.centery += self.speed[1]

        if self.rect.right > GB.WIDTH - GB.THICK \
                or self.rect.left < GB.THICK or self.rect.top < GB.THICK or \
                self.rect.bottom > GB.HEIGHT - GB.THICK:
            self.kill()
