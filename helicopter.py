import ftplib

from utils import randcell


class Helicopter:

    def __init__(self, w, h):
        cell = randcell(w, h)
        rx, ry = cell[0], cell[1]
        self.w = w
        self.h = h
        self.x = rx
        self.y = ry
        self.tank = 0
        self.mxtank = 1
        self.score = 0
        self.lives = 2000


    def move(self, x, y):
        mx, my = x + self.x, y + self.y
        if mx >= 0 and my >= 0 and mx < self.h and my < self.w:
            self.x = mx
            self.y = my

    def print_menu(self):
        print('🥣', self.tank, '/', self.mxtank, '🏆', ':', self.score, '💟', ':', self.lives)

    def export_data(self):
        return {
            'score': self.score,
            'lives': self.lives,
            'tank': self.tank,
            'mxtank': self.mxtank,
            'x':self.x, 'y': self.y

        }
    def import_data(self, data):
        self.x = data['x'] or 0
        self.y = data['y'] or 0
        self.tank = data['tank'] or 0
        self.mxtank = data['mxtank'] or 1
        self.score = data['score'] or 0
        self.lives = data['lives'] or 2000