from wdi import *

t = [3,8,2,1,7]
l = 0
p = 4


def podzial(l, p, a):
    x = a[l]
    i = l
    j = p
    while i < j:
        while a[j] > x: j = j - 1
        while a[i] < x: i = i + 1
        if i < j:
            y = a[j]
            a[j] = a[i]
            a[i] = y
            i = i + 1
            j = j - 1
    return j


def quicksort(a, l, r):
    if (l < r):
        s = podzial(l, r, a)
        quicksort(a, l, s)
        quicksort(a, s + 1, r)

print(quicksort(t, l, p))