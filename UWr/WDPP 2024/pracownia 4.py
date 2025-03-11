def okres_binarny(a, b):
    # Rozłożenie b na czynniki i usunięcie potęg 2
    tmp_b = b
    while tmp_b % 2 == 0:
        tmp_b //= 2

    # Jeśli po usunięciu potęg 2 tmp_b == 1, ułamek ma skończoną reprezentację
    if tmp_b == 1:
        return 0, ""  # Okres równy 0, brak części okresowej

    # Algorytm dla wyznaczania długości okresu i samego okresu binarnego
    reszta = a % b
    reszty = []
    okres_binarny = ""

    # Mnożenie reszty przez 2 symuluje przesunięcie binarnego przecinka
    while reszta not in reszty:
        reszty.append(reszta)
        reszta *= 2
        bit = reszta // b  # Wyciągamy bit (0 lub 1)
        okres_binarny += str(bit)  # Dodajemy bit do reprezentacji okresu
        reszta %= b  # Aktualizujemy resztę po wyciągnięciu bitu

    # Znajdujemy pozycję pierwszego wystąpienia okresu i długość cyklu
    pierwsza_pozycja = reszty.index(reszta)
    okres = len(reszty) - pierwsza_pozycja
    okres_binarny = okres_binarny[pierwsza_pozycja:]  # Wyciągamy binarny okres

    return okres, okres_binarny

print(okres_binarny(1, 2))