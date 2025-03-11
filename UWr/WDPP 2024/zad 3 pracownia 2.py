from math import sqrt
n = 10; print('\n'.join(''.join('#' if sqrt(((n - 1) / 2 - i) ** 2 + ((n - 1) / 2 - j) ** 2) <= ((n - 1) / 2) + 1 else ' ' for j in range(n)) for i in range(n)))



'''
def kolko(n, odlegosc):
    r = (n - 1) / 2
    spacje = (odlegosc - n) // 2

    for i in range(n):
        print(' ' * spacje, end='')
        for j in range(n):

            distance = sqrt((r - i) ** 2 + (r - j) ** 2)
            if distance <= r + 1:
                print('#', end='')
            else:
                print(' ', end='')

        print()
'''
