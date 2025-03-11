from itertools import permutations


# ZAD 1
def ceasar(s, k, pl_alfabet):
    szyfrogram = ''
    przesuniety_alfabet = pl_alfabet[k:] + pl_alfabet[:k]
    slownik_szyfrujacy = dict(zip(pl_alfabet, przesuniety_alfabet))
    for znak in s:
        szyfrogram += slownik_szyfrujacy[znak]
    return szyfrogram


# ZAD 2
with open('popularne_slowa2023.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()
    nowe = [slowo.strip() for slowo in lines]


def najdluzsze_cesarskie(slowa, pl_alfabet):
    max_dlugosc = 0
    najdluzsze = []
    zbior_slow = set(slowa)

    for slowo in slowa:
        for i in range(1, len(pl_alfabet)):
            try:
                szyfrogram = ceasar(slowo, i, pl_alfabet)
                if szyfrogram in zbior_slow and szyfrogram != slowo:
                    if len(slowo) > max_dlugosc:
                        max_dlugosc = len(szyfrogram)
                        najdluzsze = [slowo]
                    elif len(slowo) == max_dlugosc:
                        najdluzsze.append(slowo)
            except:
                pass

    return najdluzsze


slowka = ['kot', 'mry', 'maciek', 'żłńupy']
polski_alfabet = "aąbcćdeęfghijklłmnńoóprsśtuwyzźż"

# ZAD 3
from itertools import permutations


def zagadka(wyrazenie):
    # Wyodrębnienie unikalnych liter
    letters = sorted(set(filter(str.isalpha, wyrazenie)))
    if len(letters) > 10:
        return False

    # Generowanie permutacji cyfr
    for perm in permutations(range(10), len(letters)):
        slownik_liter = dict(zip(letters, perm))

        # Zamiana liter na cyfry w równaniu
        result = wyrazenie
        for letter, digit in slownik_liter.items():
            result = result.replace(letter, str(digit))

        # Sprawdzenie poprawności równania
        left, right = result.split('=')
        left = left.split()
        if left[0][0] != '0' and left[2][0] != '0' and right[0][0] != '0':
            lewa_strona = int(left[0]) + int(left[2])
            try:
                if lewa_strona == int(right):
                    return slownik_liter
            except:
                continue  # Przechodzimy do następnej permutacji

    return None


# ZAD 4
def subset_sums(L):
    if not L:
        return [0]
    return sorted([x + L[0] for x in subset_sums(L[1:])] + subset_sums(L[1:]))


def non_decreasing_sequences(N, A, B):
    if N == 0:
        return {()}
    return {(x,) + seq for x in range(A, B + 1) for seq in non_decreasing_sequences(N - 1, x, B)}

print(subset_sums([1,2,3,100]))
print(non_decreasing_sequences(3, 10, 20))