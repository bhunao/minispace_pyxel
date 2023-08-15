import sprites, components, pyxel


rotational_boss = [
    components.Sprite(sprites.E4),
    components.Pos(50, 50),
    components.Speed(.2, f_angle=lambda: pyxel.frame_count % 10),
]
