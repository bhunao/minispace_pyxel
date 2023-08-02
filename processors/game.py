import pyxel
import sprites
import processors
from esper import Processor
from components import (Circle, Pos, Sprite, Combat,
                        Player, Enemy, Projectile, EnemyProjectile, Text)


class Game(Processor):
    def process(self):
        player = self.world.get_components(Combat, Player)
        if player:
            pid, (pcombat, _) = player[0]
            if pcombat.hp <= 0:
                self.world.create_entity(
                    Text("GAME OVER!"),
                    Pos(pyxel.width//2-20, pyxel.height//2-20),
                )
                self.world.create_entity(
                    Text("press SPACE to restart..."),
                    Pos(pyxel.width//2-50, pyxel.height//2),
                )
                self.world.delete_entity(pid)
        elif not player:
            if pyxel.btnp(pyxel.KEY_SPACE):
                self.world.remove_processor(processors.EnemySpawner)
                self.world.add_processor(processors.EnemySpawner())
                self.delete_entities()
                self.reset()

    def delete_entities(self):
        for id, _ in self.get_components(Enemy):
            self.world.delete_entity(id)
        for id, _ in self.get_components(Enemy):
            self.world.delete_entity(id)
        for id, _ in self.get_components(Projectile):
            self.world.delete_entity(id)
        for id, _ in self.get_components(EnemyProjectile):
            self.world.delete_entity(id)
        for id, _ in self.get_components(Circle):
            self.world.delete_entity(id)

    def reset(self):
        for id, _ in self.get_components(Text):
            self.world.delete_entity(id)

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
