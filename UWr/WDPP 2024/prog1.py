from math import sqrt  # pierwiastek kwadratowy


def potega(a, n):
    wynik = 1  # zmienna lokalna
    for i in range(n):
        wynik = wynik * a  # albo: wynik *= a
    return wynik


def kwadrat(n):
    for i in range(n):
        for j in range(n):  # pętla w pętli
            print("*", end="")
        print()


def kwadrat2(n):
    for i in range(n):
        print(n * "#")

    # wcześniej były definicje, poniżej jest część która się wykonuje

'''
for i in range(10):
    print(i, 2 ** i, potega(2, i), sqrt(
        i))  # drukujemy kolejne liczby wraz z kolejnymi potęgami dwójki oraz kolejnymi pierwiastkami  
'''

print()

k = 3
j = 3
for i in range(10):
    if i > 0:
        k += 2
    if i < 5:
        print("Przebieg:", i)
        print(k * (20 * "-" + '\n'))
    else:
        print("Przebieg:", i)
        print('#\n' * j)
        j += 1

    print()  # pusty wiersz
