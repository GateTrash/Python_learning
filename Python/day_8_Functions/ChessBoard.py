def Chessboard(size): 
    if size > 0:
        i = 0
        k = 0
        is_zero = True
        while i < size:
            k = 0
            while k < size:
                if is_zero == False:
                    print(0, end="")
                    is_zero = True
                else :
                    print(1, end="")
                    is_zero = False
                k += 1
            i += 1
            print()
    else:
        print("You enter negative number or zero")
Chessboard(5)