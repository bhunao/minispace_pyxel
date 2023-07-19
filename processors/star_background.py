from esper import Processor
from components import Pos, Sprite, Combat, Player, Enemy, Movement
from sprites import WARRIOR, DOWN
from functions import rndxy


class EnemySpawner(Processor):
    def __init__(self) -> None:
        super().__init__()
        self.stars: list = [rndxy() for _ in range(25)]

    def process(self):
        for start in self.stars

        pid, (playerpos, playersprite, pcombat, player) = self.world.get_components(
            Pos, Sprite, Combat, Player)[0]

        comps = self.world.get_components(Enemy)
        if len(comps) <= 5:
            x, y = rndxy()
            y = - 5
            self.world.create_entity(
                Sprite(
                    states=WARRIOR,
                    current_state=DOWN
                ),
                Pos(
                    x=x,
                    y=y,
                ),
                Movement(speed=1),
                Enemy(),
                Combat(hp=player.level//2+1, damage=player.level//2+1),
            )
