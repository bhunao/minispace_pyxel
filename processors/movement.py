import pyxel
from esper import Processor
from components import Pos, Player, Movement, CircularMovement, Enemy, MoveToPlayer, Star, MoveXtoPlayer, CircileNearTarget
from math import cos, sin, radians, degrees, atan2, sqrt


class Move(Processor):
    def process(self):
        _, (player, _) = self.world.get_components(
            Pos, Player)[0]
        for _id, (pos, movement) in self.world.get_components(Pos, MoveToPlayer):
            self.move_to_target(pos, movement, target=player)
            self.move(pos, movement)

        for _id, (pos, movement) in self.world.get_components(Pos, Movement):
            self.move(pos, movement)

        for _id, (pos, movement) in self.world.get_components(Pos, CircularMovement):
            self.move_circular(pos, movement)

        for _id, (pos, movement) in self.world.get_components(Pos, MoveXtoPlayer):
            self.move_to_target(pos, movement, target=player)
            angle_rad = radians(movement.angle)
            pos.x += cos(angle_rad) * movement.speed
            pos.y += 1 if pos.y < 30 else 0

        for _id, (pos, movement) in self.world.get_components(Pos, CircileNearTarget):
            self.move_keep_distance(pos, movement, player)
            self.move(pos, movement)
            # dx = pos.x - player.x
            # dy = pos.y - player.y
            # angle = - degrees(atan2(dx, dy)) - 90
            # movement.angle = angle

        for _id, (pos, movement, _) in self.world.get_components(Pos, Movement, Star):
            mid = pyxel.width // 2
            diff = player.x - mid
            pos.x -= diff // 70

            if pos.y > pyxel.height + 15:
                pos.y = 0 - pyxel.frame_count % 25
                pos.x = pyxel.rndi(0, pyxel.width)

    @staticmethod
    def move_circular(pos, moviment):
        angle_rad = radians(moviment.angle + pyxel.frame_count * 10)
        pos.x += cos(angle_rad) * moviment.speed
        pos.y += sin(angle_rad) * moviment.speed

    @staticmethod
    def move(pos, moviment):
        angle_rad = radians(moviment.angle)
        pos.x += cos(angle_rad) * moviment.speed
        pos.y += sin(angle_rad) * moviment.speed

    def move_to_target(self, pos, moviment, target):
        dx = pos.x - target.x
        dy = pos.y - target.y
        angle = - degrees(atan2(dx, dy)) - 90
        moviment.angle = angle

    def move_away_from(self, pos, moviment, target):
        dx = pos.x - target.x
        dy = pos.y - target.y
        angle = degrees(pyxel.atan2(dx, dy)) - 90
        moviment.angle = angle

    def move_keep_distance(self, pos, movement, target):
        n1 = (pos.x - target.x)**2
        n2 = (pos.y - target.y)**2
        distance = sqrt(n1 + n2)
        print(distance)
        if distance > 50:
            self.move_to_target(pos, movement, target)
        elif distance < 100:
            self.move_away_from(pos, movement, target)
        else:
            self.move_circular(pos, movement)
