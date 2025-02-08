import copy
from setting import *

class GameUpdate:
    def __init__(self, state: GameState):
        self.field = state.field
    
    def is_next_alive(self, alive_neighbors, sqear):
        if sqear == 0 and alive_neighbors == 3:
            return 1
        if sqear == 1 and alive_neighbors == 3:
            return 1
        if sqear == 1 and alive_neighbors == 2:
            return 1
        return 0

    def update_map(self) -> None:
        field_now = copy.deepcopy(self.field)
        for i in range(height):
            for a in range(width):
                alive_neighbors = 0
                for neighbor in neighbors:
                    if 0 <= i + neighbor[0] < height and 0 <= a + neighbor[1] < width:
                        if field_now[i + neighbor[0]][a + neighbor[1]] == 1:
                            alive_neighbors += 1
                self.field[i][a] = self.is_next_alive(alive_neighbors, field_now[i][a])