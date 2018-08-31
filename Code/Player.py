import pygame
import Image_File as IF
import Globals as GB
from Globals import Dir
import Bullet as BT


class Player(pygame.sprite.Sprite):
    def __init__(self, xi, yi):
        pygame.sprite.Sprite.__init__(self)
        self.image = IF.SHIP
        self.rect = self.image.get_rect()
        self.rect.center = (xi, yi)
        self.speedx = 0
        self.speedy = 0
        self.accelx = 0
        self.accely = 0
        self.dir = Dir.E

    def update(self):
        ks = pygame.key.get_pressed()
        self.speedx = 0
        self.speedy = 0
        if ks[pygame.K_a]:
            self.speedx = -GB.P_SPEED
        elif ks[pygame.K_d]:
            self.speedx = GB.P_SPEED
        if ks[pygame.K_w]:
            self.speedy = -GB.P_SPEED
        elif ks[pygame.K_s]:
            self.speedy = GB.P_SPEED

        self.rect.centerx += self.speedx
        self.rect.centery += self.speedy

        self.imaging()

        if self.rect.right > GB.WIDTH - GB.THICK:
            self.rect.right = GB.WIDTH - GB.THICK
        if self.rect.left < GB.THICK:
            self.rect.left = GB.THICK
        if self.rect.top < GB.THICK:
            self.rect.top = GB.THICK
        if self.rect.bottom > GB.HEIGHT - GB.THICK:
            self.rect.bottom = GB.HEIGHT - GB.THICK

    def shoot(self):
        b = BT.Bullet(self.rect.center, self.dir)
        return b

    def imaging(self):
        x = self.speedx
        y = self.speedy
        s = GB.P_SPEED
        c = self.rect.center
        f = False
        if x == s:
            if y == 0:
                ang = 0
                self.dir = Dir.E
            elif y == -s:
                ang = 45
                self.dir = Dir.NE
            else:
                ang = -45
                self.dir = Dir.SE
        elif x == -s:
            f = True
            if y == 0:
                ang = 180
                self.dir = Dir.W
            elif y == -s:
                ang = 135
                self.dir = Dir.NW
            else:
                ang = 225
                self.dir = Dir.SW
        else:
            if y == -s:
                ang = 90
                self.dir = Dir.N
            elif y == s:
                ang = -90
                self.dir = Dir.S
            else:
                ang = 360
        if ang < 360:
            if f:
                self.image = pygame.transform.flip(IF.SHIP, False, True)
                self.image = pygame.transform.rotate(self.image, ang)
            else:
                self.image = pygame.transform.rotate(IF.SHIP, ang)
            self.rect = self.image.get_rect()
            self.rect.center = c
