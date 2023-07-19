import pyxel
from components import Sprite, Pos


def rainbow():
    return pyxel.frame_count % 15


def frame_cd(n) -> bool:
    return not pyxel.frame_count % n


def rndxy():
    return pyxel.rndi(0, pyxel.width), pyxel.rndi(0, pyxel.height)


def center_of(sprite: Sprite, pos: Pos):
    x = pos.x
    y = pos.y
    return x + sprite.w // 2, y + sprite.h // 2
