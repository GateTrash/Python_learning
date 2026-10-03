my_list = [1,2,3,4,5]
print(my_list)
while True:
    index = int(input("Enter index: "))
    if index == -1: break
    my_list[index] = int(input("New value: "))
    print(my_list)
