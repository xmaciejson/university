import turtle
import random

# ZAD 1
def wczytaj_obraz(nazwa_pliku):
    
    #Wczytuje obraz z pliku tekstowego i zwraca listę wierszy pikseli.
    
    obraz = []
    with open(nazwa_pliku, 'r') as plik:
        for linia in plik:
            wiersz = [eval(pixel) for pixel in linia.strip().split()]
            obraz.append(wiersz)
    return obraz


def rysuj_obraz(obraz, rozmiar_piksela):
    
    #Rysuje obraz za pomocą modułu turtle.
    
    turtle.tracer(0, 1)  # Przyspiesza rysowanie
    turtle.speed('fastest')
    turtle.penup()
    poczatek_x = -len(obraz[0]) * rozmiar_piksela // 2
    poczatek_y = len(obraz) * rozmiar_piksela // 2

    for i, wiersz in enumerate(obraz):
        for j, piksel in enumerate(wiersz):
            # Wyraźnie konwertujemy wartości RGB na tuplę z trzema floatami
            kolor = (float(piksel[0]) / 255, float(piksel[1]) / 255, float(piksel[2]) / 255)
            turtle.fillcolor(kolor)
            turtle.goto(poczatek_x + j * rozmiar_piksela, poczatek_y - i * rozmiar_piksela)
            turtle.begin_fill()
            for _ in range(4):
                turtle.forward(rozmiar_piksela)
                turtle.right(90)
            turtle.end_fill()

    turtle.update()
    turtle.done()


nazwa_pliku = "piksele.txt"  # Nazwa pliku z obrazem
rozmiar_piksela = 5  # Rozmiar pojedynczego piksela

# Wczytanie obrazu i rysowanie
obraz = wczytaj_obraz(nazwa_pliku)
rysuj_obraz(obraz, rozmiar_piksela)

# ZAD 2

def wczytaj_obraz(nazwa_pliku):
    
    #Wczytuje obraz z pliku tekstowego i zwraca listę wierszy pikseli.
    
    obraz = []
    with open(nazwa_pliku, 'r') as plik:
        for linia in plik:
            wiersz = [eval(pixel) for pixel in linia.strip().split()]
            obraz.append(wiersz)
    return obraz


def rysuj_obraz_losowo(obraz, rozmiar_piksela):
    
    #Rysuje obraz za pomocą modułu turtle, rysując piksele w losowej kolejności.
    
    
    turtle.speed('fastest')
    turtle.penup()
    poczatek_x = -len(obraz[0]) * rozmiar_piksela // 2
    poczatek_y = len(obraz) * rozmiar_piksela // 2

    # Przygotowanie listy współrzędnych pikseli
    piksele = [
        (i, j, obraz[i][j])
        for i in range(len(obraz))
        for j in range(len(obraz[i]))
    ]
    # Przetasowanie pikseli
    random.shuffle(piksele)

    # Rysowanie przetasowanych pikseli
    for i, j, piksel in piksele:
        kolor = (float(piksel[0]) / 255, float(piksel[1]) / 255, float(piksel[2]) / 255)
        turtle.fillcolor(kolor)
        turtle.goto(poczatek_x + j * rozmiar_piksela, poczatek_y - i * rozmiar_piksela)
        turtle.begin_fill()
        for _ in range(4):
            turtle.forward(rozmiar_piksela)
            turtle.right(90)
        turtle.end_fill()

    turtle.update()
    turtle.done()


nazwa_pliku = "piksele.txt"  # Nazwa pliku z obrazem
rozmiar_piksela = 5  # Rozmiar pojedynczego piksela

# Wczytanie obrazu i rysowanie w losowej kolejności
obraz = wczytaj_obraz(nazwa_pliku)
rysuj_obraz_losowo(obraz, rozmiar_piksela)

# ZAD 3
polskie_znaki = "ąćęłńóśżźĄĆĘŁŃÓŚŻŹ"
interpunkcja = "—,.!?;:-()[]{}\"'<>/\\|`~@#$%^&*+=_"


def czy_polskie_znaki(slowo):
    return any(znak in polskie_znaki for znak in slowo)


def czy_interpunkcja(slowo):
    return any(znak in interpunkcja for znak in slowo)


def czy_polskie_slowo(slowo):
    return slowo in polish_words_set


with open('popularne_slowa2023.txt', 'r', encoding='utf-8') as polish_file:
    polish_words = polish_file.read().splitlines()
    polish_words_set = set(polish_words)

with open('lalka_nowy.txt', 'r', encoding='utf-8') as file:
    lines = file.read()
    tekst = lines.split()
    najdluzszy_ciag = []
    aktualny_ciag = []

    for word in tekst:
        if not czy_polskie_znaki(word) and not czy_interpunkcja(word) and czy_polskie_slowo(word):
            aktualny_ciag.append(word)
        else:
            if len(aktualny_ciag) > len(najdluzszy_ciag):
                print(aktualny_ciag)
                najdluzszy_ciag = aktualny_ciag
            aktualny_ciag = []

    if len(aktualny_ciag) > len(najdluzszy_ciag):
        najdluzszy_ciag = aktualny_ciag

    print('Najdluższy ciąg: ', najdluzszy_ciag)
