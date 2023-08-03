from entities import (bartolomeo, cabesakura, rodoaldo, slow_shooter,
                      rotationer_gunner, rotational_boss, slow_walker, sorriso_ronaldo, spinning_jack, spiral_daniel, ronnie_wall)

waves = [
    *[
        [cabesakura, (), 1, 100]
        for _ in range(5)
    ],
    [cabesakura, (1, -8), 1, -1],
    # ================== wave 01
    [slow_walker, (61, -16), 1, 0],
    [slow_walker, (106, -8), 1, 0],
    [slow_walker, (151, -16), 1, -1],
    # ===
    [slow_walker, (121, -16), 1, 0],
    [slow_shooter, (166, -8), 1, 0],
    [slow_walker, (211, -16), 1, -1],
    # ===
    [slow_walker, (11, -16), 1, 0],
    [slow_shooter, (56, -8), 1, 0],
    [slow_walker, (101, -16), 1, -1],
    # ===
    [slow_walker, (121, -16), 1, 0],
    [spinning_jack, (166, -8), 1, 0],
    [slow_walker, (211, -16), 1, -1],
    # ===
    [slow_walker, (11, -16), 1, 0],
    [spinning_jack, (56, -8), 1, 0],
    [slow_walker, (101, -16), 1, -1],
    # ===
    [spinning_jack, (61, -16), 1, 0],
    [slow_walker, (106, -8), 1, 0],
    [spinning_jack, (151, -16), 1, -1],
    # ===
    [spinning_jack, (61, -16), 1, 0],
    [slow_walker, (106, -8), 1, 0],
    [spinning_jack, (151, -16), 1, -1],
    # ================== wave 02
    [slow_shooter, (151, -16), 1, 0],
    [rodoaldo, (), 2, -1],
    # ================== wave 03
    [spinning_jack, (60, -16), 1, 0],
    [spinning_jack, (160, -16), 1, -1],
    # ================== 04
    [spiral_daniel, (12, -16), 1, 0],
    [spiral_daniel, (192, -16), 1, 0],
    [spiral_daniel, (57, -80), 1, 0],
    [spiral_daniel, (147, -80), 1, -1],
    # ================== wave ??
    [slow_walker, (30, -16), 1, 0],
    [slow_walker, (60, -24), 1, 0],
    [slow_walker, (90, -32), 1, 0],
    [slow_walker, (120, -32), 1, 0],
    [slow_walker, (150, -24), 1, 0],
    [slow_walker, (180, -16), 1, 0],
    # ===
    [slow_walker, (30, -48), 1, 0],
    [slow_walker, (60, -56), 1, 0],
    [slow_walker, (90, -64), 1, 0],
    [slow_walker, (120, -64), 1, 0],
    [slow_walker, (150, -56), 1, 0],
    [slow_walker, (180, -48), 1, 0],
    # ===
    [slow_walker, (30, -80), 1, 0],
    [rotationer_gunner, (60, -88), 1, 0],
    [slow_walker, (90, -96), 1, 0],
    [slow_walker, (120, -96), 1, 0],
    [rotationer_gunner, (150, -88), 1, 0],
    [slow_walker, (180, -80), 1, -1],
    # ================== wave ??
    [rotational_boss, (50,), 1, -1],
    # ================== wave ??
    *[
        [slow_walker, (), 1, 30]
        for _ in range(10)
    ],
    [rotationer_gunner, (102, 0), 1, 0],
    *[
        [slow_walker, (), 1, 30]
        for _ in range(9)
    ],
    [slow_walker, (), 1, -1],
    # ================== wave ??
    [rodoaldo, (), 1, 50],
    [rodoaldo, (), 1, 50],
    [rodoaldo, (), 1, 50],
    [rodoaldo, (), 1, 50],
    [rodoaldo, (), 1, 50],
    [rodoaldo, (), 1, 50],
    [rodoaldo, (), 1, 50],
    [rodoaldo, (), 1, -1],
    # ================== wave ?? WALL
    *[
        [ronnie_wall, (x, -10), 1, 0]
        for x in range(-2, 222, 7)
    ],
    [ronnie_wall, (110, -10), 1, -1],
    # ================== wave ??
    [slow_shooter, (), 2, 0],
    [spinning_jack, (), 5, -1],
    # ================== wave ??
    [bartolomeo, (36, -48), 1, 0],
    [bartolomeo, (102, -56), 1, 0],
    [bartolomeo, (168, -48), 1, -1],
    # ================== wave ??
    *[
        [sorriso_ronaldo, (16, -8), 1, 25]
        for _ in range(25)
    ],
    [sorriso_ronaldo, (1, -8), 1, -1],
    # ================== wave ?? SECOND WALL
    *[
        [spiral_daniel, (x-8, -8), 1, 0]
        for x in range(-50, 272, 48)
    ],
    *[
        [spiral_daniel, (x+16, -40), 1, 0]
        for x in range(-50, 272, 48)
    ],
    *[
        [spiral_daniel, (x, -72), 1, 0]
        for x in range(-50, 272, 48)
    ],
    *[
        [spiral_daniel, (x+32, -104), 1, 0]
        for x in range(-50, 272, 48)
    ],
    *[
        [spiral_daniel, (x, -136), 1, 0]
        for x in range(-50, 272, 48)
    ],
    [spiral_daniel, (110-8, -168), 1, -1],
    # ================== wave ??
]
