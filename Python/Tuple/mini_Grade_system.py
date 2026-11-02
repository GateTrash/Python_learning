# 1. Найди уникальные записи об учениках.+
# 2. Найди множество уникальных имён.+
# 3. Найди все уникальные оценки, которые встречаются в данных. +
# 4. Найди учеников, у которых есть оценка 5. +
# 5. Найди учеников с полностью одинаковым набором оценок.
# 6. Найди оценки, которые встречаются у каждого ученика хотя бы один раз.
# 7. Посчитай, сколько уникальных записей осталось после удаления повторений.+
# Условие: исходные данные не изменяй. Используй tuple, set, циклы и условия. Не используй сторонние библиотеки.
students_list = [
    ("Alex", (5, 4, 5, 3)),
    ("Maria", (5, 5, 4, 5)),
    ("John", (3, 4, 3, 4)),
    ("Kate", (5, 4, 5, 3)),
    ("Alex", (5, 4, 5, 3))
]
students = set()
names = set()
repeating = set()
unique_grades = set()
excellent_students = set()
for item in students_list:
    if item in students:
        repeating.add(item)
    if item[0] not in names:
        names.add(item[0])
    for element in item[1]:
        unique_grades.add(element)
    if 5 in item[1]: excellent_students.add(item[0])
    students.add(item)
print(f"list of students: {students}, amount: {len(students)}")
print(f"list if names: {names}")
print(f"Unique grades: {unique_grades}")
print(f"Excellent students: {excellent_students}")
print(f"")