from dataclasses import dataclass
from typing import Callable, Optional
from sprites import SpriteSequence


@dataclass
class Sprite:
    sprite: SpriteSequence
    w: int = 8
    h: int = 8

@dataclass
class Pos:
    x: float = 0
    y: float = 0


@dataclass
class Speed:
    speed: float = 0
    angle: float = 90
    f_speed: Callable = lambda: 1
    f_angle: Callable = lambda: 0


@dataclass
class Timer:
    time: int


@dataclass
class Player:
    pass
