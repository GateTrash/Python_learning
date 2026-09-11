first_word = input("Enter the first word: ")
second_word = input("Enter the second word: ")
if first_word > second_word:
    print(f"{first_word} is the last one in alphabetical order")
elif second_word > first_word:
    print(f"{second_word} is the last one in alphabetical order")
else:
    print("You enter identical words")