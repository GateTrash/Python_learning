def squared (string, size):
    row = 0
    index = 0
    if size > 0 :
        while row < size:
            k = 0
            while k < size:
                if index > len(string) - 1:
                    index = 0
                    print(string[index], end="")
                    index += 1
                else :
                    print(string[index], end="")
                    index += 1 
                k += 1
            row += 1
            print()
    elif len(string) == 0:
        print("String cannot be empty")
    else:
        print("You enter negative number or zero")

squared("ad", 4)