import os
import sys
import time

from utils import utils
from utils.constants import DIRECTORY

import dynamique as dyn
import diviser_pour_regner as diviser


if __name__ == "__main__":
    # Changing recursion depth to the max depth possible
    sys.setrecursionlimit(100000)

    benchmarks = []

    t1 = t2 = t3 = t4 = t5 = i = 0
    x, y = '', ''

    instances = sorted(os.listdir(DIRECTORY))

    while t2 - t1 < 600 and i < len(instances):
        x, y = utils.parse_file(os.path.join(DIRECTORY, instances[i]))

        t1 = time.time()
        tab = dyn.DIST_1(x, y)
        t2 = time.time()
        dyn.SOL_1(x, y, tab)
        t3 = time.time()

        print(f"Instance {i+1}/58 with shape = ({len(x)}, {len(y)}):")
        print(f"    SOL_1: {t3 - t1:.5f} seconds (without DIST_1: {t3 - t2:.5f} s.)")

        t4 = time.time()
        diviser.SOL_2(x, y)
        t5 = time.time()

        print(f"    SOL_2: {t5 - t4:.5f} seconds.\n")
        
        benchmarks.append(f"{max(len(x), len(y))} {t3 - t2} {t3 - t1} {t5 - t4}")

        i += 1

    with open("benchmarks/benchmarks_SOL_results.txt", "w") as file:
        file.write('\n'.join(benchmarks))
