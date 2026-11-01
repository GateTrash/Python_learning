# Найди количество уникальных точек. +
# Создай множество уникальных точек. +
# Найди все точки, у которых x > y. +
# Добавь новую точку (3, 8). +
# Проверь, встречается ли точка (2, 3) в исходных данных. +
#____________________________________
points = [(2, 3),(5, 1),(2, 3),(4, 6),(5, 1),(7, 2)]
unique_points = set()
x_grather_y= set()
points.append((3,8))
for item in points:
    unique_points.add(item)   
    if item[0] > item[1]:
        x_grather_y.add(item)
print(f"amount of unique points: {len(unique_points)}")
if (2,3) in points:
    print("element found!")
else:
    print("not found")
#______________________________
# - Найди предметы, которые изучают все трое. +
# - Найди все предметы, которые изучает хотя бы один ученик. + 
# - Найди предметы, которые изучает только Алекс. +
# - Найди предметы, которые изучают Алекс и Мария, но не Джон. +
# Ограничение: для вычислений используй множества, а исходные кортежи оставь без изменений.
alex = ("Math", "Python", "English", "Physics")
maria = ("English", "Python", "Biology")
john = ("Math", "English", "History", "Python")
alex_set = set(alex)
maria_set = set(maria)
john_set = set(john)
print(f"equal hobbies: {alex_set & maria_set & john_set}")
print(f"unique hobbies: {alex_set | maria_set | john_set}")
print(f"Alex only learn: {alex_set - (maria_set | john_set)}")
print(f"both hobbies alex and maria: {(alex_set & maria_set) - john_set}")
