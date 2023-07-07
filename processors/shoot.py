import pyxel
import sprites
from esper import Processor
from components import Pos, Gun, Movement, Enemy, EnemyProjectile, Sprite, Timer, Combat, Player, FourGun
from functions import frame_cd
from math import degrees, atan2


class Shoot(Processor):
    def process(self):
        _, (player, _) = self.world.get_components(
            Pos, Player)[0]

        for _id, (gun, pos, enemy, combat) in self.world.get_components(Gun, Pos, Enemy, Combat):
            if frame_cd(gun.cd):
                angle = 90
                if gun.aim_target:
                    dx = pos.x - player.x
                    dy = pos.y - player.y
                    angle = - degrees(atan2(dx, dy)) - 90

                self.world.create_entity(
                    EnemyProjectile(),
                    Pos(x=pos.x, y=pos.y),
                    Sprite(sprite=sprites.BULLET2),
                    Movement(speed=2, angle=angle),
                    Timer(55),
                    Combat(damage=combat.damage),
                )

        for _id, (gun, pos, enemy, combat) in self.world.get_components(FourGun, Pos, Enemy, Combat):
            if frame_cd(gun.cd):
                # angle = 90
                # if gun.aim_target:
                #     dx = pos.x - player.x
                #     dy = pos.y - player.y
                #     angle = - degrees(atan2(dx, dy)) - 90

                for angle in range(0, 360, 90):
                    self.world.create_entity(
                        EnemyProjectile(),
                        Pos(x=pos.x, y=pos.y),
                        Sprite(sprite=sprites.BULLET2),
                        Movement(speed=2, angle=angle),
                        Timer(gun.timer),
                        Combat(damage=combat.damage),
                    )
