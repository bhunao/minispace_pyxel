import math
from typing import Any, List
import pyxel
from dataclasses import dataclass, field

ME = 0, 32, 0, 8, 8, 0
SHIP1 = (
        (0, 0, 16, 16, 16, 0),
        (0, 16, 16, 16, 16, 0),
)

PROJ1 = (
        (0, 32, 16, 8, 8, 0),
        (0, 40, 16, 8, 8, 0),
)
PROJ2 = (
        (0, 32, 24, 4, 4, 0),
        (0, 36, 24, 4, 4, 0),
        (0, 32, 28, 4, 4, 0),
        (0, 36, 28, 4, 4, 0),
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

    def update(self):
        angle_rad = math.radians(self.angle)
        self.render.x += math.cos(angle_rad) * self.speed
        self.render.y += math.sin(angle_rad) * self.speed


@dataclass
class Player:
    render: Render
    hp: int = 3


@dataclass
class Enemy:
    render: Render
    hp: int = 1

    def update(self):
        pass


def shoot(origin, x, y, angle=90, speed=3) -> List[Projectile]:
    render = Render(x, y, PROJ2)
    return [Projectile(render, angle, speed, origin)]


def out_of_bound(render: Render) -> bool:
    min = -pyxel.width, -pyxel.height
    max = 2*pyxel.width, 2*pyxel.height
    if render.x > max[0] or render.x < min[0]:
        return True
    if render.y > max[0] or render.y < min[0]:
        return True
    return False


class Sim:
    def __init__(self):
        pyxel.init(160, 120)
        pyxel.load('assets.pyxres')

        player_render = Render(pyxel.width//2, pyxel.height//1.25, SHIP1)
        self.player: Player = Player(player_render)
        self.scroll_x: int = 0
        self.scroll_y: int = 0

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
            self.entities[Projectile] += shoot("player",
                                               player.x, player.y, -90, 5)

    def kill(self, entity):
        self.entities[type(entity)].remove(entity)

    def match_entity(self, entity):
        match entity:
            case Enemy():
                if entity.hp <= 0:
                    self.kill(entity)
            case Projectile():
                if out_of_bound(entity.render):
                    self.kill(entity)
                if entity.origin == "enemy":
                    collided_ent = collission_between(
                        entity, self.player)
                    if collided_ent:
                        collided_ent.hp -= 1
                        self.kill(entity)
                if entity.origin == "player":
                    collided_ent = collission_between(
                        entity, self.entities[Enemy])
                    if collided_ent:
                        collided_ent.hp -= 1
                        self.kill(entity)

    def update(self):
        self.player_controller()

        if len(self.entities[Enemy]) < 3:
            x = pyxel.rndi(0, pyxel.width)
            y = pyxel.rndi(0, pyxel.height//4)
            enemy_render = Render(x, y, SHIP1)
            enemy = Enemy(enemy_render)
            self.entities[Enemy].append(enemy)

        for entity_list in self.entities.values():
            for entity in entity_list:
                entity.update()
                self.match_entity(entity)

    def draw(self):
        pyxel.cls(0)
        pyxel.blt(*self.player.render())

        for _type, entity_list in self.entities.items():
            for entity in entity_list:
                pyxel.blt(*entity.render())


Sim()
