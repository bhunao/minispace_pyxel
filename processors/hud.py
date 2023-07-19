import pyxel
from esper import Processor
from components import Pos, Sprite, Combat, Enemy, Player, HPBar
from functions import rainbow


class HUD(Processor):
    def process(self):
        _, (pos, sprite, combat, player) = self.world.get_components(
            Pos, Sprite, Combat, Player)[0]

        tamanhoBarra = pyxel.width - 20
        percenteExp = (player.exp / player.exp_total)

        xlife = pos.x
        ylife = pos.y - 4
        hp = combat.hp if combat.hp > 0 else 1
        percenteLife = (hp / combat.max_hp)
        healthbar_size = sprite.w * percenteLife if combat.hp > 0 else 0

        pyxel.rect(10, pyxel.height-7, tamanhoBarra * percenteExp, 4, 3)
        pyxel.rectb(10, pyxel.height-7, tamanhoBarra, 4, 7)

        pyxel.rect(xlife, ylife, healthbar_size, 1, 8)

        for _id, (pos, combat, sprite, hpbar) in self.world.get_components(Pos, Combat, Sprite, HPBar):
            hp = combat.hp if combat.hp > 0 else 1
            percenteLife = (hp / combat.max_hp)
            healthbar_size = sprite.w * percenteLife if combat.hp > 0 else 0
            pyxel.rect(pos.x, pos.y-4, healthbar_size, 2, 5)
