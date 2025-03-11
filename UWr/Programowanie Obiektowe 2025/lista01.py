#ZAD1------------------------------------------
def silnia_imperatywnie(n):
    wynik = 1
    for i in range(1, n + 1):
        wynik *= i

    return wynik


def silnia_funkcyjnie(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * silnia_imperatywnie(n - 1)


def binom(n, k):
    return silnia_funkcyjnie(n) // (silnia_funkcyjnie(k) * silnia_funkcyjnie(n - k))


def wypisz_trojkat(n):
    print(' '.join((str(binom(n, k)) for k in range(n + 1))))

wiersz = int(input('Podaj wiersz: '))
print("ZAD 1")
wypisz_trojkat(wiersz)
#ZAD1------------------------------------------

#ZAD2------------------------------------------
print("ZAD 2")
def wzglednie_imperatywnie(a ,b):
    while b:
        a, b = b, a % b
    return a

def wzglednie_funkcyjnie(a, b):
    return a if b == 0 else wzglednie_funkcyjnie(b, a % b)

def wypisz_imperatywnie(n):
    return [i for i in range(1, n + 1) if wzglednie_funkcyjnie(i, n) == 1]

def wypisz_funkcyjnie(n, k=1):
    if k == n:
        return ''
    else:
        if wzglednie_funkcyjnie(n, k) == 1:
            print(k)
            return wypisz_funkcyjnie(n, k + 1)
        else:
            return wypisz_funkcyjnie(n, k + 1)
#ZAD2------------------------------------------

