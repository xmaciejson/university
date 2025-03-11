
from wdi import *


class ListItem:
    def __init__(self, value):
        self.val = value
        self.next = None


def usunMax(lista):
    if lista is None:
        return None

    max_val = lista.val
    current = lista
    while current is not None:
        if current.val > max_val:
            max_val = current.val
        current = current.next

    if max_val == lista.val:
        return 1

    current = lista
    while current is not None and current.next is not None:
        if current.next.val == max_val:
            if current.next.next is None:
                return 1
            current.next = current.next.next

        current = current.next

    return 0


def pr(i, j, a):
    if i == j: return True
    s = (i + j) // 2
    if a[s] > a[s + 1]:
        return False
    p1 = pr(i, s, a)
    p2 = pr(s + 1, j, a)
    return p1 and p2


def prt(n, a):
    return pr(0, n - 1, a)


def usuwaj(lista):
    while lista is not None and lista.val % 2 == 0:
        lista = lista.next

    current = lista
    while current is not None and current.next is not None:
        if current.next.val % 2 == 0:
            current.next.val = current.next.next
        current = current.next

    return lista


def monoton(lista):
    if lista is None:
        return 0

    current = lista
    while current is not None and current.next is not None:
        if current.next.val < current.val:
            return 0
        current = current.next
    return 1


l1 = ListItem(4)
l1.next = ListItem(4)
l1.next.next = ListItem(4)
l1.next.next.next = ListItem(4)

tab = Array(10)
for i in range(10):
    tab[i] = i


def suma_kwadratow(n):
    tab = Array(n)
    for i in range(n):
        tab[i] = False

    for i in range(1, n):
        for j in range(1, n):
            suma = i * i + j * j
            if suma < n:
                tab[suma] = suma
            else:
                break

    for i in range(n):
        if tab[i] is not False:
            print(tab[i])

    return


def wylicz(n, m):
    if m == 0: return n
    if n == 0: return m
    if (n % 2 == 0):
        k = n // 2
    else:
        k = (n + 1) // 2
    return wylicz(k, m - 1) + wylicz(n - 1, 1) + 1


def usunOstPar(lista):
    if lista.val % 2 == 0 and lista.next is None:
        return None

    ostatnia = 0
    current = lista
    while current is not None: #szukamy ostatniej parzystej
        if current.val % 2 == 0:
            ostatnia = current.val
        current = current.next

    current = lista
    while current is not None and current.next is not None: #usuwamy ostatnia parzysta
        if current.next.val == ostatnia:
            current.next = current.next.next
        current = current.next


    return lista

def parzyste(lista):
    if lista is None:
        return 0

    suma = 0
    current = lista
    while current is not None:
        if current.val % 2 == 0:
            suma += current.val
        current = current.next

    return suma


