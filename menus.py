import pygame
from game_update import GameUpdate
from Buttons import *
from setting import *
from creative import Creative

class LiveMenu:
    def __init__(self, state):
        self.state = state
        self.field = state.field
        self.field_copy = state.field_copy

        self.mas_cord_buttons = [[10, 10]]
        self.mas_text_button = ["creative"]
        self.mas_funcion = [self.switch_to_creative]
        self.mas_button, self.mas_surface_but = [], []
        for i in range(len(self.mas_cord_buttons)):
            self.mas_button.append(
                Button(self.mas_cord_buttons[i][0], self.mas_cord_buttons[i][1], self.mas_text_button[i], 1,
                       self.mas_funcion[i]))
            self.mas_surface_but.append(self.mas_button[i].creat_surface())
    
    def switch_to_creative(self):
        self.state.menu = CreativeMenu(self.state)

    def check_buttons(self, cord_mouse_x, cord_mouse_y):
        for i in self.mas_button:
            if i.check_click(cord_mouse_x, cord_mouse_y):
                return True

    def update(self):
        live = GameUpdate(self.state)
        live.update_map()

    def render_buttons(self, sc):
        for i in range(len(self.mas_cord_buttons)):
            sc.blit(self.mas_surface_but[i], (self.mas_cord_buttons[i][0], self.mas_cord_buttons[i][1]))

    def fill(self):
        self.state.press_type = PressingType.FILL


class CreativeMenu:
    def __init__(self, state):
        self.state = state
        self.field = state.field
        self.field_copy = state.field_copy

        self.creative = Creative(state)
        self.mas_cord_buttons = [[10, 10], [10, 40], [10, 70], [10, 100], [10, 130]]
        self.mas_text_button = ["live", "clear", "save", "to restore", "fill"]
        self.mas_funcion = [self.switch_to_live, self.creative.clear, self.creative.save, self.creative.restore, self.fill]
        self.mas_button, self.mas_surface_but = [], []
        for i in range(len(self.mas_cord_buttons)):
            self.mas_button.append(
                Button(self.mas_cord_buttons[i][0], self.mas_cord_buttons[i][1], self.mas_text_button[i], 1,
                       self.mas_funcion[i]))
            self.mas_surface_but.append(self.mas_button[i].creat_surface())
    
    def switch_to_live(self):
        self.state.menu = LiveMenu(self.state)

    def fill(self):
        if (self.state.press_type == PressingType.FILL):
            self.state.press_type = PressingType.DRAW
        else:
            self.state.press_type = PressingType.FILL

    def check_buttons(self, cord_mouse_x, cord_mouse_y):
        for i in self.mas_button:
            if i.check_click(cord_mouse_x, cord_mouse_y):
                return True
        return

    def update(self):
        pass

    def render_buttons(self, sc):
        for i in range(len(self.mas_cord_buttons)):
            sc.blit(self.mas_surface_but[i], (self.mas_cord_buttons[i][0], self.mas_cord_buttons[i][1]))