# word = input("Enter a word bigger 3 latters: ")
# second_last_index = len(word) - 2
# if word[1] == word[second_last_index]:
#     print(f"second and last second latters the came and equal {word[1]}")
# else:
#     print("second and last second latters different")

# word = input("Enter a word: ")
# a_in_word = bool("a" in word)
# result = ""
# if a_in_word == True:
#     result +="a found"
# else:
#     result +="a not found"   
# a_in_word = bool("o" in word)
# if a_in_word == True:
#     result +=" o found"
# else:
#     result +=" o not found" 
# a_in_word = bool("e" in word)
# if a_in_word == True:
#     result +=" e found"
# else:
#     result +=" e not found" 
# print(result)
string = input("Please, enter the string at 3 symbols: ")
symbol = input("Please, enter the symbol out start ")
index = string.find(symbol) + 1
if index != -1 and len(string) > index + 2:
    while len(symbol) < 3:
        symbol += string[index]
        index += 1
    print(symbol)
elif len(string) < index + 2:
    print("index out of range")
else:
    print("Exeption symbol not found")