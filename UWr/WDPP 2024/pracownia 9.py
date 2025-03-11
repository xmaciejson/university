import turtle
from itertools import combinations
from collections import Counter, defaultdict

# ZAD 1
'''
turtle.speed('fastest')
turtle.getscreen().bgcolor("black")
turtle.color("yellow")
turtle.penup()
turtle.goto((-200, 50))
turtle.pendown()

def star(size):
    if size <= 10:
        return
    else:
        for i in range(5):
            turtle.forward(size)
            star(size / 3)

            turtle.left(216)
star(360)
turtle.done()
'''

# ZAD 2
print('ZAD 2')
# POCZĄTKOWE ZMIENNE
imie = 'maciekbrandys'
litery_imienia = Counter(imie)
dlugosc_imienia = len(imie)

# ODCZYTANIE PLIKU
with open('popularne_slowa2023.txt', 'r', encoding='utf-8') as file:
    polish_words = file.read().splitlines()

# ZMNIEJSZENIE PLIKU Z OPTYMALIZACJĄ
przefiltrowane = [word for word in polish_words if set(word).issubset(litery_imienia.keys())]
przefiltrowane = [
    word for word in przefiltrowane
    if all(Counter(word)[letter] <= litery_imienia[letter] for letter in word)
]

# MAPOWANIE SŁÓW NA SŁOWNIKI LITER I BUDOWA SŁOWNIKA ODWROTNEGO
slownik_liter = {word: Counter(word) for word in przefiltrowane}
odwrotny_slownik = defaultdict(list)

for word, counter in slownik_liter.items():
    frozenset_key = frozenset(counter.items())  # Klucz to "zestaw liter i ich ilości"
    odwrotny_slownik[frozenset_key].append(word)

# SZUKANIE TRÓJEK SŁÓW
spelniajace = []

for slowa in combinations(przefiltrowane, 2):  # Generujemy dwójki słów
    suma_liter = slownik_liter[slowa[0]] + slownik_liter[slowa[1]]
    brakujace = litery_imienia - suma_liter  # Brakujące litery jako Counter

    # Zamiana brakujących liter na klucz w odwrotnym słowniku
    brakujace_klucz = frozenset(brakujace.items())
    if brakujace_klucz in odwrotny_slownik:  # Sprawdź, czy istnieje pasujące słowo
        for slowo3 in odwrotny_slownik[brakujace_klucz]:
            spelniajace.append(' '.join([*slowa, slowo3]))

print(spelniajace)

