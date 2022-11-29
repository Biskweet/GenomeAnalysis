import os
import sys
import time

import dynamique as dyn
from utils.constants import DIRECTORY
from utils import utils

if __name__ == "__main__":
    # Changing recursion depth to the max depth possible
    sys.setrecursionlimit(100000)

    t1 = t2 = i = 0
    x, y = '', ''
    benchmarks = []

    instances = sorted(os.listdir(DIRECTORY))

    while t2 - t1 < 600 and i < len(instances):
        x, y = utils.parse_file(os.path.join(DIRECTORY, instances[i]))

        t1 = time.time()
        dyn.PROG_DYN(x, y)
        t2 = time.time()

        print(f"{i+1}/58 instance size = {(len(x), len(y))} : {t2 - t1:.5f} seconds.")

        i += 1

        benchmarks.append(f"{len(x)} {t2 - t1}")

    if t2 - t1 >= 600:
        print("-----")
        print("Exceeded 10 min with instance size =", (len(x), len(y)))
    else:
        print("End of tests.")

    with open("benchmarks/benchmarks_DIST_results.txt", "w") as file:
        file.write('\n'.join(benchmarks))
