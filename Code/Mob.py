import pygame
import random as rd
import Globals as GB

class Mob(pygame.sprite.Sprite):

    def __init__(self, xi, yi, color, size=20):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((size, size))
        self.size = size
        self.color = color
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = (xi, yi)
        self.speed = [0, 0]
        self.max = 0
        if self.size != 0:
            self.max = round(GB.E_SPEED * 15/self.size)
        else: self.max = 1
        self.rng_speed()
        self.curr_time = 0
        self.last_time = 0

    def update(self):
        self.curr_time = pygame.time.get_ticks()

        if (self.curr_time - self.last_time) / 1000 > rd.uniform(1.0, 5.0):
            self.rng_speed()
            self.last_time = self.curr_time

        self.rect.centerx += self.speed[0]
        self.rect.centery += self.speed[1]

        if self.rect.right > GB.WIDTH - GB.THICK:
            self.rect.right = GB.WIDTH - GB.THICK
            self.rng_speed(1)
        if self.rect.left < GB.THICK:
            self.rect.left = GB.THICK
            self.rng_speed(2)
        if self.rect.top < GB.THICK:
            self.rect.top = GB.THICK
            self.rng_speed(3)
        if self.rect.bottom > GB.HEIGHT - GB.THICK:
            self.rect.bottom = GB.HEIGHT - GB.THICK
            self.rng_speed(4)

    def rng_speed(self, sd=0):
        while True:
            x = rd.randint(-1, 1) * self.max
            y = rd.randint(-1, 1) * self.max
            s = [x, y]
            if s != self.speed and s != [0, 0]:
                if ((sd == 0) or (sd == 1 and s[0] < 0) or (sd == 2 and s[0] > 0) or
                        (sd == 3 and s[1] > 0) or (sd == 4 and s[1] < 0)):
                    self.speed = s
                    break

    def is_colliding(self, sprite):
        if self.rect.colliderect(sprite.rect):
            if isinstance(sprite, Mob):
                self.rng_speed()
            else:
                return True

    def split(self):
        if self.size > 20:
            new_size = self.size // 2
            new_size = new_size if new_size >= 20 else 20
            m1 = Mob(self.rect.centerx, self.rect.centery, self.color, new_size)
            m2 = Mob(self.rect.centerx, self.rect.centery, self.color, new_size)
            return [m1, m2]
