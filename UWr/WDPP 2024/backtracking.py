from wdi import *

rozmiar = 5
su = 10
przyklad = [[1, 1, 2, 1, 1], [2, 1, 1, 1, 1], [0, 2, 1, 1, 1], [0, 1, 1, 2, 1], [2, 0, 1, 1, 2]]
t = [0] * rozmiar


def is_safe(w, n, tab):
    for k in range(n):
        if tab[k] == w:
            return False
    return True


def zetony(n, s, x, wier, suma=0, kol=0):
    if kol == n:
        return suma == s

    for i in range(n):
        if is_safe(i, kol, wier):
            wier[kol] = i
            if zetony(n, s, x, wier, suma + x[kol][i], kol + 1):
                return True

    return False


class TreeItem:
    def __init__(self, value):
        self.val = value
        self.hlp = -100
        self.size = 1
        self.left = None
        self.right = None


def wypisz_sciezke(r, x, path=''):
    if r is None:
        return 0

    path += str(r.val) + ' '

    if r.val == x:
        return path

    lewe = wypisz_sciezke(r.left, x, path)
    if lewe:
        return 1, path
    prawe = wypisz_sciezke(r.right, x, path)
    if prawe:
        return 1, prawe

    return 0


def s(r):
    if r is None:
        return 0
    return r.val + s(r.left) + s(r.right)


def balans(root):
    if root is None:
        return 0

    suma_lewa = s(root.left)
    suma_prawa = s(root.right)

    return suma_lewa - suma_prawa


def suma_drzewa(root):
    if root is None:
        return 0

    suma_l = suma_drzewa(root.left)
    suma_p = suma_drzewa(root.right)

    return root.val + suma_l + suma_p


def wysokosc(root):
    if root is None:
        return 0

    wysokosc_p = wysokosc(root.right)
    wysokosc_l = wysokosc(root.left)

    return 1 + max(wysokosc_p, wysokosc_l)


def suma_parzysta(root, i=0):
    if root is None:
        return 0

    if i % 2 == 0:
        suma_p = root.val
        suma_np = 0
    else:
        suma_p = 0
        suma_np = root.val

    return (suma_p - suma_np) + suma_parzysta(root.left, i + 1) + suma_parzysta(root.right, i + 1)


def wypisz_s(root, x, sciezka=''):
    if root is None:
        return 0

    nowa_s = str(root.val) + ' ' + sciezka

    if root.val == x:
        print(nowa_s)
        return 1

    if wypisz_s(root.left, x, nowa_s) == 1 or wypisz_s(root.right, x, nowa_s) == 1:
        return 1

    return 0


def zbalansowane(r, k):
    if r is None:
        return 0
    if r.left is None and r.right is None:
        return 1

    lewe = zbalansowane(r.left, k)
    prawe = zbalansowane(r.right, k)

    if abs(lewe - prawe) <= k:
        return lewe + prawe
    else:
        return -1


def suma(root):
    if root is None:
        return 0
    return root.val + suma(root.left) + suma(root.right)


def balansKorz(r):
    if r is None:
        return 0
    lewe = suma(r.left)
    prawe = suma(r.right)

    return abs(lewe - prawe)


def balansDrzewa(r):
    if r is None:
        return 0

    sum_left = suma(r.left)
    sum_right = suma(r.right)
    balans = abs(sum_right - sum_left)
    if balans > r.hlp:
        r.hlp = balans

    return max(r.hlp, balansDrzewa(r.left), balansDrzewa(r.right))


def sprawdz(tab, n):
    for i in range(n):
        if tab[i] != tab[n - i - 1]:
            return False
    return True


def palindrom(x, n):
    najdluzszy = 1
    for i in range(n):
        for j in range(n - 1, i, -1):
            if x[i] == x[j]:
                if sprawdz(x[i:j + 1], j - i + 1):
                    najdluzszy = max(najdluzszy, j - i + 1)
    return najdluzszy


def w(r):
    if r is None:
        return 0

    left = w(r.left)
    right = w(r.right)

    return 1 + max(left, right)


def odseparowane(r, s):
    if r is None:
        return True
    suma_lewa = suma(r.left)
    suma_prawa = suma(r.right)

    warunek1 = abs(suma_lewa - suma_prawa)
    if warunek1 <= s or r.right is None or r.left is None:
        return 1 if odseparowane(r.left, s) and odseparowane(r.right, s) else 0
    else:
        return False


def rozszerzone(r, b):
    if r is None:
        return 0

    if r.val >= b:
        prawe_suma = r.right.size if r.right else 0
        return 1 + prawe_suma + rozszerzone(r.left, b)
    else:
        return rozszerzone(r.right, b)


def waga(r):
    if r is None:
        return 1

    suma_lewa = suma(r.left)
    suma_prawa = suma(r.right)

    if suma_lewa == suma_prawa:
        if waga(r.left) == 1 and waga(r.right) == 1:
            return 1
        else:
            return 0
    else:
        return 0


