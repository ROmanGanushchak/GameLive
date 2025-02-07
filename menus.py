import pygame
from rule_live import Live_rules_check
from Buttons import *
import setting as s
from collections import deque

class Live:
    def __init__(self, map_live, kil_squer_h, kil_squer_w, mas_neghbor, map_live_copy):
        self.map_live, self.kil_squer_h, self.kil_squer_w, self.mas_neghbor,\
        self.map_live_copy = map_live, kil_squer_h, kil_squer_w, mas_neghbor, map_live_copy
        self.mas_cord_buttons = [[10, 10]]
        self.mas_text_button = ["creative"]
        self.mas_funcion = [self.button_creative]
        self.mas_button, self.mas_surface_but = [], []
        for i in range(len(self.mas_cord_buttons)):
            self.mas_button.append(
                Button(self.mas_cord_buttons[i][0], self.mas_cord_buttons[i][1], self.mas_text_button[i], 1,
                       self.mas_funcion[i]))
            self.mas_surface_but.append(self.mas_button[i].creat_surface_button())
    
    def button_creative(self):
        s.set_menu(Creat_live)

    def check_buttons(self, cord_mouse_x, cord_mouse_y):
        for i in self.mas_button:
            if i.check_click_but(cord_mouse_x, cord_mouse_y):
                return True
        return

    def operecion(self):
        live = Live_rules_check(self.map_live, self.kil_squer_h, self.kil_squer_w, self.mas_neghbor)
        live.search_map()

    def output_buttons(self, sc):
        for i in range(len(self.mas_cord_buttons)):
            sc.blit(self.mas_surface_but[i], (self.mas_cord_buttons[i][0], self.mas_cord_buttons[i][1]))

    def do_filling(self, x, y):
        s.set_press_mod_left(0)


class Creat_live:
    def __init__(self, map_live, kil_squer_h, kil_squer_w, mas_neghbor, map_live_copy):
        self.map_live, self.kil_squer_h, self.kil_squer_w, self.mas_neghbor, \
        self.map_live_copy = map_live, kil_squer_h, kil_squer_w, mas_neghbor, map_live_copy
        self.mas_cord_buttons = [[10, 10], [10, 40], [10, 70], [10, 100], [10, 130], [10, 160]]
        self.mas_text_button = ["live", "clear", "save", "to restore", "fill", "del_object"]
        self.mas_funcion = [self.button_live, self.clear, self.save, self.to_restore, self.fill, self.del_object]
        self.mas_button, self.mas_surface_but = [], []
        for i in range(len(self.mas_cord_buttons)):
            self.mas_button.append(
                Button(self.mas_cord_buttons[i][0], self.mas_cord_buttons[i][1], self.mas_text_button[i], 1,
                       self.mas_funcion[i]))
            self.mas_surface_but.append(self.mas_button[i].creat_surface_button())
    
    def button_live(self):
        s.set_menu(Live)

    def clear(self):
        for i in range(self.kil_squer_h):
            for a in range(self.kil_squer_w):
                self.map_live[i][a] = 0

    def save(self):
        for i in range(self.kil_squer_h):
            for a in range(self.kil_squer_w):
                self.map_live_copy[i][a] = self.map_live[i][a]

    def to_restore(self):
        for i in range(self.kil_squer_h):
            for a in range(self.kil_squer_w):
                self.map_live[i][a] = self.map_live_copy[i][a]

    def fill(self):
        if s.get_press_mod_left() == 0:
            s.set_press_mod_left(1)
            print(self)
        else:
            s.set_press_mod_left(0)

    def del_object(self):
        if s.get_press_mod_rigth() == 0:
            s.set_press_mod_rigth(1)
        else:
            s.set_press_mod_rigth(0)

    def do_filling(self, elem):
        x, y = pygame.mouse.get_pos()
        pos_x, pos_y = x // s.size_squer, y // s.size_squer
        if self.map_live[pos_y][pos_x] == elem:
            return
        self.map_live[pos_y][pos_x] = elem
        check = deque([[pos_y, pos_x]])
        mas_neighbor = [(1, 0), (0, 1), (0, -1), (-1, 0)]
        if elem == 0:
            mas_neighbor.extend([(1, 1), (-1, 1), (1, -1), (-1, -1)])
        set_elem = {pos_y * s.kil_squer_w + pos_x}
        while check:
            deleten = check.popleft()
            for i in mas_neighbor:
                point = [deleten[0] + i[0], deleten[1] + i[1]]
                set_point = point[0] * s.kil_squer_w + point[1]
                if 0 <= point[0] < s.kil_squer_h and 0 <= point[1] < s.kil_squer_w:
                    if set_point not in set_elem and self.map_live[point[0]][point[1]] == int(not elem):
                        self.map_live[point[0]][point[1]] = elem
                        check.append(point)

    def check_buttons(self, cord_mouse_x, cord_mouse_y):
        for i in self.mas_button:
            if i.check_click_but(cord_mouse_x, cord_mouse_y):
                return True
        return

    def operecion(self):
        pass

    def output_buttons(self, sc):
        for i in range(len(self.mas_cord_buttons)):
            sc.blit(self.mas_surface_but[i], (self.mas_cord_buttons[i][0], self.mas_cord_buttons[i][1]))