word = input("Please, enter the word: ")
if(word != "" or word != " "):
    a = len(word) -1
    b = len(word)
    while a > -1 :
        print(word[a:b])
        a -= 1
else:
    print("You write empty string")