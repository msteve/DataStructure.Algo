# coding=utf-8

import time
from gameworld import Animal, draw_grid

def cats():

    for i in range(2, 8):
        yield Animal(row=i, col=i)


def mice():

    for i in range(7, 1, -1):
        yield Animal(row=7, col=i)


for cat, mouse in zip(cats(), mice()):
    draw_grid(cat, mouse)
    time.sleep(.4)
