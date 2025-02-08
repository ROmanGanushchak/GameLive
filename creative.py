import pygame
from collections import deque
from setting import *


class Creative:
    def __init__(self, state: GameState):
        self.state: GameState = state
        self.field = state.field
        self.field_copy = state.field_copy
    
    def clear(self):
        for i in range(height):
            for a in range(width):
                self.field[i][a] = 0

    def save(self):
        for i in range(height):
            for a in range(width):
                self.field_copy[i][a] = self.field[i][a]

    def restore(self):
        for i in range(height):
            for a in range(width):
                self.field[i][a] = self.field_copy[i][a]
    
    def fill(self, elem):
        x, y = pygame.mouse.get_pos()
        pos_x, pos_y = x // squer_size, y // squer_size
        if self.field[pos_y][pos_x] == elem:
            return

        self.field[pos_y][pos_x] = elem
        check = deque([[pos_y, pos_x]])
        mas_neighbor = [(1, 0), (0, 1), (0, -1), (-1, 0)]
        if elem == 0:
            mas_neighbor.extend([(1, 1), (-1, 1), (1, -1), (-1, -1)])
        set_elem = {pos_y * width + pos_x}
        while check:
            deleten = check.popleft()
            for i in mas_neighbor:
                point = [deleten[0] + i[0], deleten[1] + i[1]]
                set_point = point[0] * width + point[1]
                if 0 <= point[0] < height and 0 <= point[1] < width:
                    if set_point not in set_elem and self.field[point[0]][point[1]] == int(not elem):
                        self.state.field[point[0]][point[1]] = elem
                        check.append(point)