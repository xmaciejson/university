from math import log10, floor
# ZAD 2
def silnia(n):
    wynik = 1
    for i in range(1, n + 1):
        wynik *= i

    return wynik

for i in range(4, 101):
    print(f'{i}! ma {len(str(silnia(i)))} cyfry')


# ZAD 2 ALTERNATYWA


# ZAD 3
def krzyzyk(n):

    for i in range(n):
        print(' ' * n + '*' * n + ' ' * n)

    for i in range(n):
        print(3 * ('*' * n))

    for i in range(n):
        print(' ' * n + '*' * n + ' ' * n)

    return ''

print(krzyzyk(10))

# ZAD 4
from losowanie_fragmentow import losuj_fragment


def losuj_haslo(n):
    haslo = ''
    while len(haslo) != n:
        if len(haslo) > n:
            haslo = ''

        else:
            haslo += losuj_fragment()

    return haslo


for i in range(10):
    print(losuj_haslo(8))

for i in range(10):
    print(losuj_haslo(12))



