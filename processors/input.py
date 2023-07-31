import pyxel
from items import Items
import sprites
from esper import Processor
from components import (MoveF, MoveToEnemy, MoveX, Projectile, Pos, Sprite, CircularMovement, Timer,
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
        self.cd = 10

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
        if not frame_cd(self.cd):
            return

        bullet_mult = player.bullets + player.level
        sprite = sprites.BULLET
        angle = -90
        start = -2*bullet_mult
        stop = 2*bullet_mult
        step = (abs(start) + abs(stop)) // bullet_mult

        if bullet_mult > 1:
            angles = range(start, stop + step, step)
        else:
            angles = [0]

        for ang_dif in angles:
            x = pos.x + psprite.w//2 - sprite[0][3] // 2 + ang_dif
            self.world.create_entity(
                Projectile(),
                Pos(x=x, y=pos.y),
                Sprite(sprite=sprites.BULLET),
                Movement(speed=3, angle=angle+ang_dif),
                MoveX(speed=4, f=lambda x: sin(x)),
                Timer(35),
                Combat(damage=combat.damage),
            )

    def spray_attack(self, pos, combat, psprite, player):
        bullet_mult = player.bullets + player.level
        if bullet_mult > 10:
            pass
        if not frame_cd(10//bullet_mult):
            return

        sprite = sprites.BULLET
        x = pos.x + psprite.w//2 - sprite[0][3] // 2
        angle = sin(pyxel.frame_count % 90) * 15
        angle -= 90

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
        if not frame_cd(self.cd):
            return
        bullet_mult = player.bullets + player.level
        sprite = sprites.BULLET
        x = pos.x + psprite.w//2 - sprite[0][3] // 2
        angle = -90

        start = -25
        stop = 25
        step = (abs(start) + abs(stop)) // bullet_mult
        if bullet_mult > 1:
            angles = range(start, stop + step, step)
        else:
            angles = [0]

        for ang_dif in angles:
            self.world.create_entity(
                Projectile(),
                Pos(x=x, y=pos.y),
                Sprite(sprite=sprites.BULLET),
                Movement(speed=4, angle=angle+ang_dif),
                Timer(35),
                Combat(damage=combat.damage),
            )

    def star_attack(self, pos, combat, psprite, player):
        if not frame_cd(self.cd):
            return

        bullet_mult = (player.bullets + player.level) * 3
        sprite = sprites.BULLET
        for angle in range(0, 360, 360//bullet_mult):
            x = pos.x + psprite.w//2 - sprite[0][3] // 2
            self.world.create_entity(
                Projectile(),
                Pos(x=x, y=pos.y),
                Sprite(sprite=sprites.BULLET),
                CircularMovement(speed=1, angle=angle),
                MoveToEnemy(speed=4, angle=-90),
                Timer(20),
                Combat(damage=combat.damage),
            )

    def process(self):
        for ent, (pos, combat, psprite, player) in self.world.get_components(Pos, Combat, Sprite, Player):
            pos.x = min(pos.x, pyxel.width-4)
            pos.x = max(pos.x, 0)

            pos.y = min(pos.y, pyxel.height-4)
            pos.y = max(pos.y, 0)
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
            if pyxel.btnp(pyxel.KEY_6):
                player.bullets += 1
            if pyxel.btnp(pyxel.KEY_1):
                entities.spinning_jack(self.world.create_entity)
                self.world.create_entity(
                    Text("spinning_jack"),
                    Pos(10, 50),
                    Timer(20)
                )
