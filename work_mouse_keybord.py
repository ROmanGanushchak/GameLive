import pygame
from setting import get_press_mod_left, get_menu, set_press_mod_left, get_press_mod_rigth, set_press_mod_rigth
pygame.init()

class Work_mouse:
    def __init__(self, map_live, size_squer):
        self.left_mouse_down, self.rigth_mouse_down = False, False
        self.map_live, self.size_squer = map_live, size_squer

    def set_rigth_mouse_down(self, elem):
        self.rigth_mouse_down = elem

    def change_live(self, num):
        mouse_pos = pygame.mouse.get_pos()
        if self.map_live[mouse_pos[1] // self.size_squer][mouse_pos[0] // self.size_squer] != num:
            self.map_live[mouse_pos[1] // self.size_squer][mouse_pos[0] // self.size_squer] = num

    def main(self):
        if self.rigth_mouse_down:
            if get_press_mod_rigth() == 0:
                self.change_live(0)
            else:
                get_menu().do_filling(0)
                get_menu().del_object()
                # set_press_mod_rigth(0)
        else:
            if get_press_mod_left() == 0:
                self.change_live(1)
            else:
                get_menu().do_filling(1)
                get_menu().fill()
