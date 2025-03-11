a = 0000000001100001
b = 0000000001111111
k = 16

x = str(bin(a) + bin(b))
y = x[k:-1]

if a[0] == b[0] and a[0] != y[0]:
    print('przekroczenie')

else:
    print(x)