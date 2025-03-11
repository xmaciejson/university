import string

# ZAD 1
def rozni_o_jedna_litere(word1, word2):
    if len(word1) != len(word2):
        return False
    roznice = sum(1 for a, b in zip(word1, word2) if a != b)
    return roznice == 1


def zbuduj_graf(word_list):
    graf = {word: [] for word in word_list}
    polski_alfabet = "aąbcćdeęfghijklłmnńoóprsśtuwyzźż"

    for word in word_list:
        for pozycja in range(len(word)):
            nowe = word
            for litera in polski_alfabet:
                if litera != word[pozycja]:
                    nowe = word[:pozycja] + litera + word[pozycja + 1:]
                    if nowe in zbior:
                        graf[word].append(nowe)
                        #print(graf[word])

    return graf


def znajdz_droge(start, end, word_list):
    if start == end:
        return [start]

    graf = zbuduj_graf(word_list)
    odwiedzone = set()
    sciezki = [[start]]

    while sciezki:

        sciezka = sciezki.pop(0)
        slowo = sciezka[-1]

        if slowo in odwiedzone:
            continue
        odwiedzone.add(slowo)

        for sasiad in graf.get(slowo, []):
            nowa_sciezka = sciezka + [sasiad]
            if sasiad == end:
                return nowa_sciezka
            sciezki.append(nowa_sciezka)

    return []

word_list = ["mąka", "mika", "miks", "kiks", "keks", "woda", "wino", "wola", "kola"]
with open('popularne_slowa2023.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()
    zbior = set(line.strip() for line in lines)
#print(znajdz_droge('mąka', 'keks', zbior))
#print(znajdz_droge('woda', 'wino', zbior))

'''
# ZAD 4
def postac_normalna(slowo):
    letter_to_number = {}
    normalized_form = []
    current_number = 1

    for letter in slowo:
        if letter not in letter_to_number:
            letter_to_number[letter] = current_number
            current_number += 1
        normalized_form.append(str(letter_to_number[letter]))

    return '-'.join(normalized_form)


def slownik_normalny(nazwa):
    with open(nazwa, 'r', encoding='utf-8') as file:
        slowa = file.readlines()

    normal_dict = {}
    for s in slowa:
        normal_form = postac_normalna(s.strip())
        normal_dict[normal_form] = s.strip()

    return normal_dict

def rozszyfruj(tekst, slownik):
    wiadomosc = []
    new_tekst = tekst.split()
    for w in new_tekst:
        if w in string.punctuation:
            wiadomosc.append(w)
        else:
            normal_form = postac_normalna(w)
            try:
                wiadomosc.append(slownik[normal_form])
            except:
                pass

    return ' '.join(wiadomosc)

def main():
    slownik_test = slownik_normalny('popularne_slowa2023.txt')

    #ODCZYTANIE SZYFROGRAMU
    with open('szyfrogramy.txt', 'r', encoding='utf-8') as file:
        szyfrogramy = file.readlines()

    for szyfrogram in szyfrogramy:
        rozszyfrowane = rozszyfruj(szyfrogram, slownik_test)
        print(rozszyfrowane)

main()
'''

# ZAD 3
def in_tree(tree, e):
    if tree == []:
        return False
    n, left, right = tree
    if n == e:
        return True
    if e < n:
        return in_tree(left, e)
    return in_tree(right, e)


def tree_to_list(tree):
    if tree == []:
        return []
    n, left, right = tree
    return tree_to_list(left) + [n] + tree_to_list(right)


def add_to_tree(e, tree):
    if tree == []:
        tree.append(e)
        tree.append([])
        tree.append([])
        return
    v, left, right = tree

    if v == e:
        return
    if e < v:
        add_to_tree(e, left)
    else:
        add_to_tree(e, right)

class Set:
    def __init__(self, *elems):
        self.tree = []
        for e in elems:
            # add_to_tree(e, self.tree)
            self.add(e)

    def add(self, e):
        add_to_tree(e, self.tree)

    def __contains__(self, e):
        return in_tree(self.tree, e)
    #
    def __len__(self):
        return len(tree_to_list(self.tree))  # Liczba elementów w zbiorze

    def __and__(self, other): # Przeciecie zbiorow
        result = Set()
        for e in tree_to_list(self.tree):
            print(e)
            if e in other:
                result.add(e)
        return result

    def __sub__(self, other): # Roznica zbiorow
        result = Set()
        for e in tree_to_list(self.tree):
            if e not in other:
                result.add(e)
        return result

    def __or__(self, other): # Suma zbiorow
        result = Set()
        for e in tree_to_list(self.tree):
            result.add(e)
        for e in tree_to_list(other.tree):
            result.add(e)
        return result
    #
    def __str__(self):
        return '{' + ', '.join(str(n) for n in tree_to_list(self.tree)) + '}'

s1 = set([1,2,3,4,5])
s2 = [3,4,5,6,7]
test = Set(s1)
test2 = Set(s2)
print(test & test2)