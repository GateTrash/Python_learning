students = {"Alex": [80, 90, 85],"Maria": [95, 100, 92],"John": [60, 70, 75]}
better = ["Alex", 0]
good_studens = []
for student, grade in students.items():
    mean= sum(grade) / len(grade)
    if mean > better[1]:
        better[1] = mean
        better[0] = student 
    print(student, round(mean, 1))
    if mean > 80:
        good_studens.append(student) 
print(f"Better student: {better[0]}")
print("Students are mean grade > 80:")
for student in good_studens:
    print(student)