# ZAD 4

def g(n):
    if n == 0 or n == 1 or n == 2:
        return 1

    g0, g1, g2 = 1, 1, 1

    for i in range(3, n + 1):
        g_next = g0 + g1 + g2
        g0, g1, g2 = g1, g2, g_next

    return g2
print(g(5))
# ZAD 6
MaxN = 1000
def fibonacci(k, r):
    f = [0] * MaxN
    f[0] = 1
    f[1] = 1
    for i in range(2, k + 1):
        f[i] = f[i - 1] + f[i - 2]

    return f[k]

print(fibonacci(6, 6))

def fibonacci_2(k, r):
    if k == 0:
        return 0 % r
    elif k == 1:
        return 1 % r

    a, b = 1, 1
    for i in range(2, k + 1):
        a, b = b, (a + b) % r

    return b
print(fibonacci_2(7, 1))

# ZAD 7
def fast_power(n, k):
    result = 1
    while k > 0:
        if k % 2 == 1:
            result *= n
        k //= 2
        n *= n

    return result


def find(n, m):
    if n >= m:
        return 1

    left, right = 1, m
    while left < right:
        mid = (left + right) // 2
        if fast_power(n, mid) >= m:
            right = mid
        else:
            left = mid + 1

    return left
