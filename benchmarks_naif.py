import os
import time

import naif
from utils.constants import DIRECTORY
from utils import utils

if __name__ == "__main__":
    t1 = t2 = i = 0
    x, y = '', ''

    instances = sorted(os.listdir(DIRECTORY))

    while t2 - t1 < 60:
        x, y = utils.parse_file(os.path.join(DIRECTORY, instances[i]))

        t1 = time.time()
        naif.dist_naif(x, y)
        t2 = time.time()

        print(f"Instance size = {(len(x), len(y))} : {t2 - t1:.3f} seconds.")

        i += 1

    print("-----")
    print("Exceeded 60 seconds with instance size =", (len(x), len(y)))
