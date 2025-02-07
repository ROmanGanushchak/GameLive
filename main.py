import pygame
import math
from setting import *
from Output import Output
from work_mouse_keybord import *
import copy
pygame.init()


class Main:
    def __init__(self):
        self.sc = pygame.display.set_mode((geometry_window[0], geometry_window[1]))
        self.clock = pygame.time.Clock()
        self.w_mouse = Work_mouse(map_live, size_squer)
        self.output = Output(self.sc, map_live, kil_squer_h, kil_squer_w, size_squer)

    def run(self):
        while True:
            self.sc.fill((0, 0, 0))
            for i in pygame.event.get():
                if i.type == pygame.QUIT:
                    pygame.quit()
                elif i.type == pygame.MOUSEBUTTONDOWN:
                    if i.button == 1:
                        self.w_mouse.left_mouse_down = True
                    elif i.button == 3:
                        self.w_mouse.rigth_mouse_down = True

                    if get_menu().check_buttons(*pygame.mouse.get_pos()) is True:
                        self.w_mouse.left_mouse_down = False
                        print(self.w_mouse.rigth_mouse_down)
                elif i.type == pygame.MOUSEBUTTONUP:
                    if i.button == 1:
                        self.w_mouse.left_mouse_down = False
                    elif i.button == 3:
                        self.w_mouse.rigth_mouse_down = False

            if self.w_mouse.rigth_mouse_down is True or self.w_mouse.left_mouse_down is True:
                self.w_mouse.main()
            self.output.main()
            get_menu().operecion()
            get_menu().output_buttons(self.sc)
            pygame.display.update()
            self.clock.tick(FPS)
            print(self.clock.get_fps())


m = Main()
m.run()