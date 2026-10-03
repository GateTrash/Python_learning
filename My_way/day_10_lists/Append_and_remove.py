list_numbers = []
numbers = 1
while True:
    commant = input(f"List now: {list_numbers}; add(d) / remove(r) / exit(x): ")
    if(commant == "d"):
        list_numbers.append(numbers)
        numbers += 1
    elif(commant == "r"):
        if len(list_numbers) > 0:
            list_numbers.remove(numbers-1)
            numbers -= 1
        else:
            print("cannot be remove element in empty list")
    elif(commant == "x"):
        print("Bye")
        break
    else:
        print("Unknown command.")

