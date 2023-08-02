from random import choice
import pyxel
from components import (BarrierGun, CircileNearTarget, MoveF, MoveX, Pos, Sprite, Combat, Enemy, Movement, Gun, HPBar,
                        MoveToPlayer, MoveXtoPlayer, RotationGun,
                        FourRotationGun, CircularMovement)
from items import Items
import sprites
from functions import rndxy


def enemy1(create_entity, x=None, y=None):
    _x, _y = rndxy()
    hp = 3
    drop = choice([
        Items.change_attack,
        Items.plus_bullet,
    ])
    return create_entity(
        Sprite(
            sprite=sprites.SPHERE
        ),
        Pos(
            x=x if x else _x,
            y=y if y else pyxel.rndi(-64, - 16),
        ),
        MoveToPlayer(speed=.5),
        Enemy(drop=drop),
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
    hp = 50
    drop = choice([
        Items.change_attack,
        Items.plus_bullet,
    ])
    return create_entity(
        Sprite(
            sprite=sprites.E4
        ),
        Pos(
            x=x,
            y=y if y else pyxel.rndi(-64, - 16),
        ),
        MoveXtoPlayer(speed=5),
        Enemy(exp=15, drop=drop),
        Combat(hp=hp,
               max_hp=hp, damage=1),
        FourRotationGun(speed=2, cd=6, inc=5, timer=350),
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
        Enemy(exp=3),
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
        MoveX(speed=1, angle=90),
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
        Gun(speed=2, aim_target=True, cd=25, timer=100),
        Enemy(exp=5),
        Combat(hp=hp, max_hp=hp, damage=1),
    )


def spiral_daniel(create_entity, x=None, y=None, speed=.5):
    _x, _y = rndxy()
    hp = 15
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
        Enemy(exp=5),
        Combat(hp=hp, max_hp=hp, damage=1),
    )


def slow_shooter(create_entity, x=None, y=None):
    _x, _y = rndxy()
    hp = 3
    return create_entity(
        Sprite(
            sprite=sprites.SPHERE2
        ),
        Pos(
            x=x if x else _x,
            y=y if y else pyxel.rndi(-64, - 16),
        ),
        MoveToPlayer(speed=.5),
        Enemy(exp=2),
        Gun(speed=2, aim_target=True, cd=40, timer=100),
        Combat(hp=hp, max_hp=hp, damage=1),
    )


def ronnie_wall(create_entity, x=None, y=None):
    _x, _ = rndxy()
    hp = 10

    def coisa(x):
        b = x % 100 > 50
        impopar = (x // 100) % 2 == 0
        return 0 if b else 1 if impopar else -.2

    return create_entity(
        Sprite(
            sprite=sprites.WALLBOY
        ),
        Pos(
            x=x if x else _x,
            y=y if y else pyxel.rndi(-64, - 16),
        ),
        Movement(speed=.5, f=coisa),
        Enemy(exp=2),
        Gun(1, 90, 50, True, timer=150),
        Combat(hp=hp, max_hp=hp, damage=1),
    )


def rodoaldo(create_entity, x=None, y=None):
    _x, _y = rndxy()
    hp = 5
    return create_entity(
        Sprite(
            sprite=sprites.X_ENEMY
        ),
        Pos(
            x=x if x else _x,
            y=y if y else pyxel.rndi(-64, - 16),
        ),
        CircularMovement(speed=1, f=lambda x: 0 if x < 100 else 1, radius=5),
        Movement(speed=1, f=lambda x: 1 if x < 100 else 0, angle=90),
        Enemy(exp=2),
        Gun(speed=2, aim_target=True, cd=30, timer=100),
        Combat(hp=hp, max_hp=hp, damage=1),
    )


def bartolomeo(create_entity, x=None, y=None):
    _x, _y = rndxy()
    hp = 30
    drop = choice([
        Items.change_attack,
        Items.plus_bullet,
    ])
    return create_entity(
        Sprite(
            sprite=sprites.BARTOLOMEO
        ),
        Pos(
            x=x if x else _x,
            y=y if y else pyxel.rndi(-64, - 16),
        ),
        Movement(speed=.5),
        BarrierGun(speed=.5,
                   cd=15,
                   inc=3,
                   timer=120),
        Enemy(exp=5),
        Combat(hp=hp, max_hp=hp, damage=1),
    )


entities_list = [
    enemy1,
    enemy2,
    enemy3,
    enemy4,
    rotational_boss,
    rotationer_gunner,
    slow_walker,
    spinning_jack,
    spiral_daniel,
    slow_shooter,
    ronnie_wall,
    rodoaldo,
]
