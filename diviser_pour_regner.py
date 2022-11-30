from utils import utils
from utils.constants import CINS, CDEL
import dynamique_ameliore as dynam


def mot_gaps(k):
    return '-' * k


def align_lettre_mot(x, y):
    xbar, ybar = '', ''
    place = False

    # Checking first if x is in y
    for j in range(len(y)):
        if x == y[j]:
            return mot_gaps(j) + x + mot_gaps(len(y) - j - 1), y

    for j in range(len(y)):
        if utils.csub(x, y[j]) < CINS + CDEL and not place:
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


def coupure(x,y):
    i = len(x) // 2
    
    tab = [dynam.DIST_2(x[:i + (i == 0)],y)[0], [0 for _ in range(len(y) + 1)]]
    t2 = [[0 for _ in range(len(y) + 1)] for _ in range(2)]

    while i <= len(x):
        for j in range(len(y) + 1):
            if j == 0:
                tab[1][j] = i * CDEL
                continue

            insertion = tab[1][j-1] + CINS
            suppression = tab[0][j] + CDEL
            substitution = tab[0][j-1] + utils.csub(x[i-1], y[j-1])

            if i == len(x) // 2:
                t2[1][j] = j

            elif insertion <= suppression and insertion <= substitution:
                t2[1][j] = t2[1][j - 1]

            elif suppression <= insertion and suppression <= substitution:
                t2[1][j] = t2[0][j]

            else:
                t2[1][j] = t2[0][j - 1]

            # Travail de DIST_2
            tab[1][j] = min(
                insertion,
                suppression,
                substitution
            )

        i += 1
        tab = tab[1], tab[0]
        t2 = t2[1], t2[1]

    return t2[-1][-1]
