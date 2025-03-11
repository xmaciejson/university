from duze_cyfry import daj_cyfre


def dlc(n):
    liczba = str(n)

    wiersze = ['' for x in range(5)]

    for cyfra in liczba:

        cyfra_graf = daj_cyfre(int(cyfra))

        for i in range(5):
            wiersze[i] += cyfra_graf[i] + ' '

    for wiersz in wiersze:
        print(wiersz)

    return ''


print(dlc(112324))
