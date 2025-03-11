from os.path import split

from wdi import *

r = 4
tab = Array(r, r)
wiersze = Array(r)

for i in range(r):
    wiersze[i] = -1
    for j in range(r):
        tab[i][j] = int(input())


def is_safe(wiersz, kolumna, wier):
    for i in range(kolumna - 1):
        if wier[i] == wiersz:
            return False
    return True


def monety(n, s, a, col=0, koszt=0):
    if col == n:
        return koszt <= s

    for row in range(n):
        if is_safe(row, col, wiersze):
            wiersze[col] = row
            if monety(n, s, a, col + 1, koszt + a[row][col]):
                return True
    return False

print(monety(4, 40, tab))