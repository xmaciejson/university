from math import sqrt

# ZAD 2
def selection_sort(array, size):
    licznik = 0
    licznik2 = 0
    i = 0
    while i < size - 1:
        # ZNALEZIENIE NAJMNIEJSZEGO ELEMENTU W TABLICY
        min_index = i
        j = i + 1
        while j < size:
            licznik += 1
            if array[j] < array[min_index]:
                min_index = j
            j += 1

            # Zamiana miejscami elementu najmniejszego z elementem na pozycji `i`
        if min_index != i:
            array[i], array[min_index] = array[min_index], array[i]
            licznik2 += 1
        i += 1

    return array, licznik, licznik2



# ZAD 3
def bubble_sort(array, size):
    i = 0
    l1 = 0
    l0 = 0
    while i < size - 1:
        j = 0
        while j < size - i - 1:
            l0 += 1
            if array[j] > array[j + 1]:
                # Zamiana miejscami, jeśli elementy są w złej kolejności
                array[j], array[j + 1] = array[j + 1], array[j]
                l1 += 1
            j += 1
        i += 1
    return array, l0, l1


# Testowanie


# ZAD 5

def sito(n):
    liczby = [1] * (n + 1)
    liczby[0] = liczby[1] = 0

    i = 2
    while i < int(sqrt(n)) + 1:
        if liczby[i] == 1:
            j = i * i
            while j < n + 1:
                liczby[j] = 0
                j += i
        i += 1

    wynik = []
    k = 0
    while k < n + 1:
        if liczby[k] == 1:
            wynik.append(k)
        k += 1

    return wynik

print(sito(125))