def sciezka(r):
    if r is None:
        return 0

    sciezka_p = sciezka(r.right)
    sciezka_l = sciezka(r.left)

    return r.val + max(sciezka_l, sciezka_p)


def suma_wierzcholkow(n):
    if n is None:
        return 0
    return 1 + suma_wierzcholkow(n.left) + suma_wierzcholkow(n.right)


def bal(r):
    if r is None:
        return 0

    lewe = suma_wierzcholkow(r.left)
    prawe = suma_wierzcholkow(r.right)

    return abs(lewe - prawe)


def balfull(r):
    if r is None:
        return 0

    sp = suma_wierzcholkow(r.right)
    sl = suma_wierzcholkow(r.left)
    roznica = abs(sp - sl)
    if roznica > r.hlp:
        r.hlp = roznica

    balfull(r.left)
    balfull(r.right)

    return r.hlp


def ciezar(r):
    if r is None:
        return 0

    sumal = suma(r.left)
    sumap = suma(r.right)

    return r.val + sumap + sumal


def maxciezar(r):
    if r is None:
        return 0

    sumal = suma(r.left)
    sumap = suma(r.right)
    c = sumal + sumap + r.val

    if c > r.hlp:
        r.hlp = c

    max_l = maxciezar(r.left)
    max_r = maxciezar(r.right)

    return max(r.hlp, max_r, max_l)


def bk(r):
    if r is None:
        return 0

    sl = suma(r.right)
    sp = suma(r.left)
    roznica = abs(sl - sp)

    return roznica



def podciag(n, x):
    max_suma = -1000
    akt_suma = 0

    for i in range(n):
        akt_suma = max(x[i], akt_suma + x[i])
        max_suma = max(max_suma, akt_suma)

    return max_suma


def obciazenie(n, k, X, Y):
    kolumny = [0] * k
    wiersze = [0] * k

    for i in range(n):
        kolumny[X[i]] += 1
        wiersze[Y[i]] += 1

    max_ob = 0
    for j in range(k):
        akt = max(kolumny[j], wiersze[j])
        max_ob = max(akt, max_ob)

    return max_ob


def zroznicowany(k, n, a):
    dzielniki = [0] * 10
    counter = 0

    for i in range(n):
        reszta = a[i] % 10
        if dzielniki[reszta] == 0:
            counter += 1
            dzielniki[reszta] = 1

        if counter == k:
            return i + 1

    return 0

def bd(r):
    if r is None:
        return 0

    sp = suma(r.right)
    sl = suma(r.left)
    balans = abs(sp - sl)

    if balans > r.hlp:
        r.hlp = balans

    return max(r.hlp, bd(r.right), bd(r.left))

def w(r):
    if r is None:
        return 0

    return r.val + w(r.left) + w(r.right)

def s(r):
    if r is None:
        return 0

    sciezka_lewa = s(r.left)
    sciezka_prawa = s(r.right)

    return r.val + max(sciezka_prawa, sciezka_lewa)

def policz_ciezar(r):
    if r is None:
        return 0

    return r.val + policz_ciezar(r.left) + policz_ciezar(r.right)

def mciezar(r):
    if r is None:
        return 0

    l = policz_ciezar(r.left)
    p = policz_ciezar(r.right)

    return r.val + l + p

def max_ciezar(r):
    if r is None:
        return 0

    l = policz_ciezar(r.left)
    p = policz_ciezar(r.right)
    c = r.val + l + p

    if c > r.hlp:
        r.hlp = c

    return max(r.hlp, max_ciezar(r.right), max_ciezar(r.left))


def policz_liscie(r):
    if r is None:
        return 0
    if r.left is None and r.right is None:
        return 1
    return policz_liscie(r.right) + policz_liscie(r.left)


def lisciowo_zbalansowane(r, k):
    if r is None:
        return 0

    l = policz_liscie(r.left)
    p = policz_liscie(r.right)
    roznica = abs(l - p)

    if roznica > k:
        return -1
    else:
        if lisciowo_zbalansowane(r.left, k) == -1 or lisciowo_zbalansowane(r.right, k) == -1:
            return -1
        else:
            return l + p

def policz(r, t):
    if r is None:
        return 0
    if r.val == t:
        return policz(r.left, r.val) + policz(r.right, r.val)
    else:
        return 1 + policz(r.left, r.val) + policz(r.right, r.val)


def zrozn(t):
    if t is None:
        return 0

    policz_l = policz(t.right, t.val)
    policz_p = policz(t.left, t.val)

    return 1 + policz_l + policz_p



a = TreeItem(1)
a.right = TreeItem(2)
a.right.right = TreeItem(2)
a.right.right.left = TreeItem(1)
a.right.right.right = TreeItem(1)
a.left = TreeItem(1)
a.left.left = TreeItem(2)
a.left.right = TreeItem(2)
print(suma_parzysta(a))







