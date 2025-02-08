from pygame.mouse import get_pos
from setting import *
from creative import Creative

class MouseController:
    def __init__(self, state: GameState):
        self.creative = Creative(state)
        self.left_mouse_down, self.rigth_mouse_down = False, False
        self.state = state

    def set_rigth_mouse_down(self, elem):
        self.rigth_mouse_down = elem

    def change_live(self, num):
        mouse_pos = get_pos()
        self.state.field[mouse_pos[1] // squer_size][mouse_pos[0] // squer_size] = num

    def update(self):
        if self.rigth_mouse_down:
            if self.state.press_type == PressingType.DRAW:
                self.change_live(0)
            else:
                self.creative.fill(0)
        elif self.left_mouse_down:
            if self.state.press_type == PressingType.DRAW:
                self.change_live(1)
            else:
                self.creative.fill(1)
