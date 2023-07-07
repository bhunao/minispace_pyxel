import pyxel
import sprites
from esper import Processor
from components import Projectile, Pos, Sprite, CircularMovement, Timer, Combat, Enemy, Movement, Player
from functions import frame_cd
from sprites import Sides
from math import degrees, atan2, cos, sin


class InputHandler(Processor):
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
            if pyxel.btn(pyxel.KEY_E):
                _, (epos, esprite, ecombat, _) = self.world.get_components(
                    Pos, Sprite, Combat, Enemy)[-1]
                sprite = sprites.BULLET
                x = pos.x + psprite.w//2 - sprite[0][3] // 2

                angle = sin(pyxel.frame_count % 90) * 10
                print(angle)
                angle -= 90

                self.world.create_entity(
                    Projectile(),
                    Pos(x=x, y=pos.y),
                    Sprite(sprite=sprites.BULLET),
                    Movement(speed=4, angle=angle),
                    Timer(45),
                    Combat(damage=combat.damage),
                )
            if pyxel.btn(pyxel.KEY_Q) and frame_cd(5):
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
            if pyxel.btn(pyxel.KEY_SPACE) and frame_cd(5):
                _, (epos, esprite, ecombat, _) = self.world.get_components(
                    Pos, Sprite, Combat, Enemy)[-1]
                sprite = sprites.BULLET
                x = pos.x + psprite.w//2 - sprite[0][3] // 2

                dx = pos.x - epos.x
                dy = pos.y - epos.y
                angle = - degrees(atan2(dx, dy)) - 90
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
                            Timer(45),
                            Combat(damage=combat.damage),
                        )
                else:
                    self.world.create_entity(
                        Projectile(),
                        Pos(x=x, y=pos.y),
                        Sprite(sprite=sprites.BULLET),
                        Movement(speed=4, angle=angle),
                        Timer(45),
                        Combat(damage=combat.damage),
                    )
