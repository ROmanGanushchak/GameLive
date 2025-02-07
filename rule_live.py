import copy

class Live_rules_check:
    def __init__(self, map_live, kil_squer_h, kil_squer_w, mas_neghbor):
        self.map_live, self.kil_squer_h, self.kil_squer_w, self.mas_neghbor = map_live, kil_squer_h, kil_squer_w, mas_neghbor

    def future_sqear(self, kil_neighbor, sqear):
        if sqear == 0 and kil_neighbor == 3:
            return 1
        if sqear == 1 and kil_neighbor == 3:
            return 1
        if sqear == 1 and kil_neighbor == 2:
            return 1
        return 0

    def search_map(self) -> None:
        map_live_now = copy.deepcopy(self.map_live)
        for i in range(self.kil_squer_h):
            for a in range(self.kil_squer_w):
                kil_neighbor = 0
                for neighbor in self.mas_neghbor:
                    if 0 <= i + neighbor[0] < self.kil_squer_h and 0 <= a + neighbor[1] < self.kil_squer_w:
                        if map_live_now[i + neighbor[0]][a + neighbor[1]] == 1:
                            kil_neighbor += 1
                self.map_live[i][a] = self.future_sqear(kil_neighbor, map_live_now[i][a])