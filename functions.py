import pyxel
from components import Sprite, Pos
from math import sqrt


def rainbow():
    return pyxel.frame_count % 15


def frame_cd(n) -> bool:
    if n <= 0:
        return True
    return not pyxel.frame_count % n


def rndxy():
    return pyxel.rndi(0, pyxel.width), pyxel.rndi(0, pyxel.height)


def center_of(sprite: Sprite, pos: Pos):
    x = pos.x
    y = pos.y
    return x + sprite.w // 2, y + sprite.h // 2


def distance_between(pos1: Pos, pos2: Pos):
    n1 = (pos1.x - pos2.x)**2
    n2 = (pos1.y - pos2.y)**2
    return sqrt(n1 + n2)
