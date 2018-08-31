import pygame
from os import path as p

BASE_DIR = p.abspath(p.join(p.dirname(__file__), '..'))
ART_DIR = p.join(BASE_DIR, "Art")

HEART = pygame.image.load(p.join(ART_DIR, "hart.png"))
SHIP = pygame.transform.scale(pygame.image.load(p.join(ART_DIR, "tiny_ship.png")), (50, 50))
PEW = pygame.transform.scale2x(pygame.image.load(p.join(ART_DIR, "Pew.png")))
