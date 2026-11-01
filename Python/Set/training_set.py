# Выведи тех, кто пришёл. +
# Найди тех, кто зарегистрирован, но не пришёл. +
# Проверь, все ли пришедшие были зарегистрированы.+
# Найди количество отсутствующих. +
# Дополнительное условие: программа должна работать с любыми двумя такими множествами.
#_________________________________
# registered = {"Alex", "Maria", "John", "Kate", "Tom"}
# arrived = {"Maria", "Kate", "Tom"}
# print("Arrived:", arrived)
# print(f"Registered but failed to arrive guests: {registered - arrived}")
# print(f"All arrivals registered: {arrived.issubset(registered)}")
# print(f"Not registered arivers: {arrived - registered}")
# print(f"Amount of absent guests: {len(registered - arrived)}")
#____________________________________
numbers = [4, 2, 4, 7, 2, 9, 7, 1, 4]
sort_numbers = []
seen = set()
for item in numbers:
    if item not in seen:
        seen.add(item)
        sort_numbers.append(item)
print(sort_numbers)