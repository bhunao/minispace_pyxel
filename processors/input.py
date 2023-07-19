import pyxel
import sprites
from esper import Processor
from components import Projectile, Pos, Sprite, CircularMovement, Timer, Combat, Enemy, Movement, Player, Text, CircularMovement, MoveXtoPlayer
from functions import frame_cd
from sprites import Sides
from math import degrees, atan2, cos, sin
import entities


class InputHandler(Processor):
    def __init__(self) -> None:
        super().__init__()
        self.player_attack = self.normal_attack

    def zigzag_attack(self, pos, combat, psprite, player):
        sprite = sprites.BULLET
        x = pos.x + psprite.w//2 - sprite[0][3] // 2
        angle = sin(pyxel.frame_count % 90) * 15
        angle -= 90
        angle = -90

        self.world.create_entity(
            Projectile(),
            Pos(x=x, y=pos.y),
            Sprite(sprite=sprites.BULLET),
            Movement(speed=3, angle=angle),
            MoveXtoPlayer(speed=3, angle=angle),
            CircularMovement(speed=2, angle=angle),
            Timer(45),
            Combat(damage=combat.damage),
        )
        angle += 50
        self.world.create_entity(
            Projectile(),
            Pos(x=x, y=pos.y),
            Sprite(sprite=sprites.BULLET),
            Movement(speed=3, angle=angle),
            MoveXtoPlayer(speed=3, angle=angle),
            CircularMovement(speed=2, angle=angle),
            Timer(45),
            Combat(damage=combat.damage),
        )
        angle -= 100
        self.world.create_entity(
            Projectile(),
            Pos(x=x, y=pos.y),
            Sprite(sprite=sprites.BULLET),
            Movement(speed=3, angle=angle),
            MoveXtoPlayer(speed=9, angle=angle),
            CircularMovement(speed=2, angle=angle),
            Timer(45),
            Combat(damage=combat.damage),
        )

    def spray_attack(self, pos, combat, psprite, player):
        sprite = sprites.BULLET
        x = pos.x + psprite.w//2 - sprite[0][3] // 2
        angle = sin(pyxel.frame_count % 90) * 15
        angle -= 90

        self.world.create_entity(
            Projectile(),
            Pos(x=x, y=pos.y),
            Sprite(sprite=sprites.BULLET),
            Movement(speed=4, angle=angle),
            Timer(45),
            Combat(damage=combat.damage),
        )

    def tst(self, pos, combat, psprite, player):
        for side in Sides:
            sprite = sprites.BULLET
            x = pos.x + psprite.w//2 - sprite[0][3] // 2
            self.world.create_entity(
                Projectile(),
                Pos(x=x, y=pos.y),
                Sprite(sprite=sprite),
                CircularMovement(speed=4, angle=side.value),
                Timer(20),
                Combat(damage=combat.damage),
            )

    def normal_attack(self, pos, combat, psprite, player):
        if not frame_cd(5):
            return
        sprite = sprites.BULLET
        x = pos.x + psprite.w//2 - sprite[0][3] // 2
        angle = -90

        start = -25
        stop = 25
        step = (abs(start) + abs(stop)) // player.level
        if player.level > 1:
            for ang_dif in range(start, stop + step, step):
                self.world.create_entity(
                    Projectile(),
                    Pos(x=x, y=pos.y),
                    Sprite(sprite=sprites.BULLET),
                    Movement(speed=4, angle=angle+ang_dif),
                    Timer(35),
                    Combat(damage=combat.damage),
                )
        else:
            self.world.create_entity(
                Projectile(),
                Pos(x=x, y=pos.y),
                Sprite(sprite=sprites.BULLET),
                Movement(speed=4, angle=angle),
                Timer(35),
                Combat(damage=combat.damage),
            )

    def star_attack(self, pos, combat, psprite, player):
        sprite = sprites.BULLET
        for side in Sides:
            sprite = sprites.BULLET
            x = pos.x + psprite.w//2 - sprite[0][3] // 2
            self.world.create_entity(
                Projectile(),
                Pos(x=x, y=pos.y),
                Sprite(sprite=sprite),
                CircularMovement(speed=4, angle=side.value),
                Timer(20),
                Combat(damage=combat.damage),
            )

    def process(self):
        for ent, (pos, combat, psprite, player) in self.world.get_components(Pos, Combat, Sprite, Player):
            if pyxel.btn(pyxel.KEY_A):
                pos.x -= 2
            if pyxel.btn(pyxel.KEY_D):
                pos.x += 2
            if pyxel.btn(pyxel.KEY_W):
                pos.y -= 2
            if pyxel.btn(pyxel.KEY_S):
                pos.y += 2
            if pyxel.btn(pyxel.KEY_SPACE):
                self.player_attack(pos, combat, psprite, player)
            if pyxel.btnp(pyxel.KEY_2):
                self.player_attack = self.normal_attack
            if pyxel.btnp(pyxel.KEY_3):
                self.player_attack = self.spray_attack
            if pyxel.btnp(pyxel.KEY_4):
                self.player_attack = self.star_attack
            if pyxel.btnp(pyxel.KEY_5):
                self.player_attack = self.zigzag_attack
            if pyxel.btnp(pyxel.KEY_1):
                entities.spiral_daniel(self.world.create_entity)
                self.world.create_entity(
                    Text("spinning_jack"),
                    Pos(10, 50),
                    Timer(20)
                )
