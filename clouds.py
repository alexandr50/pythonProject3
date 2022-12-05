from utils import randbool


class Clouds:
    def __init__(self, h, w):
        self.h = h
        self.w = w
        self.cells = [[0 for i in range(w)] for j in range(h)]

    def update_couds(self, r=1, mxr=20, g=1, mxg=20):
        for i in range(self.h):
            for j in range(self.w):
                if randbool(r, mxr):
                    self.cells[i][j] = 1
                    if randbool(g, mxg):
                        self.cells[i][j] = 2
                else:
                    self.cells[i][j] = 0


    def export_data(self):
        return {'cells': self.cells}

    def import_date(self, data):
        self.cells = data['cells'] or [[0 for i in range(self.w)] for j in range(self.h)]

