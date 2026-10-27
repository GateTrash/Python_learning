contacts = {"alex": "12345","maria": "67890","john": "54321"}
while True:    
    name = input("Please, enter name: ").strip().lower()
    if len(name.strip()) == 0:
        print("Cannot be empty")
        continue
    if name in contacts:
        print(f"current phone number: {contacts[name]}")
        command = input("Do you want сhange phone number? yes(y); no(n) ").strip().lower()
        if command == "y":
            contacts[name] = input("Enter phone number: ")
        elif command != "n": print("Unknow command")
    else:
        command = input("This name not found, do you want add new contact? yes(y); no(n) ").strip().lower()
        if command == "y":
            contacts[name] = input("Enter phone number: ")
            print("Great job, new contact add!")
        elif command != "n": print("unknow command")
    command = input("Do you want to continue? yes(y); no(n) ").strip().lower()
    if command == "n":
        break
    elif command != "y":
        print("unkow command")