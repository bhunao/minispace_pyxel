from collections.abc import Callable
from dataclasses import dataclass
from typing import Any, Dict, Optional, Sequence

from math import cos
from items import Items


def pecado(x):
    return cos(x * .1)


@dataclass
class Player:
    exp: int = 0
    exp_total: int = 25
    level: int = 1
    bullets: int = 0


@dataclass
class Item:
    item: Items = Items.heart


@dataclass
class Sprite:
    sprite: Sequence[tuple] = ((0, 0, 0, 8, 8, 0), )
    states: Optional[Dict] = None
    current_state: Optional[Any] = None
    w: int = sprite[0][3]
    h: int = sprite[0][4]

    def __post_init__(self):
        self.w: int = self.sprite[0][3]
        self.h: int = self.sprite[0][4]


@dataclass
class Circle:
    r: int = 10
    colkey: int = 16
    r_inc: int = 0
    f: Optional[Callable] = None


@dataclass
class Pos:
    x: float = 0
    y: float = 0


@dataclass
class Combat:
    hp: int = 1
    max_hp: int = hp
    damage: int = 0
    invulnerability: int = 0


@dataclass
class Enemy:
    exp: int = 1
    atk_cd: int = 0
    drop: Optional[Items] = None


class Projectile:
    pass


class EnemyProjectile:
    pass


@dataclass
class Movement:
    speed: float = 0
    angle: float = 90
    f: Optional[Callable] = None
    step: int = 0


@dataclass
class CircularMovement(Movement):
    speed: float = 0
    angle: float = 0
    radius: float = 3
    circ_step: int = 0


@dataclass
class MoveF(Movement):
    f: Optional[Callable] = None


@dataclass
class MoveToEnemy(Movement):
    pass


class MoveToPlayer(Movement):
    pass


class MoveXtoPlayer(Movement):
    pass


@dataclass
class MoveX(Movement):
    f: Optional[Callable] = pecado


@dataclass
class CircileNearTarget(Movement):
    min_dist: int = 10
    max_dist: int = 20


@dataclass
class Timer:
    time: int


@dataclass
class Text:
    text: str = "PLACEHOLDER"
    colkey: int = 16


@dataclass
class Gun:
    speed: float = 0
    angle: float = 0
    cd: int = 50
    aim_target: bool = False
    timer: int = 20
    step: int = 0
    f: Optional[Callable] = None


@dataclass
class FourGun(Gun):
    pass


@dataclass
class RotationGun(Gun):
    inc: int = 45


@dataclass
class BarrierGun(RotationGun):
    pass


class FourRotationGun(RotationGun):
    pass


class HPBar:
    pass


class Star:
    pass
