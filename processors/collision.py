import pyxel
from esper import Processor
from components import Sprite, Pos, Player
from functions import get_player, myfunction


def collide(p1: Pos, s1: Sprite, p2: Pos, s2: Sprite):
    if p1.x > p2.x + s2.w or p2.x > p1.x + s1.w:
        return False
    if p1.y > p2.y + s2.h or p2.y > p1.y + s1.h:
        return False
    return True

collide_with = myfunction(collide)


class Collission(Processor):
    def process(self):
        p_id, (player, player_pos, player_sprite) = get_player(self.world)

        for components in self.world.get_components(Sprite, Pos):
            _id, (sprite, pos) = components
            print(_id)

            if p_id == _id:
                continue

            player_collision = (player_pos, player_sprite)
            comp_collission = (pos, sprite)
            if player_collision @ collide_with @ comp_collission:
                print(player_collision, comp_collission)
            else:
                print("========~PDOJASDJ")

