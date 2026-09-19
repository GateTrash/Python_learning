entered_number = int(input("Please, enter the limit number: "))
number1 = 1
while number1 <= entered_number:
    if number1 + 1 <= entered_number:
        print(number1 + 1, number1, end= " ")
        number1 += 2
    else:
        print(number1)
        number1 += 1    