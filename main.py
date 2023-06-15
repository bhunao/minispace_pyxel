import math
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


@dataclass
class Render:
    x: float = 0
    y: float = 0
    sprite: tuple = field(default_factory=tuple)

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
    origin: str

    def update(self):
        angle_rad = math.radians(self.angle)

        # Calculate the new x and y coordinates based on the angle and speed
        self.render.x += math.cos(angle_rad) * self.speed
        self.render.y += math.sin(angle_rad) * self.speed


@dataclass
class Player:
    render: Render


class Sim:
    def __init__(self):
        pyxel.init(160, 120)
        pyxel.load('assets.pyxres')

        player_render = Render(pyxel.width//2, pyxel.height//1.25, SHIP1)
        self.player: Player = Player(player_render)
        self.scroll_x: int = 0
        self.scroll_y: int = 0

        self.enemies = []

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
            render = Render(player.x + 4, player.y, PROJ1)
            projectile = Projectile(render, pyxel.frame_count, 2, "EU")
            self.enemies.append(projectile)

    def update(self):
        self.player_controller()
        for enemy in self.enemies:
            enemy.update()

    def draw(self):
        pyxel.cls(0)
        pyxel.blt(*self.player.render())

        for enemy in self.enemies:
            pyxel.blt(*enemy.render())


Sim()
