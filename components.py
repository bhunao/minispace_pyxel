import pyxel
from typing import Callable, Dict, Optional, Sequence
from math import degrees, radians, cos, sin, atan2
from dataclasses import dataclass


@dataclass
class Render:
    sprite: Sequence[tuple] = ((0, 0, 0, 8, 8, 0), )
    x: float = 0
    y: float = 0
    w: int = sprite[0][3]
    h: int = sprite[0][4]

    def collide_with(self, other):
        if self.x > other.x + other.w or other.x > self.x + self.w:
            return False
        if self.y > other.y + other.w or other.y > self.y + self.w:
            return False
        return True

    def draw(self):
        nframes = 5
        i = pyxel.frame_count % (nframes * len(self.sprite)) // nframes
        pyxel.blt(self.x, self.y, *self.sprite[i])


@dataclass
class StateRender(Render):
    states: Optional[Dict] = None
    current_state: Optional[type] = None

    def draw(self):
        if self.states and self.current_state:
            sprite = self.states[self.current_state]
        else:
            sprite = self.sprite
        nframes = 5
        i = pyxel.frame_count % (nframes * len(sprite)) // nframes
        pyxel.blt(self.x, self.y, *sprite[i])


@dataclass
class Movement:
    x: float = 0
    y: float = 0
    speed: float = 0
    angle: float = 0

    def move(self):
        angle_rad = radians(self.angle)
        self.x += cos(angle_rad) * self.speed
        self.y += sin(angle_rad) * self.speed

    def move_to_target(self, target=None):
        if target is None:
            self.move()
            return

        dx = self.x - target.x
        dy = self.y - target.y
        angle = - degrees(atan2(dx, dy)) - 90
        self.angle = angle
        self.move()

    def move_away_from(self, target=None):
        if target is None:
            self.move()
            return

        dx = self.x - target.x
        dy = self.y - target.y
        angle = degrees(atan2(dx, dy)) - 90
        self.angle = angle
        self.move()


@dataclass
class MovementMinDistance(Movement):
    def move_keep_distance(self, target=None):
        if target is None:
            self.move()
        else:
            n1 = (self.x - target.x)**2
            n2 = (self.y - target.y)**2
            distance = pyxel.sqrt(n1 + n2)
            if distance > 75:
                self.move_to_target(target)
            elif distance < 50:
                self.move_away_from(target)


@dataclass
class Combat:
    hp: int = 1
    max_hp: int = hp
    damage: int = 1
    dmg_cd: int = 0
    dmg_interval: int = 10

    def attack(self, other, game=None):
        other.dmg_cd = pyxel.frame_count
        other.hp -= self.damage
        if game:
            game.add(FloatingText(
                x=other.x, y=other.y, text=str(self.damage)))
        if other.hp <= 0 and game:
            game.remove(other)
            pyxel.play(0, 0)


@dataclass
class FloatingText:
    text: str = "PLACEHOLDER"
    x: float = 0
    y: float = 0
    colkey: int = 9
    duration: int = 25

    def update(self, game):
        self.y -= 0.5
        self.duration -= 1
        if self.duration <= 0 and game:
            game.remove(self)

    def draw(self):
        pyxel.text(self.x, self.y, self.text, self.colkey)
