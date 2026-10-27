word = input("Please, enter word: ")
count = 30 - len(word)
empty = "*" * ( count // 2)
print(empty + word + empty)