from dataclasses import dataclass
from typing import Optional
from engine.components import StateRender, Movement


@dataclass
class Player(StateRender, Movement):
    hp: int = 3


@dataclass
class Enemy(StateRender, Movement):
    hp: int = 3


@dataclass
class Projectile(StateRender, Movement):
    origin: Optional[type] = None

    def collide_with_target(self, other):
        coisa = self.collide_with(other) and self.origin != type(other)
        print(coisa)
        if coisa:
            return True
        return False
