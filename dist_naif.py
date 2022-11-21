import math
import os
import sys
import time

# Custom imports
from utils.constants import CINS, CDEL, DIRECTORY
from utils import utils


# Changing recursion depth to the max depth possible
sys.setrecursionlimit(100000)


def dist_naif(x, y):
    return dist_naif_rec(x, y, 0, 0, 0, math.inf)


def dist_naif_rec(x, y, i, j, c, dist):
    if i == len(x) and j == len(y):
        if c < dist:
            return c

    else:
        if i < len(x) and j < len(y):
            a, b = x[i], y[j]
            csub = (a != b) * (3 * (a in ('A', 'T') and b in ('A', 'T') or a in ('G', 'C') and b in ('G', 'C')) or 4)

            dist = dist_naif_rec(x, y, i+1, j+1, c + csub, dist)

        if i < len(x):
            dist = dist_naif_rec(x, y, i+1, j, c + CDEL, dist)
 
        if j < len(y):
            dist = dist_naif_rec(x, y, i, j+1, c + CINS, dist)

    return dist


if __name__ == "__main__":
    filename = utils.get_file_name()

    x, y = utils.parse_file(os.path.join(DIRECTORY, filename))

    t1 = time.time()
    dist = dist_naif(x, y)
    t2 = time.time()

    print(f"Dist(x, y) = {dist} (in {t2 - t1:.3f} seconds).")
