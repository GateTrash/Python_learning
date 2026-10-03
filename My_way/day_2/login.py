login = input("Enter login of new account ")
password = input("Enter password ")
print("Okay, you create new account")
while True:
    entered_login = input("Enter login ")
    if entered_login == login:
        break
    print("Unknown login. Try again ")
while True:
    enterted_password = input(f"Enter password from account {login} ")
    if enterted_password == password:
        break
    print("Wrong password. Try again ")
print("You successfully loget in!")