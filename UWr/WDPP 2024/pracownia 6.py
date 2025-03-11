# ZAD 2
print('ZAD 2')

with open('popularne_slowa2023.txt', 'r', encoding='utf-8') as file:
    words = file.readlines()
    print(len(words))
    reverse_dict = {word.strip('\n'): word[::-1].strip('\n') for word in words}
    reverse_pair = set()

    for word in words:
        new_word = word.strip('\n')
        reverse_word = reverse_dict[new_word]
        if reverse_word in reverse_dict:
            reverse_pair.add((new_word, reverse_word))

    print(sorted(reverse_pair))

# ZAD 3
print('ZAD 3')

def prime_divisors(n):
    divisors = set()
    czynnik = 2
    while czynnik ** 2 <= n:
        while n % czynnik == 0:
            divisors.add(czynnik)
            n //= czynnik
        czynnik += 1

    if n > 1:
        divisors.add(n)

    return divisors


print(prime_divisors(15))

# ZAD 4
print('ZAD 4')

def podziel(s):
    podzielone = []
    czy_nowe = True
    slowo = ''
    for znak in s:
        if znak == ' ' and not czy_nowe:
            czy_nowe = True
            podzielone.append(slowo)

        elif not czy_nowe:
            slowo += znak

        else:
            if znak == ' ':
                czy_nowe = False
            else:
                slowo = '' + znak
                czy_nowe = False

    if len(slowo) > 0:
        podzielone.append(slowo)

    return podzielone

