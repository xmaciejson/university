import random
from collections import defaultdict as dd, Counter

with open('brown.txt', 'r') as brown:
    lines = brown.readlines()

# ZLICZANIE SŁÓW
brown_counter = Counter()
for line in lines:
    words = line.strip('\n').lower().split(' ')
    brown_counter.update(words)

# SŁOWNIK POLSKO-ANGIELSKI
pol_ang = dd(lambda: [])
for x in open('pol_ang.txt', encoding='utf-8'):
    x = x.strip()
    L = x.split('=')
    if len(L) != 2:
        continue
    pol, ang = L
    pol_ang[pol].append(ang)


def tlumacz(polskie):
    wynik = []
    for s in polskie:
        if s in pol_ang:
            mozliwe_tlumacznia = pol_ang[s]
            # ZNALEZIENIE MAKSYMALNEJ CZESCTOSCI
            czestosc = max(brown_counter[t] for t in mozliwe_tlumacznia)
            # WYBIERAMY SLOWA Z MAX CZESTOSCIA
            najlepsze = [t for t in mozliwe_tlumacznia if brown_counter[t] == czestosc]

            wynik.append(random.choice(najlepsze))

        else:
            wynik.append('[?]')
    return ' '.join(wynik)


zdanie = 'pogoda dziś super'.split()

for i in range(15):
    print(tlumacz(zdanie))
