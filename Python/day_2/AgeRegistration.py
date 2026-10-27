age = int(input("Enter your age "))
if age >= 18:
    print("Access granted. Let's fun!")
elif age > 0 :
    print("Access denied. Sorry, are you kid")
elif age == 0:
    print("How month of You?)")
else:
    print("Are you not born yet?")