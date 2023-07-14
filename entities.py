import pyxel
from esper import Processor
from components import Pos, Sprite, Combat, Player, Enemy, Movement, Gun, FourGun, HPBar, MoveToPlayer
from sprites import WARRIOR, DOWN
import sprites
from functions import rndxy, frame_cd


class EnemyBuilder:
    def __init__(self):
        self.wave: int = 0
        self.spawned: bool = False
        self.waves: list = [
            [enemy1, (50, 50), 3],
            [enemy1, (50, 50), 5],
            [enemy2, (50, 50), 3],
            [enemy3, (50, 50), 2],
            [enemy4, (50, 50), 1],
        ]

    def wave_spawn(self, create_entity):
        if self.wave >= len(self.waves):
            return

        if not self.spawned:
            func, args, quantity = self.waves[self.wave]
            print(func, args, quantity)
            for _ in range(quantity):
                func(create_entity)
            self.wave += 1


def enemy1(create_entity, x=None, y=None):
    _x, _y = rndxy()
    hp = 3
    return create_entity(
        Sprite(
            sprite=sprites.SPHERE
        ),
        Pos(
            x=x if x else _x,
            y=y if y else -16,
        ),
        MoveToPlayer(speed=1),
        Enemy(),
        Combat(hp=hp, max_hp=hp, damage=1),
    )


def enemy2(create_entity, x=None, y=None):
    _x, _y = rndxy()
    x = x if x else _x
    y = y if y else -16
    hp = 10
    return create_entity(
        Sprite(
            sprite=sprites.E2
        ),
        Pos(
            x=x,
            y=y,
        ),
        MoveToPlayer(speed=1),
        Enemy(),
        Combat(hp=hp, max_hp=hp, damage=2),
        Gun(speed=3, angle=90, aim_target=True, cd=4),
        HPBar()
    )


def enemy3(create_entity, x=None, y=None):
    _x, _y = rndxy()
    x = x if x else _x
    y = y if y else -16
    hp = 25
    return create_entity(
        Sprite(
            sprite=sprites.E3
        ),
        Pos(
            x=x,
            y=y,
        ),
        Movement(speed=1, angle=90),
        Enemy(),
        Combat(hp=hp, max_hp=hp, damage=3),
        Gun(speed=1, angle=90, cd=50),
        HPBar()
    )


def enemy4(create_entity, x=None, y=None):
    _x, _y = rndxy()
    x = x if x else _x
    y = y if y else -16
    hp = 50
    return create_entity(
        Sprite(
            sprite=sprites.E4
        ),
        Pos(
            x=x,
            y=y,
        ),
        MoveToPlayer(speed=1),
        Enemy(),
        Combat(hp=hp,
               max_hp=hp, damage=4),
        FourGun(speed=2, angle=0, cd=50),
        HPBar(),
    )
