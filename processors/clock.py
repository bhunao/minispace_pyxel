from esper import Processor
from components import Timer


class Clock(Processor):
    def process(self):
        for id, timer in self.world.get_components(Timer):
            timer = timer[0]
            timer.time -= 1
            if timer.time <= 0:
                self.world.delete_entity(id)
