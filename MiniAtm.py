balance = int(input("Enter your balance "))
amount = int(input("Enter waldrawal amount "))
if balance < 0 or amount <= 0:
    print("Incorrect data or you try get a zero")
elif balance >= amount:
    print(f"Your balance {balance - amount}")
elif balance < amount:
    print("Insufficient funds(")