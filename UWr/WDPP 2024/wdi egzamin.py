from pythonProject.pracownie.wdi import Array


class TreeItem:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None


def sumaPN(r, i=0):
    if r is None:
        return 0  # Poprawiony warunek końcowy

    suma_p = 0
    suma_l = 0

    if i % 2 == 0:
        suma_p = r.val
    else:
        suma_l = r.val

    return (suma_p - suma_l) + sumaPN(r.left, i + 1) + sumaPN(r.right, i + 1)


def policz(root):
    if root is None:
        return 0

    return 1 + policz(root.right) + policz(root.left)


def wysokosc(root):
    if root is None:
        return 0

    lewa = wysokosc(root.left)
    prawa = wysokosc(root.right)

    if prawa > lewa:
        return prawa + 1
    else:
        return lewa + 1


t = TreeItem(1)
t.right = TreeItem(7)
t.right.right = TreeItem(19)
t.left = TreeItem(9)
t.left.right = TreeItem(3)
t.left.right.left = TreeItem(2)
t.left.right.left.right = TreeItem(5)
t.left.left = TreeItem(11)
t.left.left.left = TreeItem(4)


def suma_sasiednich(X, n):
    max_suma = -999
    for i in range(n):
        suma = X[i]
        if suma > max_suma:
            max_suma = suma
        for j in range(i + 1, n):
            suma += X[j]
            if suma > max_suma:
                max_suma = suma

    return max_suma


def zagadka(A, x, l, p):
    if l == p:
        if A[l] <= x:
            return A[l]
        else:
            return 0
    if l > p:
        return 0
    s = (l + p) // 2
    if (l + p) % 2 == 0:
        s -= 1
    sl = zagadka(A, x, l, s)
    sr = zagadka(A, x, s + 1, p)

    return sl + sr


def lisciowo_zbalansowane(root, k):
    if root is None:
        return 0

    if root.left is None and root.right is None:
        return 1

    lewe = lisciowo_zbalansowane(root.left, k)
    prawe = lisciowo_zbalansowane(root.right, k)
    roznica = lewe - prawe

    if roznica < 0:
        roznica *= -1

    if roznica <= k:
        return lewe + prawe
    else:
        return -1


def dfs(root):
    if root is None:
        return

    print(root.val)
    lewe = dfs(root.left)
    prawe = dfs(root.right)


def z2(n, k):
    if k >= n:
        return 1
    if n % k == 0 and k > 1:
        return 1 + z2(n // 2, k)
    return z2(n, k + 1)


from math import sqrt


def is_prime(n):
    if n < 2:
        return False

    dist = int(sqrt(n)) + 1
    for i in range(2, dist):
        if n % i == 0:
            return False
    return True


def pol(num):
    if num == 2:
        return 1

    licznik = 0
    for i in range(2, num // 2):
        if is_prime(i) and num % i == 0:
            licznik += 1

    return licznik


def ob(n, k, X, Y):
    kolumny = Array(k)
    wiersze = Array(k)
    for l in range(k):
        wiersze[l] = 0
        kolumny[l] = 0

    for i in range(n):
        kolumny[X[i]] += 1
        wiersze[Y[i]] += 1

    najwieksze_ob = 0
    for j in range(k):
        obciazenie = 0
        if kolumny[j] > wiersze[j]:
            obciazenie = kolumny[j]
        else:
            obciazenie = wiersze[j]

        if obciazenie > najwieksze_ob:
            najwieksze_ob = obciazenie

    return najwieksze_ob



    
