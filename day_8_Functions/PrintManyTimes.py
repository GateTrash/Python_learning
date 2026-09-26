def ManyPrint (string, times):
    i = 0
    if times > 0:
        while i < times:
            print(string)
            i += 1
    else:
        print("You enter negative number or zero")
ManyPrint("I like Python!", 0)