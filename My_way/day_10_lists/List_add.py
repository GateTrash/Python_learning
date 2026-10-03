list_numbers = []
element = int(input("New element: "))
list_numbers.append(element)
while True:
    print(f"List now: {list_numbers}; List sorted: {sorted(list_numbers)}", end= " ")
    element = int(input("New element: "))
    if(element == 0):
        print("Bye!")
        break
    else:
        list_numbers.append(element)