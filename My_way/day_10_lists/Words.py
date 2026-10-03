storage = ""
another_words = 0
while True:
    word = input("Word: ")
    if word in storage:
        break
    else:
        storage += word + " "
        another_words += 1
print(f"Amount another words: {another_words}")
print(storage)