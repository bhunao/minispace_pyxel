import pyxel
from processors.input import InputHandler
import sprites
from esper import Processor
from items import Items
from components import (Pos, Sprite, Combat, Player, Enemy,
                        Text, Movement, Timer, Projectile, Circle,
                        EnemyProjectile, Item)
from math import pi
from random import choice


class Collission(Processor):
    def display_dmg(self, pos, combat):
        self.world.create_entity(
            Text(str(combat.damage)),
            Pos(pos.x, pos.y),
            Movement(speed=1, angle=-90),
            Timer(25),
        )

    def create_item(self, pos, item=None):
        item = choice([*Items])
        sprite = sprites.HEART if item == Items.heart else sprites.PLUS_ONE
        self.world.create_entity(
            Item(item),
            Pos(pos.x, pos.y),
            Sprite(sprite),
            Timer(150),
            Movement(1, angle=90),
        )

    def level_up(self, player, pos, combat):
        if player.exp >= player.exp_total:
            player.exp = player.exp_total - player.exp
            player.exp_total = int(player.exp_total*pi)
            player.level += 1
            combat.hp = combat.max_hp
            self.world.create_entity(
                Text("LVL UP!"),
                Pos(pos.x, pos.y),
                Movement(speed=1, angle=-90),
                Timer(25),
            )
            self.world.create_entity(
                Circle(r_inc=1),
                Pos(pos.x, pos.y),
                Timer(50),
            )
            self.world.create_entity(
                Circle(r_inc=2),
                Pos(pos.x, pos.y),
                Timer(25),
            )

    def process(self):
        player = self.world.get_components(
            Pos, Sprite, Combat, Player)

        if not player:
            return

        pid, (playerpos, playersprite, playercombat, player) = player[0]

        for iid, components in self.get_components(Item, Pos, Sprite):
            item, ipos, isprite = components
            if self.collide_with(ipos, isprite, playerpos, playersprite):
                input_handler = InputHandler()
                if item.item == Items.heart:
                    playercombat.hp += 1
                else:
                    input_handler.attack_style = item.item
                    player.bullets += 1
                    self.world.remove_processor(InputHandler)
                    self.world.add_processor(input_handler)

                self.world.delete_entity(iid)

        for eid, (pos, sprite) in self.world.get_components(Pos, Sprite):
            if pid == eid:
                continue
            pass

        eprojcetile_components = Pos, Sprite, Combat, EnemyProjectile
        for epid, (eppos, epsprite, epcombat, _) in self.world.get_components(*eprojcetile_components):
            if self.collide_with(eppos, epsprite, playerpos, playersprite):
                self.display_dmg(playerpos, epcombat)
                self.world.delete_entity(epid)
                self.attack(epcombat, playercombat)

        projcetile_components = Pos, Sprite, Combat, Projectile
        for pid, (ppos, psprite, pcombat, _) in self.world.get_components(*projcetile_components):
            enemy_components = Pos, Sprite, Combat, Enemy
            for eid, (epos, esprite, ecombat, enemy) in self.world.get_components(*enemy_components):
                if self.collide_with(ppos, psprite, epos, esprite):
                    self.world.delete_entity(pid)
                    self.display_dmg(epos, pcombat)
                    if self.attack(pcombat, ecombat, eid):
                        player.exp += enemy.exp
                        self.level_up(player, playerpos, playercombat)
                        if pyxel.rndi(0, 15) == 0:
                            self.create_item(epos)

        enemy_components = Pos, Sprite, Combat, Enemy
        for eid, (epos, esprite, ecombat, enemy) in self.world.get_components(*enemy_components):
            if self.collide_with(epos, esprite, playerpos, playersprite):
                if self.attack(ecombat, playercombat):
                    self.display_dmg(epos, ecombat)

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
