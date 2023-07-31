from entities import (rodoaldo, slow_shooter, enemy2, enemy3, enemy4, rotationer_gunner,
                      rotational_boss, slow_walker, spinning_jack,
                      spiral_daniel, thing)


waves = [
    [rodoaldo, (110, 5), 1, True],
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
    [slow_shooter, (151, -16), 1, False],
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
    # ================== wave ??
    [slow_shooter, (90,), 1, False],
    [slow_shooter, (), 3, False],
    [slow_shooter, (), 2, True],
    [enemy2, (), 1, True],
    [slow_shooter, (), 10, False],
    [enemy3, (), 2, False],
    [slow_shooter, (), 10, False],
    [slow_shooter, (), 5, False],
    [slow_shooter, (), 10, False],
    [slow_shooter, (), 15, False],
    [enemy3, (), 5, False],
    [slow_shooter, (), 13, False],
    [slow_shooter, (), 8, False],
    [slow_shooter, (), 13, False],
    [slow_shooter, (), 18, False],
    [enemy4, (), 1, False],
    [spiral_daniel, (), 50, False],
    [spinning_jack, (), 50, False],
    [spiral_daniel, (), 50, False],
    [spinning_jack, (), 50, False],
    [spiral_daniel, (), 50, False],
    [spinning_jack, (), 50, False],
    [spiral_daniel, (), 50, False],
    [spinning_jack, (), 50, False],
    [spiral_daniel, (), 50, False],
    [spinning_jack, (), 50, False],
    [spiral_daniel, (), 50, False],
    [spinning_jack, (), 50, False],
    # ================== wave ??
    [rotational_boss, (-50,), 1, True],
    [thing, (), 10, False],
]
