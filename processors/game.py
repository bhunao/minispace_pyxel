import pyxel
import sprites
import processors
from esper import Processor
from functions import rainbow
from components import (Circle, MoveToPlayer, Pos, Sprite, Combat, Player,
                        Enemy, Projectile, EnemyProjectile, Timer)


class Game(Processor):
    def process(self):
        pid, (pcombat, _) = self.world.get_components(
            Combat, Player)[0]

        if pcombat.hp <= 0:
            pyxel.text(60, 60, "GAME OVER!", rainbow())
            self.world.delete_entity(pid)

            self.world.remove_processor(processors.EnemySpawner)
            self.world.add_processor(processors.EnemySpawner())
            for id, _ in self.world.get_components(Enemy):
                self.world.delete_entity(id)
            for id, _ in self.world.get_components(Projectile):
                self.world.delete_entity(id)
            for id, _ in self.world.get_components(EnemyProjectile):
                self.world.delete_entity(id)
            for id, _ in self.world.get_components(Circle):
                self.world.delete_entity(id)
            self.reset()

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
        self.world.create_entity(
            Circle(r=25, f=lambda x: .2 * pyxel.sin(x) + .5),
            Sprite(
                sprite=[[0, 0, 0, 0, 0, 0]]
            ),
            Pos(
                x=pyxel.width//2,
                y=pyxel.height//2,
            ),
            MoveToPlayer(2),
            Timer(525),
        )
