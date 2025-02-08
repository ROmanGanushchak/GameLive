import pygame
pygame.init()

class Button:
    def __init__(self, x, y, text, num_menu, function, size_x=70, size_y=25):
        self.x, self.y, self.size_x, self.size_y, self.num_menu = x, y, size_x, size_y, num_menu
        self.function = function
        f = pygame.font.Font(None, 20)
        self.text = f.render(text, True, (255, 255, 255))

    def check_click(self, cord_mouse_x, cord_mouse_y):
        if self.x <= cord_mouse_x <= self.x + self.size_x and self.y <= cord_mouse_y <= self.y + self.size_y:
            self.function()
            return True
        return

    def creat_surface(self):
        surfce_button = pygame.Surface((self.size_x, self.size_y))
        surfce_button.fill((100, 100, 100))
        place = self.text.get_rect(center=(self.size_x // 2, self.size_y // 2))
        surfce_button.blit(self.text, place)
        return surfce_button