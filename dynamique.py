from utils import utils
from utils.constants import CINS, CDEL


def PROG_DYN(x, y):
    tab = DIST_1(x, y)
    xbar, ybar = SOL_1(x, y, tab)
    return xbar, ybar, tab[-1][-1]


def DIST_1(x, y):
    tab = [[0 for _ in range(len(y) + 1)] for _ in range(len(x) + 1)]
    
    for i in range(len(x) + 1):
        for j in range(len(y) + 1):
            # Remplissage de la 1ere ligne
            if i == 0:
                tab[i][j] = j * CINS

            # Remplissage de la 1ere colonne
            elif j == 0:
                tab[i][j] = i * CDEL
 
            else:
                tab[i][j] = min(
                    tab[i][j - 1] + CINS,
                    tab[i - 1][j] + CDEL,
                    tab[i - 1][j - 1] + utils.csub(x[i-1], y[j-1])
                )  # min() pour garder le coût le plus intéressant

    return tab  # On renvoie le tableau des coûts


def SOL_1(x, y, tab):
    xbar, ybar = '', ''
    i, j = len(x), len(y)

    while i > 0 and j > 0:
        if (tab[i][j - 1] <= tab[i - 1][j]) and (tab[i][j - 1] <= tab[i - 1][j - 1]):
            xbar = '-' + xbar
            ybar = y[j - 1] + ybar
            j -= 1

        elif (tab[i - 1][j] <= tab[i][j - 1]) and (tab[i - 1][j] <= tab[i - 1][j - 1]):
            xbar = x[i - 1] + xbar
            ybar = '-' + ybar
            i -= 1

        else:
            xbar = x[i - 1] + xbar
            ybar = y[j - 1] + ybar
            i -= 1
            j -= 1

    while i > 0:
        xbar = x[i - 1] + xbar
        ybar = '-' + ybar
        i -= 1

    while j > 0:
        xbar = '-' + xbar
        ybar = y[j - 1] + ybar
        j -= 1

    return xbar, ybar
