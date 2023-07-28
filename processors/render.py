import pyxel
from esper import Processor
from components import Text, Pos, Circle
from functions import rainbow


class Render(Processor):
    def process(self):
        text_comps = Text, Pos
        for _, (text, pos) in self.world.get_components(*text_comps):
            colkey = text.colkey if text.colkey <= 15 else rainbow()
            pyxel.text(pos.x, pos.y, text.text, colkey)

        circle_comps = Circle, Pos
        for _, (circle, pos) in self.world.get_components(*circle_comps):
            colkey = circle.colkey if circle.colkey <= 15 else rainbow()
            pyxel.circb(pos.x, pos.y, circle.r, colkey)
            if circle.f:
                circle.r += circle.f(pyxel.frame_count)
            else:
                circle.r += circle.r_inc
