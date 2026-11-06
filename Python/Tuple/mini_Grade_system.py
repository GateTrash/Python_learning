# 1. Найди уникальные записи об учениках.+
# 2. Найди множество уникальных имён. +
# 3. Найди все уникальные оценки, которые встречаются в данных. +
# 4. Найди учеников, у которых есть оценка 5. +
# 5. Найди учеников с полностью одинаковым набором оценок. +
# 6. Найди оценки, которые встречаются у каждого ученика хотя бы один раз. +
# 7. Посчитай, сколько уникальных записей осталось после удаления повторений.+
# Условие: исходные данные не изменяй. Используй tuple, set, циклы и условия. Не используй сторонние библиотеки. +
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
grades = set()
excellent_students = set()

for item in students_list:
    if item in students:
        repeating.add(item[0])
    if item[0] not in names:
        names.add(item[0])
    if 5 in item[1]: excellent_students.add(item[0])

    for element in item[1]:
        grades.add(element)
    students.add(item)

identical_grades = set(students_list[0][1])
for item in students:
    student_second = set(item[1])
    buffer = set()
    for element in identical_grades:
        if element not in student_second:
            buffer.add(element)
    if len(buffer) > 0:
        for element in buffer:
            identical_grades.discard(element)

print(f"list of students: {students}, amount: {len(students)}")
print(f"list if names: {names}")
print(f"All grades: {grades}")
print(f"Excellent students: {excellent_students}")
print(f"Students repeating set of grades: {repeating}")
print(f"identical grades students at all: {identical_grades}")
