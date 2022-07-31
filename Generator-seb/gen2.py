# coding=utf-8

import time
import random
from gameworld import Animal, draw_grid, move


def cats():

    cat = Animal(row=2, col=2)
    while True:
        mouse = yield cat
        if mouse.row > cat.row:
            cat = move(cat, row=1)
        elif mouse.row < cat.row:
            cat = move(cat, row=-1)
        if mouse.col > cat.col:
            cat = move(cat, col=1)
        elif mouse.col < cat.col:
            cat = move(cat, col=-1)


def mice():

    mouse = Animal(row=7, col=7)
    while True:
        cat = yield mouse
        if mouse.col == cat.col and mouse.row == cat.row:
            raise StopIteration()
        if mouse.row > cat.row:
            mouse = move(mouse, row=1)
        elif mouse.row < cat.row:
            mouse = move(mouse, row=-1)
        else:
            mouse = move(mouse, row=random.choice([-1, 1]))
        if mouse.col > cat.col:
            mouse = move(mouse, col=1)
        elif mouse.col < cat.col:
            mouse = move(mouse, col=-1)
        else:
            mouse = move(mouse, col=random.choice([-1, 1]))


icat = cats()
imouse = mice()
cat = icat.send(None)
mouse = imouse.send(None)
while True:
    draw_grid(cat, mouse)
    time.sleep(.4)
    try:
        cat = icat.send(mouse)
        mouse = imouse.send(cat)
    except StopIteration:
        break
draw_grid(cat, mouse)
