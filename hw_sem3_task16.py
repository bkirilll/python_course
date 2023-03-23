N = int(input("Введите размер массива: "))
list = [i for i in range(1, N+1)]
print(list)
x = int(input("Введите число: "))
answer = 0
for i in list:
    if i == x:
        answer +=1
print(f'Число {x} встречается {answer} раз')