import random
import turtle


macierz = [[0 for a in range(100)] for b in range(100)]

#PRZYPISANIE NIEZEROWYCH WARTOSCI
for x in range(20):
    wartosc = random.uniform(0.01, 1)
    cord_x = random.randint(0, 99)
    cord_y = random.randint(0, 99)
    macierz[cord_x][cord_y] = wartosc

#SREDNIA WAZONA
def srednia(matrix, i, j):
    sasiedzi = [
        [i-1, j], [i+1, j],  # góra, dół
        [i, j-1], [i, j+1],  # lewo, prawo
        [i-1, j-1], [i-1, j+1], [i+1, j-1], [i+1, j+1]] #skosy

    suma = matrix[i][j]
    for sasiad in sasiedzi:
        suma += matrix[sasiad[0]][sasiad[1]]

    avg = suma / len(sasiedzi) + 1

    return avg

#WYPELNIANIE SREDNIA
for y in range(80):
    cord_x = random.randint(0, 99)
    cord_y = random.randint(0, 99)
    wysokosc = srednia(macierz, cord_x, cord_y)

#