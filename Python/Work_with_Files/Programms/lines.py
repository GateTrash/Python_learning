with open("Work_with_Files/files/note.txt", "r", encoding="utf-8") as file:
    text = file.read()
    words = text.split()
    print(f"Words: {words}; Amount: {len(words)}")