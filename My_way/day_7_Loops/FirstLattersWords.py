string = input("Please, enter sentence: ")
index = string.find(" ")
substring = string[index+1: len(string)]
word = string[0]
print(word)
if(index != -1):
    while index != -1:
        index = substring.find(" ")
        word = substring[0]
        substring = substring[index+1: len(substring)]
        print(word)
else:
    print("You not entered data")