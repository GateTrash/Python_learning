# Найди все уникальные пары (имя, пароль).
# Найди множество всех использованных паролей. +
# Определи, сколько разных паролей использовалось. = одинаковые - длинна кортежа паролей
# Найди пароли, которые использовали несколько разных пользователей.
# Найди пользователей, чьи записи повторяются полностью.
list_passwords= [
    ("Alex", "python123"),
    ("Maria", "qwerty"),
    ("John", "python123"),
    ("Kate", "hello123"),
    ("Tom", "qwerty"),
    ("Alex", "python123")
]
users = set(list_passwords)
passwords = set()
repeat_passwords = []
for item in users:
    if item[1] in passwords:
        repeat_passwords.add(item[1])
    passwords.add(item[1])
