import os
import sys
import time

import naif
from utils.constants import DIRECTORY
from utils import utils

if __name__ == "__main__":
    # Changing recursion depth to the max depth possible
    sys.setrecursionlimit(100000)

    t1 = t2 = i = 0
    x, y = '', ''
    benchmarks = []

    instances = sorted(os.listdir(DIRECTORY))

    while t2 - t1 < 60:
        x, y = utils.parse_file(os.path.join(DIRECTORY, instances[i]))

        t1 = time.time()
        naif.dist_naif(x, y)
        t2 = time.time()

        print(f"Instance size = {(len(x), len(y))} : {t2 - t1:.5f} seconds.")

        i += 1

        benchmarks.append(f"{max(len(x), len(y))} {t2 - t1}")

    print("-----")
    print("Exceeded 60 seconds with instance size =", (len(x), len(y)))

    with open("benchmarks/benchmarks_naif_results.txt", "w") as file:
        file.write('\n'.join(benchmarks))
