from wdi import *

def init():
    for i in range(n):
        b[i] = -1

def poprawne(a, n):
    for i in range(n):
        for j in range(i + 1, n):
            # Sprawdzenie wierszy
            if a[i] == a[j]:
                return 0
            # Sprawdzenie przekątnych
            if (a[i] - a[j]) == (i - j) or (a[j] - a[i]) == (j - i):
                return 0
    return 1

def hetmany(n, k, a):
    if k == n:
        return poprawne(a, n)
    for i in range(n):
        a[k] = i
        if hetmany(n, k + 1, a):
            return 1
    return 0

n = 4
b = Array(n)
init()
print(hetmany(n, 0, b))