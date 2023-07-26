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
        for eid, (pos, _) in self.world.get_components(Pos, Enemy):
            if pos.y > pyxel.height + 64:
                self.world.delete_entity(eid)

        for _, comps in self.get_components(Enemy, Pos):
            _, pos = comps
            if pos.y < 100:
                return
        self.spawn_wave()
