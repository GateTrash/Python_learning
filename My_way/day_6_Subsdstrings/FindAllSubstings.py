word = input("Please, enter word: ")
symbol = input("Please, enter symbol: ")
index = word.find(symbol)
substring =""
if (index < len(word)):
    while True:
        if index + 3 < len(word):
            substring += word[index: index + 3] + " "
        else:
            break
        index += 1
    print(substring)
else:
    print("symbol not found")