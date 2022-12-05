from random import randint


def randbool(r, rmax):
    t = randint(0, rmax)
    return t <= r


def randcell(x, y):
    t1 = randint(0, x - 1)
    t2 = randint(0, y - 1)
    return t1, t2


def randcell2(x, y):
    moves = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    t = randint(0, 3)
    tx, ty = moves[t][0], moves[t][1]
    return (x + tx, y + ty)
