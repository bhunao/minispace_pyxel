import pyxel
import sprites
import processors
from esper import Processor
from functions import rainbow
from components import (Circle, GameOver, MoveToPlayer, Pos, Sprite, Combat,
                        Player, Enemy, Projectile, EnemyProjectile, Text,
                        Timer)


class Game(Processor):
    def process(self):
        player = self.world.get_components(Combat, Player)
        pid, (pcombat, _) = player[0]

        over_list = self.get_components(GameOver)
        game_over = len(over_list) <= 0
        print(game_over, pcombat.hp, bool(game_over))
        if pcombat.hp <= 0 and not game_over:
            self.world.create_entity(
                Text("GAMEOVER"),
                Timer(15),
                Pos(pyxel.width//2-20, pyxel.height//2-20),
                GameOver()
            )
            print("hp é zero", pcombat)
            self.world.delete_entity(pid)
            self.world.remove_processor(processors.EnemySpawner)
            self.world.add_processor(processors.EnemySpawner())
        elif pcombat.hp <= 0 and game_over:
            print("game over na tela")
        elif pcombat.hp >= 0 and not game_over:
            print("outro")
            pyxel.text(60, 60, "GAME OVER!", rainbow())
            for id, _ in over_list:
                self.world.delete_entity(id)
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
