from entities import (bartolomeo, rodoaldo, slow_shooter, enemy2, enemy3, enemy4,
                      rotationer_gunner, rotational_boss, slow_walker, spinning_jack, spiral_daniel, ronnie_wall)

waves = [
    * [
        [spiral_daniel, (x-8, -8), 1, True]
        for x in range(-50, 272, 48)
    ],
    *[
        [spiral_daniel, (x+16, -40), 1, True]
        for x in range(-50, 272, 48)
    ],
    *[
        [spiral_daniel, (x, -72), 1, True]
        for x in range(-50, 272, 48)
    ],
    *[
        [spiral_daniel, (x+16, -104), 1, True]
        for x in range(-50, 272, 48)
    ],
    *[
        [spiral_daniel, (x, -136), 1, True]
        for x in range(-50, 272, 48)
    ],
    [spiral_daniel, (110-8, -168), 1, False],
    # ================== wave 01
    [slow_walker, (61, -16), 1, True],
    [slow_walker, (106, -8), 1, True],
    [slow_walker, (151, -16), 1, False],
    # ===
    [slow_walker, (121, -16), 1, True],
    [slow_shooter, (166, -8), 1, True],
    [slow_walker, (211, -16), 1, False],
    # ===
    [slow_walker, (11, -16), 1, True],
    [slow_shooter, (56, -8), 1, True],
    [slow_walker, (101, -16), 1, False],
    # ===
    [slow_walker, (121, -16), 1, True],
    [spinning_jack, (166, -8), 1, True],
    [slow_walker, (211, -16), 1, False],
    # ===
    [slow_walker, (11, -16), 1, True],
    [spinning_jack, (56, -8), 1, True],
    [slow_walker, (101, -16), 1, False],
    # ===
    [spinning_jack, (61, -16), 1, True],
    [slow_walker, (106, -8), 1, True],
    [spinning_jack, (151, -16), 1, False],
    # ===
    [spinning_jack, (61, -16), 1, True],
    [slow_walker, (106, -8), 1, True],
    [spinning_jack, (151, -16), 1, False],
    # ================== wave 02
    [slow_shooter, (151, -16), 1, True],
    [rodoaldo, (), 2, False],
    # ================== wave 03
    [spinning_jack, (60, -16), 1, True],
    [spinning_jack, (160, -16), 1, False],
    # ================== 04
    [spiral_daniel, (12, -16), 1, True],
    [spiral_daniel, (192, -16), 1, True],
    [spiral_daniel, (57, -80), 1, True],
    [spiral_daniel, (147, -80), 1, False],
    # ================== wave ??
    [slow_walker, (30, -16), 1, True],
    [slow_walker, (60, -24), 1, True],
    [slow_walker, (90, -32), 1, True],
    [slow_walker, (120, -32), 1, True],
    [slow_walker, (150, -24), 1, True],
    [slow_walker, (180, -16), 1, True],
    # ===
    [slow_walker, (30, -48), 1, True],
    [slow_walker, (60, -56), 1, True],
    [slow_walker, (90, -64), 1, True],
    [slow_walker, (120, -64), 1, True],
    [slow_walker, (150, -56), 1, True],
    [slow_walker, (180, -48), 1, True],
    # ===
    [slow_walker, (30, -80), 1, True],
    [rotationer_gunner, (60, -88), 1, True],
    [slow_walker, (90, -96), 1, True],
    [slow_walker, (120, -96), 1, True],
    [rotationer_gunner, (150, -88), 1, True],
    [slow_walker, (180, -80), 1, False],
    # ================== wave ??
    [rotational_boss, (50,), 1, False],
    # ================== wave ??
    [rotationer_gunner, (50,), 1, True],
    [rotationer_gunner, (160,), 1, False],
    # ================== wave ?? WALL
    *[
        [ronnie_wall, (x, -10), 1, True]
        for x in range(-2, 222, 7)
    ],
    [ronnie_wall, (110, -10), 1, False],
    # ================== wave ??
    [slow_shooter, (), 2, True],
    [enemy2, (), 1, True],
    [enemy3, (), 2, False],
    [enemy4, (), 1, False],
    [spiral_daniel, (), 50, False],
    # ================== wave ??
    [bartolomeo, (36, -48), 1, True],
    [bartolomeo, (102, -56), 1, True],
    [bartolomeo, (168, -48), 1, False],
    # ================== wave ?? SECOND WALL
    # ================== wave ??
    [rotational_boss, (-50,), 1, True],
]
