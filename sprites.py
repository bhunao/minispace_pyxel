from enum import Enum


class Colors:
    BLACK = 0
    BLUE1 = 1
    PURPLE = 2
    PISCINA = 3
    MARROM = 4
    BLUE2 = 5
    BLUE3 = 6
    WHITE = 7
    PINK = 8
    ORANGE = 9
    YELLOW = 10
    GREEN = 11
    BLUE4 = 12
    GRAY = 13
    SALMON = 14
    BEGE = 15


class Sides(Enum):
    RIGHT = 0
    RIGHT_DOWN = 45
    DOWN = 90
    DOWN_LEFT = 135
    LEFT = 180
    LEFT_UP = 225
    UP = 270
    UP_RIGHT = 315


LEFT = Sides.LEFT
RIGHT = Sides.RIGHT
UP = Sides.UP
DOWN = Sides.DOWN

SPHERE = [
    (0, 0, 0, 8, 8, Colors.BLACK),
    (0, 8, 0, 8, 8, Colors.BLACK),
    (0, 0, 8, 8, 8, Colors.BLACK),
    (0, 8, 8, 8, 8, Colors.BLACK),
]
BULLET = [(0, 28, 0, 4, 4, Colors.BLACK)]
BULLET2 = [(0, 24, 0, 4, 4, Colors.BLACK)]

NV1 = [
    (0, 32, 0, 8, 8, Colors.BLACK),
    (0, 40, 0, 8, 8, Colors.BLACK),
]
E1 = [
    (0, 0, 64, 16, 16, Colors.BLACK),
    (0, 16, 64, 16, 16, Colors.BLACK),
]
E2 = [
    (0, 0, 48, 16, 16, Colors.BLACK),
]
E3 = [
    (0, 0, 32, 16, 16, Colors.BLACK),
    (0, 16, 32, 16, 16, Colors.BLACK),
]


STARS = [
    (0, 0, 80, 4, 4, Colors.BLACK),
    (0, 4, 80, 4, 4, Colors.BLACK),
    (0, 0, 84, 4, 4, Colors.BLACK),
    (0, 4, 84, 4, 4, Colors.BLACK),
]

GRASS1 = [(0, 32, 64, 8, 8, Colors.WHITE),]
GRASS2 = [(0, 40, 64, 8, 8, Colors.WHITE),]
GRASS3 = [(0, 32, 72, 8, 8, Colors.WHITE),]
GRASS4 = [(0, 40, 72, 8, 8, Colors.WHITE),]
WATER1 = [(0, 32, 32, 8, 8, Colors.WHITE),]
WATER2 = [(0, 40, 32, 8, 8, Colors.WHITE),]
WATER3 = [(0, 32, 40, 8, 8, Colors.WHITE),]
WATER4 = [(0, 40, 40, 8, 8, Colors.WHITE),]
GRASS = [(0, 32, 0, 8, 8, Colors.WHITE)]
TREE = [(0, 40, 0, 8, 8, Colors.WHITE)]
PORTAL = [
    (0, 32, 8, 8, 8, Colors.WHITE),
    (0, 40, 8, 8, 8, Colors.WHITE),
]
ENEMY1 = [
    (0, 0, 48, 8, 8, Colors.WHITE),
    (0, 8, 48, 8, 8, Colors.WHITE),
    (0, 0, 56, 8, 8, Colors.WHITE),
    (0, 8, 56, 8, 8, Colors.WHITE),
]
ENEMY2 = {
    LEFT: [(0, 32, 0, 16, 16, 1)],
    RIGHT: [(0, 32, 16, 16, 16, 1)],
    UP: [(0, 48, 16, 16, 16, 1)],
    DOWN: [(0, 48, 16, 16, 16, 1)],
}
ATTACK = [
    (0, 0, 0, 8, 8, 0),
    (0, 8, 0, 8, 8, 0),
    (0, 0, 8, 8, 8, 0),
    (0, 8, 8, 8, 8, 0),
]
CYCLONE = [
    (0, 0, 40, 8, 8, Colors.BLACK),
    (0, 0, 48, 8, 8, Colors.BLACK),
    (0, 8, 32, 8, -8, Colors.BLACK),
    (0, 0, 48, -8, 8, Colors.BLACK),
    (0, 0, 40, -8, 8, Colors.BLACK),
    (0, 0, 32, -8, 8, Colors.BLACK),
    (0, 8, 32, 8, 8, Colors.BLACK),
    (0, 0, 32, 8, 8, Colors.BLACK),
]
ARROW = [
    (0, 0, 24, 8, 5, Colors.WHITE),
    (0, 0, 24, -8, 5, Colors.WHITE),
    (0, 0, 16, 5, -8, Colors.WHITE),
    (0, 0, 16, 5, 8, Colors.WHITE),
]
FIREBALL = {
    LEFT: ((0, 8, 24, 8, 5, 7),),
    RIGHT: ((0, 0, 0, 8, 8, Colors.BLACK),),
    DOWN: ((0, 8, 16, 5, -8, 7),),
    UP: ((0, 8, 16, 5, 8, 7),),
}
EXP_ORB = [
    (0, 16, 16, 8, 8, 15),
    (0, 24, 16, 8, 8, 15),
    (0, 16, 24, 8, 8, 15),
    (0, 24, 24, 8, 8, 15)
]


MAGE = {
    LEFT: ((0, 16, 0, -8, 8, 7),),
    RIGHT: ((0, 16, 0, 8, 8, 7),),
    UP: ((0, 16, 0, 8, 8, 7),),
    DOWN: ((0, 16, 0, 8, 8, 7),),
}

WARRIOR = {
    LEFT: ((0, 16, 8, -8, 8, 7),),
    RIGHT: ((0, 16, 8, 8, 8, 7),),
    UP: ((0, 16, 8, 8, 8, 7),),
    DOWN: ((0, 16, 8, 8, 8, 7),),
}

ARCHER = {
    LEFT: ((0, 16, 16, -8, 8, 7),),
    RIGHT: ((0, 16, 16, 8, 8, 7),),
    UP: ((0, 16, 16, 8, 8, 7),),
    DOWN: ((0, 16, 16, 8, 8, 7),),
}

PLAYER = {
    LEFT: ((0, 0, 8, 8, 8, Colors.WHITE),),
    RIGHT: ((0, 8, 8, 8, 8, Colors.WHITE),),
    UP: ((0, 8, 0, 8, 8, Colors.WHITE),),
    DOWN: ((0, 0, 0, 8, 8, Colors.WHITE),),
}
ENEMIE1 = {
    LEFT: ((0, 0, 0, 8, 8, Colors.WHITE),),
    RIGHT: ((0, 0, 0, 8, 8, Colors.WHITE),),
    UP: ((0, 0, 0, 8, 8, Colors.WHITE),),
    DOWN: ((0, 24, 0, 8, 8, 1),),
}
