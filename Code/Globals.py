from enum import Enum

WIDTH = 1080
HEIGHT = 720
FPS = 60
# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
CYAN = (0, 255, 255)

THICK = 10
E_SPEED = 3
P_ACCEL = 0.1
P_SPEED = 4
B_SPEED = 10

class Dir(Enum):
    N = 90
    NE = 45
    E = 0
    SE = 315
    S = 270
    SW = 225
    W = 180
    NW = 135