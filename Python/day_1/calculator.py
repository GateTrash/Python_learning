first_number = int(input("Enter the first number "))
operation = input("Enter the operation (+, -, /, *): ")
second_number = int(input("Enter the second number "))
if operation == "+":
    print("Result", first_number + second_number)
elif operation == "-":
    print("Result", first_number - second_number)
elif operation == "/":
    if second_number == 0:
        print("Cannot devide by zero")
    else:
        print("Result", first_number / second_number)
elif operation == "*":
    print("Result", first_number * second_number)
else:
    print("Unknown operation")