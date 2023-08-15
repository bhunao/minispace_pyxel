from esper import Processor
from components import Timer
import pyxel


class Clock(Processor):
    def process(self):
        for components in self.world.get_components(Timer):
            id, (timer,) = components
            pyxel.text(10, 10, str(timer.time), 15)
            timer.time -= 1
            if timer.time <= 0:
                self.world.delete_entity(id)
