from dataclasses import dataclass
from typing import Optional
from components import Render, Movement


@dataclass
class Player(Render, Movement):
    hp: int = 3


@dataclass
class Enemy(Render, Movement):
    hp: int = 3


@dataclass
class Projectile(Render, Movement):
    origin: Optional[type] = None

    def collide_with_target(self, other):
        coisa = self.collide_with(other) and self.origin != type(other)
        print(coisa)
        if coisa:
            return True
        return False
