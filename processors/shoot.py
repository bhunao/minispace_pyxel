import pyxel
import sprites
from esper import Processor
from components import BarrierGun, CircularMovement, MoveF, Pos, Gun, Movement, Enemy, EnemyProjectile, Sprite, Timer, Combat, Player, FourGun, RotationGun, FourRotationGun
from functions import frame_cd, center_of
from math import degrees, atan2


class Shoot(Processor):
    def process(self):
        for gun in self.get_components(RotationGun, Pos, Enemy, Combat, Sprite):
            _id, (gun, pos, enemy, combat, sprite) = gun
            if frame_cd(gun.cd):
                angle = gun.angle

                self.world.create_entity(
                    EnemyProjectile(),
                    Pos(*center_of(sprite, pos)),
                    Sprite(sprite=sprites.BULLET2),
                    Movement(speed=gun.speed, angle=angle),
                    Timer(gun.timer),
                    Combat(damage=combat.damage),
                )
                if gun.inc:
                    gun.angle += gun.inc

        for gun in self.get_components(FourRotationGun, Pos, Enemy, Combat, Sprite):
            _id, (gun, pos, enemy, combat, sprite) = gun
            if frame_cd(gun.cd):
                for angle in range(0, 360, 90):
                    x, y = center_of(sprite, pos)
                    x -= sprites.BULLET2[0][3] // 2
                    y -= sprites.BULLET2[0][4] // 2
                    self.world.create_entity(
                        EnemyProjectile(),
                        Pos(x, y),
                        Sprite(sprite=sprites.BULLET2),
                        Movement(speed=gun.speed, angle=angle + gun.angle),
                        Timer(gun.timer),
                        Combat(damage=combat.damage),
                    )
            if gun.inc:
                gun.angle += gun.inc

        for gun in self.get_components(BarrierGun, Pos, Enemy, Combat, Sprite):
            _id, (gun, pos, enemy, combat, sprite) = gun
            if frame_cd(gun.cd):
                for angle in range(0, 360, 90):
                    x, y = center_of(sprite, pos)
                    x -= sprites.BULLET2[0][3] // 2
                    y -= sprites.BULLET2[0][4] // 2
                    self.world.create_entity(
                        EnemyProjectile(),
                        Pos(x, y-20),
                        Sprite(sprite=sprites.BULLET2),
                        Movement(speed=gun.speed, angle=90),
                        CircularMovement(speed=gun.speed*2,
                                         angle=0,
                                         radius=gun.inc),
                        Timer(gun.timer),
                        Combat(damage=combat.damage),
                    )

        for gun in self.get_components(FourGun, Pos, Enemy, Combat, Sprite):
            _id, (gun, pos, enemy, combat, sprite) = gun
            if frame_cd(gun.cd):
                for angle in range(0, 360, 90):
                    self.world.create_entity(
                        EnemyProjectile(),
                        Pos(*center_of(sprite, pos)),
                        Sprite(sprite=sprites.BULLET2),
                        Movement(speed=gun.speed, angle=angle),
                        Timer(gun.timer),
                        Combat(damage=combat.damage),
                    )

        player = self.world.get_components(
            Pos, Player, Sprite)

        if not player:
            return

        _, (player, _, psprite) = player[0]

        for gun in self.get_components(Gun, Pos, Enemy, Combat, Sprite):
            _id, (gun, pos, enemy, combat, sprite) = gun
            if frame_cd(gun.cd):
                angle = gun.angle
                if gun.aim_target:
                    px, py = center_of(psprite, player)
                    x, y = center_of(sprite, pos)
                    dx = x - px
                    dy = y - py
                    angle = - degrees(atan2(dx, dy)) - 90

                x, y = center_of(sprite, pos)
                self.world.create_entity(
                    EnemyProjectile(),
                    Pos(*center_of(sprite, pos)),
                    Sprite(sprite=sprites.BULLET2),
                    Movement(speed=gun.speed, angle=angle),
                    Timer(gun.timer),
                    Combat(damage=combat.damage),
                )
