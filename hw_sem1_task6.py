number = int(input("Введите номер билета: "))

number_len = str(number)
if(len(number_len) == 6):
    firstHalf = number // 1000
    secondHalf = number % 1000
    sum1 = 0
    sum2 = 0
    while(firstHalf > 0):
        temp1 = firstHalf % 10
        temp2 = secondHalf % 10
        sum1 +=temp1
        sum2 +=temp2
        firstHalf = firstHalf // 10
        secondHalf = secondHalf // 10
    if(sum1 == sum2):
        print("Твой билет счастливый!")
    else:
        print("Твой билет несчастливый(")
else:
    print("Номер билета должен быть 6-значным")


