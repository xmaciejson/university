from kwadrat import kwadrat
from turtle import update, clear
import random
import sys

MX, MY = 21, 21  # Rozmiar planszy
tab = [[0 for _ in range(MX)] for _ in range(MY)]  # 0 - białe, 1 - czarne
mx, my = MX // 2, MY // 2
kierunek = 1


def rysuj_plansze(tab):
    clear()
    for x in range(MX):
        for y in range(MY):
            kolor = 'black' if tab[y][x] == 1 else 'white'
            kwadrat(x, MY - y, kolor)
    update()


def zmien_kierunek(kierunek, wartosc_komorki):
    if wartosc_komorki == 0:
        return (kierunek + 1) % 4
    else:
        return (kierunek - 1) % 4


rysuj_plansze(tab)

while True:
    rysuj_plansze(tab)

    if kierunek == 0:  # góra
        my = (my - 1) % MY
    elif kierunek == 1:  # prawo
        mx = (mx + 1) % MX
    elif kierunek == 2:  # dół
        my = (my + 1) % MY
    elif kierunek == 3:  # lewo
        mx = (mx - 1) % MX

    kierunek = zmien_kierunek(kierunek, tab[my][mx])
    tab[my][mx] = 1 - tab[my][mx]