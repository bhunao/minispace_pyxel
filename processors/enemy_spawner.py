import pyxel
from esper import Processor
from components import Pos, Sprite, Combat, Player, Enemy, Movement, Gun, FourGun, HPBar, MoveToPlayer
from sprites import WARRIOR, DOWN
import sprites
from functions import rndxy, frame_cd


class EnemySpawner(Processor):
    def process(self):
        pid, (playerpos, playersprite, pcombat, player) = self.world.get_components(
            Pos, Sprite, Combat, Player)[0]

        comps = self.world.get_components(Enemy)
        if len(comps) <= 5:
            x, y = rndxy()
            y = - 5
            match pyxel.frame_count % player.level:
                case 1:
                    self.world.create_entity(
                        Sprite(
                            sprite=sprites.E1
                        ),
                        Pos(
                            x=x,
                            y=y,
                        ),
                        MoveToPlayer(speed=1),
                        Enemy(),
                        Combat(hp=player.level*10,
                               max_hp=player.level*10, damage=1),
                        FourGun(speed=2, angle=0, cd=50),
                        HPBar(),
                    )

                case 2:
                    hp = player.level * 2
                    self.world.create_entity(
                        Sprite(
                            sprite=sprites.E2
                        ),
                        Pos(
                            x=x,
                            y=y,
                        ),
                        MoveToPlayer(speed=1),
                        Enemy(),
                        Combat(hp=hp, max_hp=hp, damage=player.level//2+1),
                        Gun(speed=3, angle=90, aim_target=True, cd=4),
                        HPBar()
                    )

                case 3:
                    hp = player.level * 3
                    self.world.create_entity(
                        Sprite(
                            sprite=sprites.E3
                        ),
                        Pos(
                            x=x,
                            y=y,
                        ),
                        MoveToPlayer(speed=1),
                        Enemy(),
                        Combat(hp=hp, max_hp=hp, damage=player.level//2+1),
                        Gun(speed=1, angle=90, cd=50),
                        HPBar()
                    )

                case _:
                    hp = player.level + 1
                    self.world.create_entity(
                        Sprite(
                            sprite=sprites.SPHERE
                        ),
                        Pos(
                            x=x,
                            y=y,
                        ),
                        MoveToPlayer(speed=1),
                        Enemy(),
                        Combat(hp=hp, max_hp=hp, damage=player.level//2+1),
                    )
