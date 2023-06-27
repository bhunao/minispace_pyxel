import pyxel
from typing import Dict
from entities import Player, Enemy, Projectile


class Game:
    def __init__(self):
        pyxel.init(180, 140)
        pyxel.load('assets.pyxres')
        self.start()
        pyxel.run(self.update, self.draw)

    def start(self):
        self.entities: Dict[type, list] = {}
        self.add_entity(
            Player(x=50, y=50),
            Enemy(speed=1, angle=45)
        )

    def add_entity(self, *entities):
        for entity in entities:
            if not self.entities.get(type(entity)):
                self.entities[type(entity)] = []
            self.entities[type(entity)].append(entity)

    def remove_entity(self, *entities):
        for entity in entities:
            self.entities[type(entity)].remove(entity)

    def controller(self):
        player: Player = self.entities[Player][0]
        if pyxel.btn(pyxel.KEY_LEFT):
            player.x -= 1
        if pyxel.btn(pyxel.KEY_RIGHT):
            player.x += 1
        if pyxel.btn(pyxel.KEY_DOWN):
            player.y += 1
        if pyxel.btn(pyxel.KEY_UP):
            player.y -= 1
        if pyxel.btnp(pyxel.KEY_SPACE):
            self.add_entity(
                Projectile(x=player.x, y=player.y, angle=-
                           90, speed=3, origin=type(player))
            )

    def update(self):
        self.controller()

        for entity_list in self.entities.values():
            for entity in entity_list:
                entity.move()

                match entity:
                    case Projectile():
                        for other in self.entities[Enemy]:
                            if entity.collide_with_target(other):
                                self.remove_entity(entity)
                                other.hp -= 1
                                if other.hp <= 0:
                                    self.remove_entity(other)
                        for other in self.entities[Player]:
                            if entity.collide_with_target(other):
                                self.remove_entity(entity)
                                if other.hp <= 0:
                                    self.remove_entity(other)

    def draw(self):
        pyxel.cls(0)
        for entity_list in self.entities.values():
            for entity in entity_list:
                entity.render()


Game()
