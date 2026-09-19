import random
eng_alphabet = "abcdefghijklmnopqrstuvwxyz"
password_length = int(input("Please, enter the password length: "))
password = ""
if password_length == 0 or password_length < 0:
    print("Password length must be greater than 0")
else:
    remaining_length = password_length
    while remaining_length > 0:
        rnd = random.randint(0,9)
        if password_length % 2 == 0:
            password += random.choice(eng_alphabet)
        else:
            password += str(rnd)
        remaining_length -= 1
    print(f"Your password {password}")