import pyxel
from esper import Processor
from components import Pos, Sprite, Combat, Player, Enemy, Text, Movement, Timer, Projectile, Circle, EnemyProjectile
from math import pi


class Collission(Processor):
    def process(self):
        pid, (playerpos, playersprite, playercombat, player) = self.world.get_components(
            Pos, Sprite, Combat, Player)[0]

        for eid, (pos, sprite) in self.world.get_components(Pos, Sprite):
            if pid == eid:
                continue
            pass

        eprojcetile_components = Pos, Sprite, Combat, EnemyProjectile
        for epid, (eppos, epsprite, epcombat, _) in self.world.get_components(*eprojcetile_components):
            if self.collide_with(eppos, epsprite, playerpos, playersprite):
                self.world.create_entity(
                    Text(str(epcombat.damage)),
                    Pos(playerpos.x, playerpos.y),
                    Movement(speed=1, angle=-90),
                    Timer(25),
                )
                self.world.delete_entity(epid)
                self.attack(epcombat, playercombat)

        projcetile_components = Pos, Sprite, Combat, Projectile
        for pid, (ppos, psprite, pcombat, _) in self.world.get_components(*projcetile_components):
            enemy_components = Pos, Sprite, Combat, Enemy
            for eid, (epos, esprite, ecombat, enemy) in self.world.get_components(*enemy_components):
                if self.collide_with(ppos, psprite, epos, esprite):
                    self.world.delete_entity(pid)
                    self.world.create_entity(
                        Text(str(pcombat.damage)),
                        Pos(epos.x, epos.y),
                        Movement(speed=1, angle=-90),
                        Timer(25),
                    )
                    if self.attack(pcombat, ecombat, eid):
                        player.exp += enemy.exp

                    if player.exp >= player.exp_total:
                        player.exp = player.exp_total - player.exp
                        player.exp_total = int(player.exp_total*pi)
                        player.level += 1
                        playercombat.damage += 1
                        playercombat.max_hp += 1
                        playercombat.hp = playercombat.max_hp
                        self.world.create_entity(
                            Text("LVL UP!"),
                            Pos(playerpos.x, playerpos.y),
                            Movement(speed=1, angle=-90),
                            Timer(25),
                        )
                        self.world.create_entity(
                            Circle(r_inc=1),
                            Pos(playerpos.x, playerpos.y),
                            Timer(25),
                        )
                        self.world.create_entity(
                            Circle(r_inc=2),
                            Pos(playerpos.x, playerpos.y),
                            Timer(25),
                        )
                        self.world.create_entity(
                            Circle(r_inc=3),
                            Pos(playerpos.x, playerpos.y),
                            Timer(25),
                        )

        enemy_components = Pos, Sprite, Combat, Enemy
        for eid, (epos, esprite, ecombat, enemy) in self.world.get_components(*enemy_components):
            if self.collide_with(epos, esprite, playerpos, playersprite):
                if self.attack(ecombat, playercombat):
                    self.world.create_entity(
                        Text(str(ecombat.damage), 7),
                        Pos(epos.x, epos.y),
                        Movement(speed=1, angle=-90),
                        Timer(25),
                    )

    def attack(self, combat1: Combat, combat2: Combat, combat2_id=None):
        combat2.hp -= combat1.damage
        pyxel.play(0, 0)
        if combat2.hp <= 0 and combat2_id:
            self.world.delete_entity(combat2_id)
            pyxel.play(0, 1)
            return True

    @staticmethod
    def collide_with(render1, sprite1, render2, sprite2):
        if render1.x > render2.x + sprite2.w or render2.x > render1.x + sprite1.w:
            return False
        if render1.y > render2.y + sprite2.w or render2.y > render1.y + sprite1.w:
            return False
        return True
