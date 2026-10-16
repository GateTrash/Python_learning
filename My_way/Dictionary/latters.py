text = input()
storage = {}
for latter in text:
    if latter in storage:
        storage[latter] += 1 
    else:
        storage[latter] = 1
    print(latter, end= ":")
    print(storage[latter])