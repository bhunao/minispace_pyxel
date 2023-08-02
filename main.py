import sprites
from components import (Player, Sprite, Pos, Combat, Star, Movement)
from functions import rndxy
import processors

import esper
import pyxel


class App:
    def __init__(self) -> None:
        pyxel.init(220, 180)
        pyxel.load("assets.pyxres")
        # pyxel.playm(0, loop=True)

        self.world = esper.World()
        self.world.add_processor(processors.Draw())
        self.world.add_processor(processors.Move())
        self.world.add_processor(processors.EnemySpawner())
        self.world.add_processor(processors.HUD())
        self.world.add_processor(processors.Clock())
        self.world.add_processor(processors.InputHandler())
        self.world.add_processor(processors.Collission())
        self.world.add_processor(processors.Render())
        self.world.add_processor(processors.Shoot())
        self.world.add_processor(processors.Game())

        self.world.create_entity(
            Sprite(
                sprite=sprites.NV1
            ),
            Pos(
                x=pyxel.width//2,
                y=pyxel.height//2,
            ),
            Player(level=1),
            Combat(hp=5, max_hp=5, damage=1)
        )

        for _ in range(125):
            x, y = rndxy()
            speed = pyxel.rndi(4, 5)
            sprite = [sprites.STARS[pyxel.rndi(0, len(sprites.STARS)-1)]]
            self.world.create_entity(
                Sprite(sprite=sprite),
                Pos(x=x, y=y),
                Movement(speed=speed, angle=90),
                Star(),
            )

        pyxel.run(self.update, self.draw)

    def update(self):
        return

    def draw(self):
        pyxel.cls(0)
        self.world.process()


App()
