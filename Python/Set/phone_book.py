# - Удали полностью одинаковые записи. +
# - Найди множество уникальных имён. +
# - Найди имена, у которых записано больше одного номера. +
# - Выведи все уникальные записи в виде кортежей. +
# Важно: записи ("Maria", "222") и ("Maria", "444") должны считаться разными контактными записями, хотя имя одинаковое.
contacts = [
    ("Alex", "111"),
    ("Maria", "222"),
    ("Alex", "111"),
    ("John", "333"),
    ("Maria", "444"),
    ("John", "333")
]
phone_book = set(contacts)
names = set()
print(f"phone Book: {phone_book}")
repeat_names = set()
for item in phone_book:
    if item[0] in names:
        repeat_names.add(item[0])
    names.add(item[0])
print(f"All names: {tuple(names)}")
print(f"Names that have more one number: {tuple(repeat_names)}")
