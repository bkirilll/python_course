x = int(input("Введите x: "))
y = int(input("Введите y: "))

for i in range(x):
    for j in range(y):
        if x == i + j and y == i*j:
            print(i, j)