from math import log2


# ZAD 1A
def zad_1a(n):  # zlozonosc o(1)
    wynik = (-1 ** n) * n
    return wynik


# ZAD 1B
def zad_1b(n):  # zlozonosc o(n)
    suma = 0
    for i in range(1, n + 1):
        suma += ((-1) ** i) / i

    return suma


# ZAD 1C
def zad_1c(n, x):  # zlozonosc o(1)
    suma = 0
    for i in range(1, n + 1):
        suma += i * (x ** i)

    return suma


# ZAD 2A
def nwd(a, b):  # zlozonosc o(LOG(MIN(A,B))
    while b != 0:
        a, b = b, a % b

    return a


def nww(a, b):  # zlozonosc o(LOG(MIN(A,B))
    return a * b // nwd(a, b)


# ZAD 2B
def ulamek(x, y):  # zlozonosc o(LOG(MIN(A,B))
    dzielnik = nwd(x, y)
    return x // dzielnik, y // dzielnik


# ZAD 3 #zlozonosc o(n * LOG(MIN(A,B))
n = int(input())
numbers = []
for i in range(n):
    numbers.append(int(input()))


def nwd_multiple(numbers):
    result = numbers[0]

    for number in numbers[1:]:
        result = nwd(result, number)
        if result == 1:
            break

    return result


# ZAD 4 #zlozonosc o(k * LOG(n))
n = int(input('Podaj dodatnią liczbę całkowitą: '))
k = int(input('Podaj dodatnią liczbę całkowitą: '))
nums = []
for i in range(k):
    num = int(input('Podaj dowolną liczbę naturalną większą od 1: '))
    nums.append(num)


def potegi(nums):
    max_p = 0
    divisors = []
    for num in nums:
        p = 1
        while num ** p <= n:
            if n % (num ** i) == 0 and i > max_p:
                max_p = i
                divisors = []
                divisors.append(num)
            elif n % (num ** i) == 0 and i == max_p:
                divisors.append(num)
            p += 1
    return max_p, divisors


# ZAD 5 zlozonosc o(dlugosc // 2)
dlugosc = int(input('Podaj dlugosc liczby binarnej: '))
binarna = input('Podaj liczbe w systemie bin: ')


def palindrom(binarna):
    for i in range(dlugosc // 2):
        if binarna[i] != binarna[dlugosc - 1 - i]:
            return False
    return True


# ZAD 6 o(log(n))
def k_palindrom(n, k):
    k_pal = ''
    temp = n
    while temp > 0:
        k_pal += str(temp % k)
        temp //= k

    for i in range(len(k_pal) // 2):
        if k_pal[i] != k_pal[len(k_pal) - 1 - i]:
            return False

    return True


# ZAD 7 o(d^2) gdzie d to liczba cyfr
def zapis_cyfrowy(n):
    k = 0
    cyfry = []
    for cyfra in n:
        if cyfra not in cyfry:
            k += 1
            cyfry.append(cyfra)

    return k


# ZAD 8 o(d) gdzie d to liczba cyfr
def zlicz_wystapienia(x):
    wystapienia = [0] * 10

    while x > 0:
        cyfra = x % 10
        wystapienia[cyfra - 1] += 1
        x //= 10

    return wystapienia


def podobienstwo(n, m):
    wystapienia_n = zlicz_wystapienia(n)
    wystapienia_m = zlicz_wystapienia(m)

    if wystapienia_n == wystapienia_m:
        return True

    else:
        return False
