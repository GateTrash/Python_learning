def Hash_Square(size):
    if(size > 0):
        i = 0
        while i < size:
            print("#" * size)
            i += 1
    else:
        print("You entered negative number or zero")
Hash_Square(5)