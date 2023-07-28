import pyxel
from esper import Processor
from components import (Enemy, MoveF, MoveToEnemy, Pos, Player, Movement, CircularMovement,
                        MoveToPlayer, Star, MoveXtoPlayer, CircileNearTarget,
                        Sprite, Projectile)
from math import cos, sin, radians, degrees, atan2, sqrt
from functions import center_of, distance_between


class Move(Processor):
    def process(self):
        _, (player, p_sprite, _) = self.world.get_components(
            Pos, Sprite, Player)[0]
        player = Pos(*center_of(p_sprite, player))
        for _, components in self.get_components(Pos, MoveToPlayer, Sprite):
            pos, movement, sprite = components
            self.move_to_target(pos, movement, sprite, target=player)
            self.move(pos, movement)

        for _, components in self.get_components(Pos, MoveToEnemy, Sprite):
            pos, movement, sprite = components

            enemy = self.world.get_components(Pos, Sprite, Enemy)

            if enemy:
                eposs = [epos for _, (epos, esprite, _) in enemy]
                target = min(eposs, key=lambda x: distance_between(x, pos))
                self.move_to_target(pos, movement, sprite, target=target)
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

    @staticmethod
    def f(pos, movement):
        if movement.f:
            angle_rad = radians(movement.angle)
            f_val = movement.f(movement.step)
            print(f_val)
            pos.x += cos(angle_rad) * f_val * movement.speed
            pos.y += sin(angle_rad) * f_val * movement.speed
            movement.step += 1

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
        distance = distance_between(pos, target)
        if distance > 50:
            self.move_to_target(pos, movement, sprite, target)
        elif distance < 100:
            self.move_away_from(pos, movement, target)
        else:
            self.move_circular(pos, movement)
