import pygame
from setting import *
pygame.init()

class Output:
    def __init__(self, state: GameState, sc):
        self.sc = sc
        self.state = state
        self.field = state.field

    def render_field(self):
        for i in range(height):
            for a in range(width):
                if self.field[i][a]:
                    pygame.draw.rect(self.sc, (100, 255, 255),
                                     (a * squer_size + 1, i * squer_size + 1, squer_size - 1, squer_size - 1))

    def __render_lines(self, sc):
        for y in range(height):
            pygame.draw.line(sc, (75, 75, 75), (0, y * squer_size), (width * squer_size, y * squer_size), 1)
        for x in range(width):
            pygame.draw.line(sc, (75, 75, 75), (x * squer_size, 0), (x * squer_size, height * squer_size), 1)

    def render(self):
        self.render_field()
        self.__render_lines(self.sc)
