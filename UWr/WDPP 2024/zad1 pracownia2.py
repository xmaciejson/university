n = 3
k = 5
counter1 = 0
counter2 = 0
wiersz1 = ''
wiersz2 = ''

for i in range(n * 2):

    if counter1 % 2 == 0:
        wiersz1 += '.' * k
        wiersz2 += '#' * k
        counter1 += 1
    else:
        wiersz1 += '#' * k
        wiersz2 += '.' * k
        counter1 += 1

wiersz1 += '\n'
wiersz2 += '\n'
licznik = 0

for i in range(0, n * 2):

    if licznik % 2 == 0:
        print(k * wiersz1, end='')
        licznik += 1

    else:
        print(k * wiersz2, end='')
        licznik += 1
