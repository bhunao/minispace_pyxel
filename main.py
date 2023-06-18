import math
import pyxel
import logging
from typing import Any, List, Tuple
from dataclasses import dataclass


SpriteType = Tuple[int, int, int, int, int, int]


def sprite(x, y, w=8, h=8, image=0, colkey=0) -> SpriteType:
    return image, x, y, w, h, colkey


class Objetcs:
    STARS = (
        sprite(0, 80),
        sprite(8, 80),
        sprite(0, 88),
        sprite(8, 88),
    )


class Ships():
    Blue = (
        sprite(0, 16, 16, 16),
        sprite(16, 16, 16, 16),
    )
    ENEMY1 = (
        sprite(0, 0),
        sprite(0, 8),
        sprite(8, 0),
        sprite(8, 8),
    )
    ENEMY2 = (
        sprite(0, 48, 16, 16),
    )


class Projectiles:
    purple = (
        sprite(24, 0, 4, 4),
    )
    purple_beam = (
        sprite(28, 4, 4, 4),
    )


def collission_between(entity1, entities_list):
    if not isinstance(entities_list, list):
        entities_list = [entities_list]

    for entity2 in entities_list:
        r1 = entity1.render
        r2 = entity2.render
        if r1.x > r2.x + r2.w or r2.x > r1.x + r1.w:
            continue
        if r1.y > r2.y + r2.w or r2.y > r1.y + r1.w:
            continue
        return entity2
    return


@dataclass
class Render:
    x: float
    y: float
    sprite: tuple

    def __post_init__(self):
        self.w: int = self.sprite[0][3]
        self.h: int = self.sprite[0][4]

    def __call__(self):
        frames_per_sprite = 5
        sprite_index = pyxel.frame_count % (
            frames_per_sprite * len(self.sprite)) // frames_per_sprite
        return self.x, self.y, *self.sprite[sprite_index]


@dataclass
class Projectile:
    render: Render
    angle: float
    speed: float
    origin: Any


@dataclass
class Player:
    render: Render
    hp: int = 3


@dataclass
class Gun:
    damage: int = 1
    cd: int = 0
    cd_time: int = 25

    def cooldown(self):
        if self.cd + self.cd_time < pyxel.frame_count:
            self.cd = pyxel.frame_count
            return True
        return False


@dataclass
class Enemy:
    render: Render
    hp: int = 1
    gun: Gun | None = None


@dataclass
class Text:
    text: str
    colkey: int
    pos: Tuple[int, int] | str

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        if isinstance(self.pos, tuple):
            return self.pos[0], self.pos[1], self.text, self.colkey
        elif isinstance(self.pos, str):
            if self.pos == "center":
                x = pyxel.width / 2 - len(self.pos) * 2
                y = pyxel.height / 2 - 3
                return x, y, self.text, self.colkey


