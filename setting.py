import random
from array import array
from enum import Enum

FPS = 120
INIT_ALIVE_SQUERE_CNT = 5000

width = 190
height = 100
squer_size = 8
geometry_window = [width * squer_size, height * squer_size]
neighbors = [(0, 1), (1, 0), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, -1), (-1, 1)]

class PressingType(Enum):
    DRAW = 1
    FILL = 2

class GameState:
    def __init__(self):
        self.field = [array("b", [0] * width) for i in range(height)]
        self.field_copy = [array("b", [0] * width) for i in range(height)]
        self.menu = None
        self.press_type = PressingType.DRAW

        for _ in range(INIT_ALIVE_SQUERE_CNT):
            self.field[random.randint(0, height-1)][random.randint(0, width-1)] = 1