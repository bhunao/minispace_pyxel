from enum import auto, Enum


class Items(Enum):
    heart = auto()
    plus_bullet = auto()
    change_attack = auto()


class AttackStyle(Enum):
    spray_attack = auto()
    normal_attack = auto()
    zizag_attack = auto()
    star_attack = auto()
