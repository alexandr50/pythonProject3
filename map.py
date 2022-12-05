import os

from utils import randbool
from utils import randcell
from utils import randcell2
UPGRADE_COST = 5000
CELL_TYPES = '🟩🌲🌊🚑🛒🔥'
LIVE_COST = 10000
class Map:

    def __init__(self, width, high):
        self.width = width
        self.high = high
        self.cells = [[0 for i in range(width)] for j in range(high)]
        self.generate_forest(3, 10)
        self.generate_upgrade_shop()
        self.generate_river(6)
        self.generate_river(4)
        self.generate_hospital()

    def generate_river(self, l):
        cell = randcell(self.high, self.width)
        r, c = cell[0], cell[1]
        while l >= 0:
            cell2 = randcell2(r, c)
            x, y = cell2[0], cell2[1]
            if self.check_bounds(x, y) and self.cells[x][y] != 2:
                self.cells[x][y] = 2
                r, c  = x, y
                l -= 1

    def generate_fire(self):
        cell = randcell(self.high, self.width)
        r, c = cell[0], cell[1]
        if self.cells[r][c] == 1:
            self.cells[r][c] = 5

    def fire_update(self):
        for row in range(self.high):
            for col in range(self.width):
                if self.cells[row][col] == 5:
                    self.cells[row][col] = 0
        for i in range(10):
            self.generate_fire()



    def generate_forest(self, r, rmax):
        for row in range(self.high):
            for col in range(self.width):
                if randbool(r, rmax):
                    self.cells[row][col] = 1

    def generate_tree(self):
        cell = randcell(self.high, self.width)
        r, c = cell[0], cell[1]
        if self.check_bounds(r, c) and self.cells[r][c] == 0:
            self.cells[r][c] = 1

    def generate_upgrade_shop(self):
        cell = randcell(self.high, self.width)
        r, c = cell[0], cell[1]
        self.cells[r][c] = 4

    def generate_hospital(self):
        cell = randcell(self.high, self.width)
        r, c = cell[0], cell[1]
        if self.cells[r][c] != 4:
            self.cells[r][c] = 3
        else:
            self.generate_hospital()



    def print_map(self, hel, clouds):
        print('🔲' * (self.width + 2))
        for ri in range(self.high):
            print('🔲', end='')
            for ci in range(self.width):
                cell = self.cells[ri][ci]
                if clouds.cells[ri][ci] == 1:
                    print('🟦', end='')
                elif clouds.cells[ri][ci] == 2:
                    print('🟪', end='')
                elif hel.x == ri and hel.y == ci:
                    print('🚁', end='')
                elif cell >= 0 and cell < (len(CELL_TYPES)):
                    print(CELL_TYPES[cell], end='')
            print('🔲', end='')
            print()
        print('🔲' * (self.width + 2))

    def check_bounds(self, x, y):
        return x >= 0 and y >= 0 and x < self.high and y < self.width


    def process_helicopter(self, hel, clouds):
        cell = self.cells[hel.x][hel.y]
        d = clouds.cells[hel.x][hel.y]
        if cell == 2:
            hel.tank = hel.mxtank
        if cell == 5 and hel.tank >= 1:
            hel.score += 100
            hel.tank -= 1
            self.cells[hel.x][hel.y] = 1
        if cell == 4 and hel.score >= UPGRADE_COST:
            hel.mxtank += 1
            hel.score -= UPGRADE_COST
        if cell == 3 and hel.score >= LIVE_COST:
            hel.lives += 1000
            hel.score -= LIVE_COST
        if d == 2:
            hel.lives -= 1
            if hel.lives == 0:
                os.system('clear')
                print(f'Your score {hel.score}, Game Over')
                exit(0)


    def export_data(self):
        return {'cells':self.cells}

    def import_date(self, data):
        self.cells = data['cells'] or [[0 for i in range(self.width)] for j in range(self.high)]




