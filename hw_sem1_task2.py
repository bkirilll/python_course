number = int(input("Введите трехзначное число: "))

sum = 0
while(number > 0):
    temp = 0
    temp = number % 10
    sum += temp
    number = number//10

print(sum)
