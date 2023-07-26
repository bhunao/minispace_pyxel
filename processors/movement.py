import pyxel
from esper import Processor
from components import (MoveF, Pos, Player, Movement, CircularMovement,
                        MoveToPlayer, Star, MoveXtoPlayer, CircileNearTarget,
                        Sprite, Projectile)
from math import cos, sin, radians, degrees, atan2, sqrt
from functions import center_of


class Move(Processor):
    def process(self):
        _, (player, p_sprite, _) = self.world.get_components(
            Pos, Sprite, Player)[0]
        player = Pos(*center_of(p_sprite, player))
        for _, components in self.get_components(Pos, MoveToPlayer, Sprite):
            pos, movement, sprite = components
            self.move_to_target(pos, movement, sprite, target=player)
            self.move(pos, movement)

        for _, components in self.get_components(Pos, Movement):
            pos, movement = components
            self.move(pos, movement)

        for _, components in self.get_components(Pos, CircularMovement):
            pos, movement = components
            self.move_circular(pos, movement)

        for _, components in self.get_components(Pos, MoveXtoPlayer, Sprite):
            pos, movement, sprite = components
            self.move_to_target(pos, movement, sprite, target=player)
            angle_rad = radians(movement.angle)
            pos.x += cos(angle_rad) * movement.speed
            pos.y += 1 if pos.y < 30 else 0

        for _, components in self.get_components(Pos, CircileNearTarget, Sprite):
            pos, movement, sprite = components
            self.move_keep_distance(pos, movement, sprite, player)
            self.move(pos, movement)

        for _, components in self.get_components(Pos, MoveF, Sprite):
            pos, movement, sprite = components
            self.f(pos, movement)

        for _, (pos, movement, _) in self.get_components(Pos, Movement, Star):
            mid = pyxel.width // 2
            diff = player.x - mid
            pos.x -= diff // 70

            if pos.y > pyxel.height + 15:
                pos.y = 0 - pyxel.frame_count % 25
                pos.x = pyxel.rndi(0, pyxel.width)

        for id, components in self.get_components(Projectile, Pos):
            _, pos = components
            if int(pos.y) not in range(0, pyxel.height):
                self.world.delete_entity(id)

    @staticmethod
    def f(pos, movement, n1=3, n2=2):
        x = movement.step
        movement.step += 1
        z = x - 20
        y = (n1 / n2 * z ** 2)*.05 - 10
        angle_rad = radians(movement.angle)
        pos.x += y / 5
        pos.y += sin(angle_rad)
        print(y)

    @staticmethod
    def move_circular(pos, movement):
        angle_rad = radians(
            movement.angle + pyxel.frame_count * movement.radius)
        pos.x += cos(angle_rad) * movement.speed
        pos.y += sin(angle_rad) * movement.speed

    @staticmethod
    def move(pos, moviment):
        angle_rad = radians(moviment.angle)
        pos.x += cos(angle_rad) * moviment.speed
        pos.y += sin(angle_rad) * moviment.speed

    def move_to_target(self, pos, moviment, sprite, target):
        x, y = center_of(sprite, pos)
        dx = x - target.x
        dy = y - target.y
        angle = - degrees(atan2(dx, dy)) - 90
        moviment.angle = angle

    def move_away_from(self, pos, moviment, target):
        dx = pos.x - target.x
        dy = pos.y - target.y
        angle = degrees(pyxel.atan2(dx, dy)) - 90
        moviment.angle = angle

    def move_keep_distance(self, pos, movement, sprite, target):
        n1 = (pos.x - target.x)**2
        n2 = (pos.y - target.y)**2
        distance = sqrt(n1 + n2)
        if distance > 50:
            self.move_to_target(pos, movement, sprite, target)
        elif distance < 100:
            self.move_away_from(pos, movement, target)
        else:
            self.move_circular(pos, movement)
