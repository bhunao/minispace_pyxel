import pyxel
from esper import Processor
from components import Sprite, Pos


class Draw(Processor):
    def __init__(self) -> None:
        super().__init__()

    def draw_sprite(self, sprite: Sprite, pos: Pos):
        nframes = 5
        i = pyxel.frame_count % (nframes * len(sprite.sprite)) // nframes
        pyxel.blt(pos.x, pos.y, *sprite.sprite[i])

    def process(self):
        for _, (sprite, pos) in self.world.get_components(Sprite, Pos):
            if sprite.states is None:
                self.draw_sprite(sprite, pos)
            else:
                self.draw_state_sprite(sprite, pos)

    @staticmethod
    def draw_state_sprite(sprite, pos):
        if sprite.states and sprite.current_state:
            image = sprite.states[sprite.current_state]
        else:
            image = sprite.image
        nframes = 5
        i = pyxel.frame_count % (nframes * len(image)) // nframes
        pyxel.blt(pos.x, pos.y, *image[i])
