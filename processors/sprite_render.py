import pyxel
from esper import Processor
from components import Sprite, Pos, Speed
from math import cos, sin, radians


class SpriteRender(Processor):
    def process(self):
        for components in self.world.get_components(Sprite, Pos):
            _, (sprite, pos) = components
            frames = 5
            i = pyxel.frame_count % (frames * len(sprite.sprite)) // frames
            pyxel.blt(pos.x, pos.y, *sprite.sprite[i])


class Movement(Processor):
    def process(self):
        for components in self.world.get_components(Pos, Speed):
            _, (pos, speed) = components
            angle = radians(speed.angle)
            speed_val = speed.f_speed()
            pos.x += cos(angle) * speed_val
            pos.y += sin(angle) * speed_val
            speed.angle += speed.f_angle()
