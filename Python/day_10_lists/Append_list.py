my_list = []
amount_updates = int(input("Enter amount updates: "))
item = 1
while amount_updates > 0:
    my_list.append(int(input(f"item {item}: ")))
    amount_updates -= 1
    item += 1
print(my_list)