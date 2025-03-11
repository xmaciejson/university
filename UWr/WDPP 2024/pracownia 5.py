import turtle as pen
import random
from duze_cyfry import daj_cyfre

# ZAD 2
obwod = -150
pen.speed('fastest')
colors = ['yellow', 'purple', 'green']
for i in range(4):
    for color in colors:
        pen.begin_fill()
        pen.fillcolor(color)
        pen.circle(obwod)
        pen.end_fill()
        obwod += 10

pen.done()

# ZAD 3
pen.penup()
pen.speed('fastest')
def draw_square(x, y, size, color):
    pen.goto(x, y)
    pen.pendown()
    pen.fillcolor(color)
    pen.begin_fill()
    for _ in range(4):
        pen.forward(size)
        pen.right(90)
    pen.end_fill()
    pen.penup()

def draw_digit(digit, x, y, size=20):
    pattern = daj_cyfre(digit)  # Pobranie definicji cyfry
    color = random.choice(["red", "blue", "green", "purple", "orange", "yellow"])  # Losowy kolor

    # Przechodzimy przez wiersze i kolumny wzoru cyfry
    for row in range(len(pattern)):
        for col in range(len(pattern[row])):
            if pattern[row][col] == '#':  # Jeśli jest '#', rysujemy kwadrat
                draw_square(x + col * size, y - row * size, size, color)

# Funkcja do rysowania liczby n
def draw_number(n, x=0, y=0, size=20):
    for i, digit in enumerate(str(n)):
        draw_digit(int(digit), x + i * (size * 6), y, size)  # Przesuwamy pozycję dla każdej cyfry


draw_number(999, -200, 100, size=20)
pen.done()

# ZAD 4
def usun_duplikaty(l):
    l.sort()
    wynik = []

    for i in range(len(l)):
        if i == 0 or l[i] != l[i - 1]:
            wynik.append(l[i])

    return wynik

print(usun_duplikaty([12,312,41,12,4124,121,12]))