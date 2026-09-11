number = float(input("Enter the number "))
if number == 0:
     print("Number is zero")
elif number > 0:
    if number % 2 == 0:
        print(f"Number {number} is positive and even")
    else:
        print(f"Number {number} is positive and odd")
else :
    if number % 2 == 0:
        print(f"Number {number} is negative and even")
    else:
        print(f"Number {number} is negative and odd")
        
