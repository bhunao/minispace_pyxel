import pyxel
from esper import Processor
from components import Pos, Sprite, Combat, Player, Enemy, Movement, Gun, FourGun, HPBar, MoveToPlayer, MoveXtoPlayer, CircileNearTarget, RotationGun, FourRotationGun, CircularMovement
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
            y=y if y else pyxel.rndi(-64, - 16),
        ),
        MoveToPlayer(speed=.5),
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
            y=y if y else pyxel.rndi(-64, - 16),
        ),
        MoveToPlayer(speed=.5),
        Enemy(),
        Combat(hp=hp, max_hp=hp, damage=2),
        Gun(speed=3, angle=90, aim_target=True, cd=4),
        HPBar()
    )


def enemy3(create_entity, x=None, y=None):
    _x, _y = rndxy()
    hp = 25
    return create_entity(
        Sprite(
            sprite=sprites.E3
        ),
        Pos(
            x=x if x else _x,
            y=y if y else -16,
        ),
        Movement(speed=.5, angle=90),
        Enemy(),
        Combat(hp=hp, max_hp=hp, damage=3),
        Gun(speed=2, angle=90, cd=50),
        HPBar()
    )


def enemy4(create_entity, x=None, y=None):
    _x, _y = rndxy()
    x = x if x else _x
    y = y if y else -16
    hp = 150
    return create_entity(
        Sprite(
            sprite=sprites.E4
        ),
        Pos(
            x=x,
            y=y if y else pyxel.rndi(-64, - 16),
        ),
        MoveXtoPlayer(speed=5),
        Enemy(),
        Combat(hp=hp,
               max_hp=hp, damage=4),
        Gun(speed=3, angle=0, cd=50, timer=150),
        Gun(speed=3, angle=90, aim_target=True, cd=4),
        HPBar(),
    )


def rotational_boss(create_entity, x=None, y=None):
    _x, _y = rndxy()
    x = x if x else _x
    y = y if y else -16
    hp = 150
    return create_entity(
        Sprite(
            sprite=sprites.E4
        ),
        Pos(
            x=x,
            y=y if y else pyxel.rndi(-64, - 16),
        ),
        MoveXtoPlayer(speed=5),
        Enemy(),
        Combat(hp=hp,
               max_hp=hp, damage=4),
        FourRotationGun(speed=2, cd=4, inc=5, timer=350),
        HPBar(),
    )


def rotationer_gunner(create_entity, x=None, y=None):
    _x, _y = rndxy()
    hp = 3
    return create_entity(
        Sprite(
            sprite=sprites.E5
        ),
        Pos(
            x=x if x else _x,
            y=y if y else -16,
        ),
        Movement(speed=.5, angle=90),
        Enemy(),
        Combat(hp=hp, max_hp=hp, damage=1),
        RotationGun(speed=2, angle=90, cd=5, timer=50),
    )


def slow_walker(create_entity, x=None, y=None):
    _x, _y = rndxy()
    hp = 3
    return create_entity(
        Sprite(
            sprite=sprites.SPHERE
        ),
        Pos(
            x=x if x else _x,
            y=y if y else pyxel.rndi(-64, - 16),
        ),
        Movement(speed=.5, angle=90),
        Enemy(),
        Combat(hp=hp, max_hp=hp, damage=1),
    )


def spinning_jack(create_entity, x=None, y=None):
    _x, _y = rndxy()
    hp = 3
    return create_entity(
        Sprite(
            sprite=sprites.E6
        ),
        Pos(
            x=x if x else _x,
            y=y if y else pyxel.rndi(-64, - 16),
        ),
        CircularMovement(speed=.5, radius=7),
        Movement(speed=.5, angle=90),
        Gun(speed=2, aim_target=True, cd=15, timer=100),
        Enemy(),
        Combat(hp=hp, max_hp=hp, damage=1),
    )


def spiral_daniel(create_entity, x=None, y=None, speed=.5):
    _x, _y = rndxy()
    hp = 3
    return create_entity(
        Sprite(
            sprite=sprites.E3
        ),
        Pos(
            x=x if x else _x,
            y=y if y else pyxel.rndi(-64, - 16),
        ),
        Movement(speed=speed, angle=90),
        FourRotationGun(speed=2, cd=2, inc=5, timer=15),
        Enemy(),
        Combat(hp=hp, max_hp=hp, damage=1),
    )


def slow_shooter(create_entity, x=None, y=None):
    _x, _y = rndxy()
    hp = 3
    return create_entity(
        Sprite(
            sprite=sprites.SPHERE
        ),
        Pos(
            x=x if x else _x,
            y=y if y else pyxel.rndi(-64, - 16),
        ),
        MoveToPlayer(speed=.5),
        Enemy(),
        Gun(speed=2, aim_target=True, cd=25, timer=100),
        Combat(hp=hp, max_hp=hp, damage=1),
    )
