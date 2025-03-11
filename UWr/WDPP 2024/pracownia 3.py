from math import sqrt
from itertools import combinations_with_replacement
import turtle


def is_prime(n):
    if n < 2:
        return False

    dist = int(sqrt(n)) + 1

    for i in range(2, dist):
        if n % i == 0:
            return False

    return True


def is_lucky(m):
    if '7' * 3 in m:
        return True

    return False


def generate_hyperlucky():
    hyperlucky = []
    losowanie = ('012345689')
    for i in range(7, 11):
        wylosowane = combinations_with_replacement(losowanie, 10 - i)
        for c in wylosowane:
            po = '7' * i + ''.join(c)
            przed = ''.join(c) + '7' * i
            hyperlucky.append(po)
            if przed[0] != '0':
                hyperlucky.append(przed)

    return len(hyperlucky)


# ZAD 1

print('ZAD 1')

counter = 0
spelniajace = []
for i in range(777, 100001):
    if is_lucky(str(i)) and is_prime(i):
        counter += 1
        spelniajace.append(i)

print(f'Liczb szczesliwych pierwszych jest {counter}')
print(sorted(spelniajace))

# ZAD 2
print('ZAD 2')
print(generate_hyperlucky())

# ZAD 3
print('ZAD 3')


def usun_w_nawiasach(s):
    bracket = False
    new_s = ''
    for znak in s:

        if znak == '(':
            bracket = True

        elif znak == ')':
            bracket = False

        else:
            if bracket == False:
                new_s += znak

    return new_s


test1 = 'asdas (213123 234123) 12312 .'
test2 = '(12313) (123123) (123123) 333'

print(usun_w_nawiasach(test1))

# zad 4
def draw_square(size):
    for _ in range(4):
        turtle.forward(size)
        turtle.right(90)

# Ustawienia początkowe
turtle.speed(5)  # Prędkość rysowania

# Rysowanie 10 kwadratów, każdy mniejszy i wewnątrz poprzedniego
size = 200  # Początkowy rozmiar kwadratu
decrement = 20  # Zmniejszenie rozmiaru przy każdym kwadracie

for _ in range(10):
    draw_square(size)  # Narysowanie kwadratu
    size -= decrement  # Zmniejszenie rozmiaru na kolejny kwadrat
    turtle.penup()  # Podniesienie pióra, aby nie rysować podczas przemieszczania
    turtle.forward(decrement / 2)  # Przesunięcie do środka na kolejny kwadrat
    turtle.right(90)
    turtle.forward(decrement / 2)
    turtle.left(90)
    turtle.pendown()  # Opuszczenie pióra, aby rysować kolejny kwadrat

# Zakończenie rysowania
turtle.done()
