import pyxel
from esper import Processor
from components import Pos, Enemy
from waves import waves


class EnemySpawner(Processor):
    def __init__(self) -> None:
        super().__init__()
        self.wave_n: int = 0
        self.waves: list = waves

    def spawn_wave(self):
        waves_size = len(self.waves)
        if self.wave_n < waves_size:
            func, args, quantity, spawn_next = self.waves[self.wave_n]
            for _ in range(quantity):
                func(self.world.create_entity, *args)
            self.wave_n += 1
            if spawn_next:
                self.spawn_wave()

    def process(self):
        enemy_len = len(self.world.get_components(Enemy))
        if enemy_len == 0:
            self.spawn_wave()

        for eid, (pos, _) in self.world.get_components(Pos, Enemy):
            if pos.y > pyxel.height + 64:
                self.world.delete_entity(eid)
