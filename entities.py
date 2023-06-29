from dataclasses import dataclass
from enum import Enum
from typing import Optional
from engine.components import StateRender, Movement, Combat


class Sides(Enum):
    LEFT = 180
    DOWN_LEFT = -1, 1
    DOWN = -90
    DOWN_RIGHT = 1, 1
    RIGHT = 0
    UP_RIGHT = 1, -1
    UP = 90
    UP_LEFT = -1, -1


LEFT = Sides.LEFT
RIGHT = Sides.RIGHT
UP = Sides.UP
DOWN = Sides.DOWN

FIREBALL = {
    LEFT: ((2, 8, 24, 8, 5, 7),),
    RIGHT: ((2, 8, 24, -8, 5, 7),),
    UP: ((2, 8, 16, 5, -8, 7),),
    DOWN: ((2, 8, 16, 5, 8, 7),),
}


@dataclass
class Player(StateRender, Movement):
    hp: int = 3

    def skill_1(self, world):
        print(self.current_state, *FIREBALL.keys(), sep="\n")
        print(self.current_state in FIREBALL.keys())

        world.add(
            Projectile(x=self.x, y=self.y, angle=self.current_state.value,
                       speed=3, origin=type(self),
                       sprite=FIREBALL[self.current_state], damage=1,
                       duration=15)
        )

    def skill_2(self, world):
        projs = [
            Projectile(x=self.x, y=self.y, angle=angle, speed=3, origin=type(self),
                       sprite=FIREBALL, damage=1, duration=15) for angle in range(0, 360, 360//8)
        ]
        world.add(*projs)

    def skill_3(self, world):
        projs = [
            Projectile(x=self.x-8, y=self.y-8, origin=type(self),
                       sprite=FIREBALL, damage=1, duration=15),
            Projectile(x=self.x, y=self.y-8, origin=type(self),
                       sprite=FIREBALL, damage=1, duration=15),
            Projectile(x=self.x+8, y=self.y-8, origin=type(self),
                       sprite=FIREBALL, damage=1, duration=15),
            Projectile(x=self.x-8, y=self.y, origin=type(self),
                       sprite=FIREBALL, damage=1, duration=15),
            Projectile(x=self.x+8, y=self.y, origin=type(self),
                       sprite=FIREBALL, damage=1, duration=15),
            Projectile(x=self.x-8, y=self.y+8, origin=type(self),
                       sprite=FIREBALL, damage=1, duration=15),
            Projectile(x=self.x, y=self.y+8, origin=type(self),
                       sprite=FIREBALL, damage=1, duration=15),
            Projectile(x=self.x+8, y=self.y+8, origin=type(self),
                       sprite=FIREBALL, damage=1, duration=15),
        ]
        world.add(*projs)


@dataclass
class Enemy(StateRender, Movement, Combat):
    hp: int = 3

    def update(self, world):
        self.move()
        if self.hp <= 0 and world:
            world.remove(self)


@dataclass
class Projectile(StateRender, Movement, Combat):
    origin: Optional[type] = None
    duration: Optional[int] = None

    def update(self, world=None):
        self.move()
        if self.duration is not None:
            self.duration -= 1
        if self.duration and self.duration <= 0:
            if world:
                world.remove(self)

    def collide_with_target(self, other):
        coisa = self.collide_with(other) and self.origin != type(other)
        if coisa:
            return True
        return False
