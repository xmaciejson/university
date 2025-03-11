def podzial(l, p, a):
    x = a[l]
    i = l
    j = p
    while i < j:
        while a[j] > x:
            j -= 1
        while a[i] < x:
            i += 1
        if i < j:
            y = a[j]
            a[j] = a[i]
            a[i] = y
            i = i + 1
            j = j - 1
    return j


i = 0


def quicksort(a, l, r):
    global i
    i += 1
    if l < r:
        s = podzial(l, r, a)
        quicksort(a, l, s)
        quicksort(a, s + 1, r)
    return i


def hanoi(n, pocz, kon, tymcz):
    if n == 1:
        print(f'Przenieś krążek z wieży {pocz} na wieże {kon}')
    else:
        hanoi(n - 1, pocz, tymcz, kon)
        print(f'Przenieś krążek z wieży {pocz} na wieże {kon}')
        hanoi(n - 1, tymcz, kon, pocz)

print(hanoi(4,'A','B','C'))
