import pyxel
from items import AttackStyle
import sprites
from esper import Processor
from components import (MoveF, MoveToEnemy, Projectile, Pos, Sprite, CircularMovement, Timer,
                        Combat, Movement, Player, Text)
from functions import frame_cd
from math import sin
import entities


class InputHandler(Processor):
    attack_style: AttackStyle = AttackStyle.normal_attack
    cd: int = 10
    select: bool = False

    def player_attack(self, pos, combat, psprite, player):
        match self.attack_style:
            case AttackStyle.normal_attack:
                return self.normal_attack(pos, combat, psprite, player)
            case AttackStyle.spray_attack:
                return self.spray_attack(pos, combat, psprite, player)
            case AttackStyle.zizag_attack:
                return self.zigzag_attack(pos, combat, psprite, player)
            case AttackStyle.star_attack:
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
            x = pos.x + psprite.w//2 - sprite[0][3] // 2
            self.world.create_entity(
                Projectile(),
                Pos(x=x, y=pos.y),
                Sprite(sprite=sprites.BULLET),
                CircularMovement(speed=3, angle=angle+ang_dif),

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

        bullet_mult = (player.bullets + player.level) * 2
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
            if pyxel.btnp(pyxel.KEY_6):
                player.bullets += 1

            if self.select:
                n = -1
                for i in range(49, 59):
                    if pyxel.btnp(i):
                        n = i-49
                        break

                if n >= 0:
                    ent = entities.entities_list[n]
                    ent(self.world.create_entity)
                    self.world.create_entity(
                        Text(str(ent.__name__)),
                        Pos(10, 0),
                        Timer(20)
                    )
                    self.select = False
            elif pyxel.btnp(pyxel.KEY_1) and not self.select:
                self.select = True
                for i, enemy in enumerate(entities.entities_list[0:10]):
                    text = f"{i} - {enemy.__name__}"
                    self.world.create_entity(
                        Text(text),
                        Pos(10, 10 + i * 10),
                        Timer(100)
                    )
