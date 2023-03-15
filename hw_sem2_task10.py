from random import randint


number = int(input("Введиет количество монеток: "))

list_1 = []

for i in range(number):
    list_1.append(randint(0, 1))
print(list_1)

count_zero = 0
count_one = 0

for i in range(number):
    if(list_1[i] == 0):
        count_zero +=1
    else:
        count_one +=1

if(count_one < count_zero):
    print(count_one)
else:
    print(count_zero)