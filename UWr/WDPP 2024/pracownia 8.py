# ZAD 2
def zamien_na_slownik(word):
    litery = list(word)
    word_dict = {}
    for litera in litery:
        if litera not in word_dict:
            word_dict[litera] = litery.count(litera)

    return word_dict


def czy_ukladalne(do_ulozenia, ulozone):
    dict1 = zamien_na_slownik(do_ulozenia)
    dict2 = zamien_na_slownik(ulozone)
    czy_mozna = True
    for key in dict1.keys():
        if key not in dict2 or dict1[key] > dict2[key]:
            czy_mozna = False

    return czy_mozna


# ZAD 3
print('ZAD 3')
#POCZĄTKOWE ZMIENNE
imie = 'jankociszewski'
litery_imienia = sorted(imie)
dlugosc_imienia = len(imie)

#ODCZYTANIE PLIKU
with open('popularne_slowa2023.txt', 'r', encoding='utf-8') as file:
    polish_words = file.read().splitlines()

#ZMNIEJSZENIE PLIKU
przefiltrowane = [word for word in polish_words
                  if set(word).issubset(litery_imienia) and len(word) <= dlugosc_imienia]
przefiltrowane_set = set(przefiltrowane)

#SZUKANIE ZAGADKI
spelniajace = []
odwrocone_zagadki = set()

for slowo1 in przefiltrowane_set:
    for slowo2 in przefiltrowane_set:
        zagadka = slowo1 + ' ' + slowo2
        if (sorted(slowo1 + slowo2) == litery_imienia
                and slowo2 + ' ' + slowo1 not in odwrocone_zagadki):
            spelniajace.append(zagadka)
            odwrocone_zagadki.add(zagadka)

print(spelniajace)



