import processors
from components import Timer, Pos, Sprite, Speed
import sprites, entities

import esper
import pyxel


class App:
    def __init__(self) -> None:
        pyxel.init(220, 180)
        pyxel.load("assets.pyxres")
        # pyxel.playm(0, loop=True)

        self.world = esper.World()
        self.world.add_processor(processors.Clock())
        self.world.add_processor(processors.SpriteRender())
        self.world.add_processor(processors.Movement())
        self.world.add_processor(processors.Collission())
        for diff in range(-100, 100, 50):
            self.world.create_entity(
                Timer(500),
                Pos(150+diff, 100+diff),
                Sprite(sprites.COLOR),
                Speed(1, f_speed=lambda: pyxel.frame_count % 5, f_angle=lambda: pyxel.frame_count % 5),
            )
            self.world.create_entity(*entities.rotational_boss)

        pyxel.run(self.update, self.draw)

    def update(self):
        return

    def draw(self):
        pyxel.cls(0)
        self.world.process()


App()
