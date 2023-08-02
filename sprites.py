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
SPHERE2 = [
    (0, 16, 0, 8, 8, Colors.BLACK),
    (0, 24, 0, 8, 8, Colors.BLACK),
    (0, 16, 8, 8, 8, Colors.BLACK),
    (0, 24, 8, 8, 8, Colors.BLACK),
]
BULLET = [(0, 36, 8, 4, 4, Colors.BLACK)]
BULLET2 = [(0, 32, 8, 4, 4, Colors.BLACK)]
LASER = [(0, 36, 12, 4, 4, Colors.BLACK)]
LASER2 = [(0, 32, 12, 4, 4, Colors.BLACK)]

FIRE = [
    (0, 40, 26, 2, 2, Colors.BLACK),
    (0, 42, 24, 2, 2, Colors.BLACK),
    (0, 40, 26, 2, 2, Colors.BLACK),
    (0, 42, 26, 2, 2, Colors.BLACK),
]

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
E4 = [
    (0, 0, 112, 32, 32, Colors.BLACK),
    (0, 32, 112, 32, 32, Colors.BLACK),
]
E5 = [
    (0, 0, 64, 16, 16, Colors.BLACK),
    (0, 16, 64, 16, 16, Colors.BLACK),
]
E6 = [
    (0, 0, 96, 16, 16, Colors.BLACK),
    (0, 16, 96, 16, 16, Colors.BLACK),
]
X_ENEMY = [
    (0, 0, 144, 8, 8, Colors.BLACK),
    (0, 8, 144, 8, 8, Colors.BLACK),
    (0, 0, 152, 8, 8, Colors.BLACK),
    (0, 8, 152, 8, 8, Colors.BLACK),
]
WALLBOY = [
    (0, 16, 144, 8, 8, Colors.BLACK),
    (0, 24, 144, 8, 8, Colors.BLACK),
    (0, 16, 152, 8, 8, Colors.BLACK),
    (0, 24, 152, 8, 8, Colors.BLACK),
]
BARTOLOMEO = [
    (0, 0, 160, 16, 16, Colors.BLACK),
    (0, 16, 160, 16, 16, Colors.BLACK),
]


STARS = [
    (0, 0, 80, 4, 4, Colors.BLACK),
    (0, 4, 80, 4, 4, Colors.BLACK),
    (0, 0, 84, 4, 4, Colors.BLACK),
    (0, 4, 84, 4, 4, Colors.BLACK),
]

PLUS_ONE = [
    (0, 32, 48, 8, 8, Colors.BLACK),
    (0, 32, 56, 8, 8, Colors.BLACK),
]
HEART = [
    (0, 40, 48, 8, 8, Colors.BLACK),
    (0, 40, 56, 8, 8, Colors.BLACK),
]
ATTACKCHANGE = [
    (0, 32, 64, 8, 8, Colors.BLACK),
    (0, 32, 72, 8, 8, Colors.BLACK),
]
PLANET = [
    (0, 48, 0, 32, 32, Colors.BLACK),
]
