def exp(a, b):
    if b == 0:
        return 1
    return a * exp(a, b - 1)

A = int(input('Введите число: '))
B = int(input('Введите степень числа: '))
print(exp(A, B))