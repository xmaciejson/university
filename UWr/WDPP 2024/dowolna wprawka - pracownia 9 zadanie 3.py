#ZAD 3
liczby = {
      1 : 'jeden',

      2 : 'dwa',

      3 : 'trzy',

      4 : 'cztery',

      5 : 'pięć',

      6 : 'sześć',

      7 : 'siedem',

      8 : 'osiem',

      9 : 'dziewięć',

      10 : 'dziesięć',

      11 : 'jedenaście',

      12 : 'dwanaście',

      13 : 'trzynaście',

      14 : 'czternaście',

      15 : 'piętnaście',

      16 : 'szesnaście',

      17 : 'siedemnaście',

      18 : 'osiemnaście',

      19 : 'dziewiętnaście',

      20 : 'dwadzieścia',

      30 : 'trzydzieści',

      40 : 'czterdzieści',

      50 : 'pięćdziesiąt',

      60 : 'sześćdziesiąt',

      70 : 'siedemdziesiąt',

      80 : 'osiemdziesiąt',

      90 : 'dziewięćdziesiąt',

      100 : 'sto',

      200 : 'dwieście',

      300 : 'trzysta',

      400 : 'czterysta',

      500 : 'pięćset',

      600 : 'sześćset',

      700 : 'siedemset',

      800 : 'osiemset',

      900 : 'dziewięćset'
    }

def tekstowa(num):
    dlugosc = len(num)
    wynik = ''
    if dlugosc == 3:
        for i in range(dlugosc):
            if i == 0:
                czesc_setna = num[0] + '00'
                wynik += str(liczby[int(czesc_setna)])
            if i == 1:
                if int(num) <= 20:
                    wynik += str(liczby[int(num)])
                else:
                    czesc_dziesietna = num[1] + '0'
                    wynik += ' ' + str(liczby[int(czesc_dziesietna)])
            if i == 2:
                wynik += ' ' + str(liczby[int(num[2])])

    if dlugosc == 2:
        if int(num) <= 20:
            wynik += str(liczby[int(num)])
        else:
            for i in range(dlugosc):
                if i == 0:
                    czesc_dziesietna = num[0] + '0'
                    wynik += str(liczby[int(czesc_dziesietna)])
                if i == 1:
                    wynik += ' ' + str(liczby[int(num[1])])

    if dlugosc == 1:
        wynik += str(liczby[int(num[0])])

    return wynik

def napis_z_liczbami(napis):
    poprawiony = ''
    slowa = napis.split(' ')
    for slowo in slowa:
        if slowo.isdigit():
            poprawiony += tekstowa(slowo) + ' '
        else:
            poprawiony += slowo + ' '
    return poprawiony

print(napis_z_liczbami('maciek ma 19 lat i 312 psy i 9 kotów! ma też 186 cm wzrostu oraz spał wczoraj 15 godzin'))