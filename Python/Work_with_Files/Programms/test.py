with open("Python/Work_with_Files/files/note.txt", "w", encoding= "utf-8") as file:
    file.write("Andrey\n")
    file.write("17 years old\n")
    file.write("Python\n")
with open("Python/Work_with_Files/files/note.txt", "a", encoding= "utf-8") as file:
    file.write("Today I learned Python files.")
with open("Python/Work_with_Files/files/note.txt", "r") as file:
    text = file.read()
    print(text)
