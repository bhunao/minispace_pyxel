import pyxel
from typing import Sequence
from math import radians, cos, sin
from dataclasses import dataclass


@dataclass
class Render:
    sprite: Sequence[tuple] = ((0, 0, 0, 8, 8, 0), )
    x: float = 0
    y: float = 0
    w: int = sprite[0][3]
    h: int = sprite[0][4]

    def collide_with(self, other):
        if self.x > other.x + other.w or other.x > self.x + self.w:
            return False
        if self.y > other.y + other.w or other.y > self.y + self.w:
            return False
        return True

    def render(self):
        nframes = 5
        i = pyxel.frame_count % (nframes * len(self.sprite)) // nframes
        pyxel.blt(self.x, self.y, *self.sprite[i])


@dataclass
class Movement:
    x: float = 0
    y: float = 0
    speed: int = 0
    angle: int = 0

    def move(self):
        angle_rad = radians(self.angle)
        self.x += cos(angle_rad) * self.speed
        self.y += sin(angle_rad) * self.speed
