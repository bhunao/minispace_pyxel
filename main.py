import processors
from components import Timer, Pos, Sprite, Speed
import sprites

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
        for diff in range(-100, 100, 50):
            self.world.create_entity(
                Timer(500),
                Pos(150+diff, 100+diff),
                Sprite(sprites.E6),
                Speed(1, f_speed=lambda: pyxel.frame_count % 5 if pyxel.frame_count % 50 > 25 else -1, f_angle=lambda: pyxel.frame_count % 3),
            )

        pyxel.run(self.update, self.draw)

    def update(self):
        return

    def draw(self):
        self.world.process()


App()
