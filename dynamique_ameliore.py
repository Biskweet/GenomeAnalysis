from utils import utils
from utils.constants import CINS, CDEL


def DIST_2(x, y):
    tab = [[0 for _ in range(len(y) + 1)] for _ in range(2)]

    for i in range(1, len(x) + 1):
        for j in range(len(y) + 1):
            if i == 0:
                tab[i][j] = j * CINS

            elif j == 0:
                tab[i % 2][j] = i * CDEL


            else:
                if i % 2 == 0:
                    tab[0][j] = min(
                        tab[0][j - 1] + CINS,
                        tab[1][j] + CDEL,
                        tab[1][j - 1] + utils.csub(x[i-1], y[j-1])
                    )
                else:
                    tab[1][j] = min(
                        tab[1][j - 1] + CINS,
                        tab[0][j] + CDEL,
                        tab[0][j - 1] + utils.csub(x[i-1], y[j-1])
                    )

    return tab[1 - len(x) % 2], tab[len(x) % 2]
