def to_bin(n):
    if n == 0:
        return 0

    elif n < 0:
        n *= -1

    binary = ''

    while n > 0:
        reszta = n % 2
        binary = str(reszta) + binary
        n //= 2

    return binary


liczba_bitow = int(input('Podaj liczbe bitow: '))
liczba = int(input('Podaj liczbe, ktora chcesz zakodowac: '))
zakres_dod = 2 ** (liczba_bitow - 1) - 1
zakres_uj = -2 ** (liczba_bitow - 1)
binarna = str(to_bin(liczba))
ujemna_bin = ''

if zakres_uj <= liczba <= zakres_dod:
    if len(binarna) <= liczba_bitow:
        dopisanie = liczba_bitow - len(binarna)
        binarna = '0' * dopisanie + binarna

        if liczba < 0:
            czy_jeden = False
            for i in range(len(binarna) - 1, -1, -1):

                if binarna[i] == '0' and not czy_jeden:
                    ujemna_bin += '0'

                else:
                    if czy_jeden:
                        if binarna[i] == '0':
                            ujemna_bin += '1'
                        else:
                            ujemna_bin += '0'
                    else:
                        czy_jeden = True
                        ujemna_bin += '1'
    if liczba > 0:
        print(binarna)

    else:
        print(ujemna_bin[::-1])

else:
    print('Liczba poza zakresem!')
