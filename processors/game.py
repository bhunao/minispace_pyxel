import pyxel
import sprites
from esper import Processor
from components import Pos, Sprite, Combat, Player, Enemy, Text, Movement, Timer, Projectile, Circle, EnemyProjectile
from functions import rainbow


class Game(Processor):
    def process(self):
        pid, (ppos, psprite, pcombat, player) = self.world.get_components(
            Pos, Sprite, Combat, Player)[0]

        if pcombat.hp <= 0:
            pyxel.text(60, 60, "GAME OVER!", rainbow())
            self.world.delete_entity(pid)
            self.reset()

            for id, _ in self.world.get_components(Enemy):
                self.world.delete_entity(id)
            for id, _ in self.world.get_components(Projectile):
                self.world.delete_entity(id)
            for id, _ in self.world.get_components(EnemyProjectile):
                self.world.delete_entity(id)

    def reset(self):
        self.world.create_entity(
            Sprite(
                sprite=sprites.NV1
            ),
            Pos(
                x=pyxel.width//2,
                y=pyxel.height//2,
            ),
            Player(),
            Combat(hp=5, max_hp=5, damage=1)
        )
