N = int(input("Введите размер массива: "))
list = [i for i in range(1, N+1)]
print(list)
x = int(input("Введите число: "))
for i in list:
    if i == x+1 or i == x-1:
        print(i)