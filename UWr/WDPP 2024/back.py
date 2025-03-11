from wdi import *


def is_safe(tab, w, n):
    for j in range(n):
        if tab[j] == w:
            return False
    return True


def pionki(n, k, Z, rozm=[], kol=0, wier=[], count=0):
    if count == k:
        return rozm
    if kol == n:
        return 0

    for i in range(n):
        if is_safe(wier, i, n) and Z[kol][i] == 0:
            wier[i] = i
            if pionki(n, k, Z, rozm + [(kol, i)], kol + 1, wier, count + 1):
                return True
    return False


def balans(root):
    if root is None:
        return 0

            
