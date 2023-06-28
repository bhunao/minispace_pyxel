from dataclasses import dataclass
from typing import Callable, Optional
from engine.components import StateRender, Movement, Combat


FIREBALL = (
    (2, 8, 16, 5, 8, 7),
)


@dataclass
class Player(StateRender, Movement):
    hp: int = 3

    def skill_1(self, add):
        add(
            Projectile(x=self.x, y=self.y, angle=-
                       90, speed=3, origin=type(self),
                       sprite=FIREBALL, damage=1)
        )

    def skill_2(self, add):
        projs = [
            Projectile(x=self.x, y=self.y, angle=angle, speed=3, origin=type(self),
                       sprite=FIREBALL, damage=1) for angle in range(0, 360, 360//8)
        ]
        print(*[proj.angle for proj in projs])
        add(*projs)


@dataclass
class Enemy(StateRender, Movement, Combat):
    hp: int = 3


@dataclass
class Projectile(StateRender, Movement, Combat):
    origin: Optional[type] = None

    def collide_with_target(self, other):
        coisa = self.collide_with(other) and self.origin != type(other)
        if coisa:
            return True
        return False
