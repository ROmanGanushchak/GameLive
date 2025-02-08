import pygame
from setting import *
from Output import Output
from mouse_controller import *
from menus import LiveMenu, CreativeMenu
pygame.init()


class Main:
    def __init__(self):
        self.sc = pygame.display.set_mode((geometry_window[0], geometry_window[1]))
        self.clock = pygame.time.Clock()
        self.state = GameState()
        self.state.menu = LiveMenu(self.state)
        self.w_mouse = MouseController(self.state)
        self.output = Output(self.state, self.sc)

    def run(self):
        while True:
            self.sc.fill((0, 0, 0))
            for i in pygame.event.get():
                if i.type == pygame.QUIT:
                    pygame.quit()
                    return
                elif i.type == pygame.MOUSEBUTTONDOWN:
                    if i.button == 1:
                        self.w_mouse.left_mouse_down = True
                    elif i.button == 3:
                        self.w_mouse.rigth_mouse_down = True

                    if self.state.menu.check_buttons(*pygame.mouse.get_pos()) is True:
                        self.w_mouse.left_mouse_down = False
                        print(self.w_mouse.rigth_mouse_down)
                elif i.type == pygame.MOUSEBUTTONUP:
                    if i.button == 1:
                        self.w_mouse.left_mouse_down = False
                    elif i.button == 3:
                        self.w_mouse.rigth_mouse_down = False

            if self.w_mouse.rigth_mouse_down is True or self.w_mouse.left_mouse_down is True:
                self.w_mouse.update()
            self.output.render()
            self.state.menu.update()
            self.state.menu.render_buttons(self.sc)
            pygame.display.update()
            self.clock.tick(FPS)


if __name__ == "__main__":
    m = Main()
    m.run()