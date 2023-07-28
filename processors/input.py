import pyxel
from items import Items
import sprites
from esper import Processor
from components import (MoveF, MoveToEnemy, Projectile, Pos, Sprite, CircularMovement, Timer,
                        Combat, Movement, Player, Text, MoveXtoPlayer)
from functions import frame_cd
from sprites import Sides
from math import sin
import entities


class InputHandler(Processor):
    def __init__(self) -> None:
        super().__init__()
        self.attack_style: Items = Items.normal_attack
        self.n1 = 1
        self.n2 = 1

    def player_attack(self, pos, combat, psprite, player):
        match self.attack_style:
            case Items.normal_attack:
                return self.normal_attack(pos, combat, psprite, player)
            case Items.spray_attack:
                return self.spray_attack(pos, combat, psprite, player)
            case Items.zizag_attack:
                return self.zigzag_attack(pos, combat, psprite, player)
            case Items.star_attack:
                return self.star_attack(pos, combat, psprite, player)

    def zigzag_attack(self, pos, combat, psprite, player):
        if not frame_cd(15):
            return

        sprite = sprites.LASER
        x = pos.x + psprite.w//2 - sprite[0][3] // 2

        n = 35
        start = -n
        stop = n
        step = (abs(start) + abs(stop)) // player.level
        for ang_dif in range(start, stop + step, step):
            self.world.create_entity(
                Projectile(),
                Pos(x=x, y=pos.y),
                Sprite(sprite=sprites.BULLET),
                MoveToEnemy(speed=2, angle=-90),
                MoveF(speed=.1, angle=-90+ang_dif,
                      f=lambda x: sin(x) + x * .1),
                Timer(135),
                Combat(damage=combat.damage),
            )

    def spray_attack(self, pos, combat, psprite, player):
        # if not frame_cd(5):
        # return

        sprite = sprites.BULLET
        x = pos.x + psprite.w//2 - sprite[0][3] // 2
        angle = sin(pyxel.frame_count % 90) * 15
        angle -= 90

        for n in range(player.level):
            mult = 1 if angle > -90 else -1
            diff = pyxel.rndi(-6, 6) * n * mult

            self.world.create_entity(
                Projectile(),
                Pos(x=x, y=pos.y),
                Sprite(sprite=sprites.LASER),
                MoveF(speed=3, angle=angle,
                      f=lambda x: abs(pyxel.sin(x)) + 2),
                Timer(45),
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
        if not frame_cd(10):
            return
        sprite = sprites.BULLET
        for side in Sides:
            sprite = sprites.LASER
            x = pos.x + psprite.w//2 - sprite[0][3] // 2
            self.world.create_entity(
                Projectile(),
                Pos(x=x, y=pos.y),
                Sprite(sprite=sprite),
                CircularMovement(speed=1, angle=side.value),
                Movement(speed=4, angle=-90),
                Timer(20),
                Combat(damage=combat.damage),
            )

    def process(self):
        for ent, (pos, combat, psprite, player) in self.world.get_components(Pos, Combat, Sprite, Player):
            if pyxel.btn(pyxel.KEY_Q):
                self.n2 += 1
            if pyxel.btn(pyxel.KEY_E):
                self.n2 -= 1
            if pyxel.btn(pyxel.KEY_UP):
                self.n1 += 1
            if pyxel.btn(pyxel.KEY_DOWN):
                self.n1 -= 1
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
                self.attack_style = Items.normal_attack
            if pyxel.btnp(pyxel.KEY_3):
                self.attack_style = Items.spray_attack
            if pyxel.btnp(pyxel.KEY_4):
                self.attack_style = Items.star_attack
            if pyxel.btnp(pyxel.KEY_5):
                self.attack_style = Items.zizag_attack
            if pyxel.btnp(pyxel.KEY_1):
                entities.spinning_jack(self.world.create_entity)
                self.world.create_entity(
                    Text("spinning_jack"),
                    Pos(10, 50),
                    Timer(20)
                )
