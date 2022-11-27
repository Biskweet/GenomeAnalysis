from utils import utils
from utils.constants import CINS, CDEL


def mot_gaps(k):
    return '-' * k


def align_lettre_mot(x, y):
    xbar, ybar = '', ''
    place = False

    for j in range(len(y)):
        if (x == y[j] or utils.csub(x, y[j]) < CINS + CDEL) and not place:
            xbar += x
            place = True

        else:
            xbar += '-'

        ybar += y[j]

    if not place:
        xbar += x
        ybar += '-'

    return xbar, ybar


def SOL_2(x, y):
    if x == '':
        return '-' * len(y)

    elif y == '':
        return '-' * len(x)

    elif len(x) == 1:
        return align_lettre_mot(x, y)

    elif len(y) == 1:
        return align_lettre_mot(y, x)

    else:
        i = len(x) // 2
        j = coupure(x, y)

        x1, y1 = SOL_2(x[:i+1], y[:j+1])
        x2, y2 = SOL_2(x[i+1:], y[j+1:])

        return (x1 + x2, y1 + y2)


def DIST_2(x, y):
    tab = [[0 for _ in range(len(y))]for _ in range(2)]

    for j in range(len(y)):
        tab[0][j] = j * CINS


    for i in range(1, len(x)):
        for j in range(len(y)):
            iprime = i % 2

            if j == 0:
                tab[iprime][j] = i * CDEL

            else:
                tab[iprime][j] = min(
                    tab[iprime][j - 1] + CINS,
                    tab[iprime - 1][j] + CDEL,
                    tab[iprime - 1][j - 1] + utils.csub(x[i], y[j])
                )


# "ACAGTA", "AGTCA"