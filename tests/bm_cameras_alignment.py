# Copyright (c) Facebook, Inc. and its affiliates. All rights reserved.

import itertools
from fvcore.common.benchmark import benchmark
from test_cameras_alignment import TestCamerasAlignment


def bm_cameras_alignment() -> None:

    case_grid = {
        "batch_size": [10, 100, 1000],
        "mode": ["centers", "extrinsics"],
        "estimate_scale": [False, True],
    }
    test_cases = itertools.product(*case_grid.values())
    kwargs_list = [dict(zip(case_grid.keys(), case)) for case in test_cases]

    benchmark(
        TestCamerasAlignment.corresponding_cameras_alignment,
        "CORRESPONDING_CAMERAS_ALIGNMENT",
        kwargs_list,
        warmup_iters=1,
    )
