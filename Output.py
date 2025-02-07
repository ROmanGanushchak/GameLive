import pygame


class Output:
    def __init__(self, sc, map_live, kil_squer_h, kil_squer_w, size_squer):
        self.sc, self.map_live, self.kil_squer_h, self.kil_squer_w = sc, map_live, kil_squer_h, kil_squer_w
        self.kil_squer_w, self.size_squer = kil_squer_w, size_squer

    def output_map_sqear_surface(self, sc, map_live):
        for i in range(self.kil_squer_h):
            for a in range(self.kil_squer_w):
                if map_live[i][a]:
                    pygame.draw.rect(sc, (100, 255, 255),
                                     (a * self.size_squer + 1, i * self.size_squer + 1, self.size_squer - 1, self.size_squer - 1))

    def output_lines(self, sc):
        for y in range(self.kil_squer_h):
            pygame.draw.line(sc, (75, 75, 75), (0, y * self.size_squer), (self.kil_squer_w * self.size_squer, y * self.size_squer), 1)
        for x in range(self.kil_squer_w):
            pygame.draw.line(sc, (75, 75, 75), (x * self.size_squer, 0), (x * self.size_squer, self.kil_squer_h * self.size_squer), 1)

    def main(self):
        self.output_map_sqear_surface(self.sc, self.map_live)
        self.output_lines(self.sc)
