import random
import pygame
import math
import copy
from array import *
from menus import *

# настройка квадратів
FPS = 120

# основне
kil_squer_w, kil_squer_h = 190, 100
size_squer = 8
geometry_window = [kil_squer_w * size_squer, kil_squer_h * size_squer]
mas_neghbor = [(0, 1), (1, 0), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, -1), (-1, 1)]

# створення карти
map_live = [array("b", [0] * kil_squer_w) for i in range(kil_squer_h)]

kil_start_sqear = 5000
for i in range(kil_start_sqear):
    map_live[random.randint(0, kil_squer_h-1)][random.randint(0, kil_squer_w-1)] = 1
map_live_copy = [[0] * kil_squer_w for i in range(kil_squer_h)]

# режими нажаття
press_mod_left = 0
def set_press_mod_left(n):
    global press_mod_left
    press_mod_left = n

def get_press_mod_left():
    return press_mod_left

press_mod_rigth = 0
def set_press_mod_rigth(n):
    global press_mod_rigth
    press_mod_rigth = n

def get_press_mod_rigth():
    return press_mod_rigth



# режими меню
# num_menu = 1
menu = Live(map_live, kil_squer_h, kil_squer_w, mas_neghbor, map_live_copy)

def set_menu(obj):
    global menu
    menu = obj(map_live, kil_squer_h, kil_squer_w, mas_neghbor, map_live_copy)

def get_menu():
    return menu