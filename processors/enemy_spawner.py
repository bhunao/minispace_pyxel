import pyxel
from esper import Processor
from components import Pos, Enemy
from waves import waves


class EnemySpawner(Processor):
    wave_n: int = 0
    waves: list = waves
    wait: int = 0

    def spawn_wave(self):
        waves_size = len(self.waves)
        if self.wave_n < waves_size:
            wave_line = self.waves[self.wave_n]
            match wave_line:
                case [func, args, quantity, wait_time]:
                    for _ in range(quantity):
                        func(self.world.create_entity, *args)
                    self.wave_n += 1
                    self.wait = wait_time

    def process(self):
        for eid, (pos, _) in self.world.get_components(Pos, Enemy):
            if pos.y > pyxel.height + 64:
                self.world.delete_entity(eid)

        for _, comps in self.get_components(Enemy, Pos):
            _, pos = comps
            if pos.y < 100 and self.wait == -1:
                return

        if self.wait > 0:
            self.wait -= 1
        else:
            self.spawn_wave()
