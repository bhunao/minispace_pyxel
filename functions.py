import sprites
from typing import Tuple
from dataclasses import dataclass
import pyxel
from components import Sprite, Pos, Player
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


def inside_screen(pos: Pos):
    if pos.x < -4 or pos.x > pyxel.width:
        return False
    if pos.y < -4 or pos.y > pyxel.height:
        return False
    return True

def get_player(world) -> Tuple[int, Tuple[Player, Pos, Sprite]]:
    for player_components in world.get_components(Player, Pos, Sprite):
        return player_components
    else:
        return -1, (Player(), Pos(), Sprite(sprites.SPHERE))
        

@dataclass
class myfunction:
    def __init__(self, f) -> None:
        self.f = f
        self.val1 = None
        self.val2 = None
        self.re = None

    def __matmul__(self, other):
        if not self.val1:
            self.val1 = other
        elif not self.val2:
            self.val2 = other
            self.re = self.f(*self.val1, *self.val2)
            return self.re
        return self

    def __rmatmul__(self, other):
        if not self.val1:
            self.val1 = other
        elif not self.val2:
            self.val2 = other
            self.re = self.f(*self.val1, *self.val2)
            return self.re
        return self

    def __str__(self) -> str:
        return f"{self.f}, {self.val1}, {self.val2}, {self.re}"