def shoot(origin, angle=90, speed=3, sprite=Projectiles.purple) -> List[Projectile]:
    r = origin.render
    render = Render(r.x + r.w//2, r.y + r.h//2, sprite)
    return [Projectile(render, angle, speed, type(origin))]


def out_of_bound(render: Render) -> bool:
    min = -pyxel.width, -pyxel.height
    max = 2*pyxel.width, 2*pyxel.height
    if render.x > max[0] or render.x < min[0]:
        return True
    if render.y > max[0] or render.y < min[0]:
        return True
    return False


waves = {
    0: {
        "Entity": Enemy,
        "sprite": Ships.ENEMY2,
        "quantity": 5,
    }
}


def wave_gen(waves):
    for wave in waves:
        yield wave

    logging.info("end of waves")


def r_x():
    return pyxel.rndi(0, pyxel.width)


class Sim:
    def __init__(self):
        pyxel.init(180, 140)
        pyxel.load('assets.pyxres')

        player_render = Render(pyxel.width//2, pyxel.height//1.25, Ships.Blue)
        self.player: Player = Player(player_render)
        self.scroll_x: int = 0
        self.scroll_y: int = 0

        w = [
            [Enemy(Render(r_x(), -10, Ships.ENEMY1)) for x in range(1)],
            [Enemy(Render(r_x(), -10, Ships.ENEMY2)) for x in range(3)],
            [Enemy(Render(r_x(), -10, Ships.ENEMY1)) for x in range(5)],
            [Enemy(Render(r_x(), -10, Ships.ENEMY2)) for x in range(7)],
            [Enemy(Render(r_x(), -10, Ships.ENEMY1)) for x in range(9)],
        ]
        self.waves = wave_gen(w)
        self.end = False

        self.bg = []
        for _ in range(10):
            x = pyxel.rndi(0, pyxel.width)
            y = pyxel.rndi(0, pyxel.height)
            sprite = Objetcs.STARS[pyxel.rndi(0, len(Objetcs.STARS)-1)]
            star = Render(x, y, tuple([sprite]))
            self.bg.append(star)

        self.entities = {
            Projectile: [],
            Enemy: []
        }

        pyxel.run(self.update, self.draw)

    def player_controller(self):
        player = self.player.render
        if pyxel.btn(pyxel.KEY_LEFT):
            player.x = (player.x - 1) % pyxel.width
        if pyxel.btn(pyxel.KEY_RIGHT):
            player.x = (player.x + 1) % pyxel.width
        if pyxel.btn(pyxel.KEY_DOWN):
            player.y = (player.y + 1) % pyxel.height
        if pyxel.btn(pyxel.KEY_UP):
            player.y = (player.y - 1) % pyxel.height
        if pyxel.btn(pyxel.KEY_SPACE):
            self.entities[Projectile] += shoot(self.player, -90,
                                               5, sprite=Projectiles.purple_beam)

    def kill(self, entity):
        self.entities[type(entity)].remove(entity)

    def match_entity(self, entity):
        match entity:
            case Enemy():
                entity.render.x += pyxel.sin(pyxel.frame_count * 6)
                entity.render.y += 1

                if entity.hp <= 0:
                    self.kill(entity)
                    pyxel.play(0, 1)
                if out_of_bound(entity.render):
                    self.kill(entity)

                if entity.gun and entity.gun.cooldown():
                    self.entities[Projectile] += shoot(
                        entity, sprite=Projectiles.purple)
            case Projectile():
                angle_rad = math.radians(entity.angle)
                entity.render.x += math.cos(angle_rad) * entity.speed
                entity.render.y += math.sin(angle_rad) * entity.speed

                if out_of_bound(entity.render):
                    self.kill(entity)
                if entity.origin == Enemy:
                    collided_ent = collission_between(
                        entity, self.player)
                    if collided_ent:
                        collided_ent.hp -= 1
                        self.kill(entity)
                if entity.origin == Player:
                    collided_ent = collission_between(
                        entity, self.entities[Enemy])
                    if collided_ent:
                        collided_ent.hp -= 1
                        self.kill(entity)
            case Gun():
                pass

    def update(self):
        self.player_controller()

        for item in self.bg:
            _max = pyxel.height + 5
            item.y = (item.y + 3) % _max

        if len(self.entities[Enemy]) <= 0:
            try:
                next_wave = next(self.waves)
                print((next_wave))
                self.entities[Enemy] += next_wave
            except StopIteration:
                self.end = True

        for entity_list in self.entities.values():
            for entity in entity_list:
                self.match_entity(entity)

    def draw(self):
        pyxel.cls(0)
        for item in self.bg:
            pyxel.blt(*item())
        pyxel.blt(*self.player.render())
        for entity_list in self.entities.values():
            for entity in entity_list:
                pyxel.blt(*entity.render())

        if self.end:
            text = "FIM!"
            x = pyxel.width / 2 - len(text) * 2
            y = pyxel.height / 2 - 3

            pyxel.text(x, y, text, 5)
            pyxel.text(x-1, y-1, text, pyxel.frame_count % 10)


Sim()
