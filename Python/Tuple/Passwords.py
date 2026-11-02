# Найди все уникальные пары (имя, пароль). +
# Найди множество всех использованных паролей. +
# Определи, сколько разных паролей использовалось. +
# Найди пароли, которые использовали несколько разных пользователей.+
# Найди пользователей, чьи записи повторяются полностью.+
list_passwords= [
    ("Alex", "python123"),
    ("Maria", "qwerty"),
    ("John", "python123"),
    ("Kate", "hello123"),
    ("Tom", "qwerty"),
    ("Alex", "python123")
]
users = [] #список без повторений
passwords = set() 
repeat_passwords = [] #одинаковые пароли
repeat_users = [] #Одинаковые пользователи/повторяющиеся записи
for item in list_passwords:
    if item[1] in passwords and item[1] not in repeat_passwords: 
        repeat_passwords.append(item[1])
    if item not in users: 
        users.append(item)
    elif item in users:
        repeat_users.append(item[0])

    passwords.add(item[1])
print(f"Unique couples: {users}")
print(f"All passwords: {passwords}, amount: {len(passwords)}")
print(f"Repeat passwords: {repeat_passwords}")
print(f"Repeat whrites users: {repeat_users}")