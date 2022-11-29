from utils import utils
from utils.constants import CINS, CDEL
import dynamique


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
        return mot_gaps(len(y)), y

    elif y == '':
        return x, mot_gaps(len(x))

    elif len(x) == 1:
        return align_lettre_mot(x, y)

    elif len(y) == 1:
        return align_lettre_mot(y, x)[::-1]

    else:
        i = len(x) // 2
        j = coupure(x, y)

        x1, y1 = SOL_2(x[:i], y[:j])
        x2, y2 = SOL_2(x[i:], y[j:])

        return (x1 + x2, y1 + y2)


def coupure(x, y):
    i = len(x) // 2
    k = i

    tab = dynamique.DIST_1(x, y)
    
    t2 = [list(range(len(y) + 1))] + [[0 for _ in range(len(y) + 1)] for _ in range(len(x) - i)]

    i += 1
    while i <= len(x):
        for j in range(len(y) + 1):
            if j == 0:
                t2[i - k][j] = t2[i - k - 1][j]

            elif (tab[i][j - 1] <= tab[i - 1][j]) and (tab[i][j - 1] <= tab[i - 1][j - 1]):
                t2[i - k][j] = t2[i - k][j - 1]

            elif (tab[i - 1][j] <= tab[i][j - 1]) and (tab[i - 1][j] <= tab[i - 1][j - 1]):
                t2[i - k][j] = t2[i - k - 1][j]

            else:
                t2[i - k][j] = t2[i - k - 1][j - 1]

        i += 1

    return t2[-1][-1]
