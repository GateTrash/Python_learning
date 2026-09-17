word = input("Please, enter word: ")
substring = input("Please, enter substring: ")
index = word.find(substring)
substring_cut = word[index + len(substring): len(word)]
print(substring_cut)
seek_index = substring_cut.find(substring) + len(word[0:index+len(substring)])
print(seek_index)
if(index != -1):
    if(seek_index >= 1):
        print(f"the second substring is located on index {seek_index}")
    else:
        print("the second substring not found")
else:
    print("substing not found")