student = {
    "name": "Alex",
    "age": 17,
    "grade": 85
}
print(student["name"])
student["age"] += 1
student["grade"] = 90
student["city"] = "Tallinn"
for key in student:
    print(student[key])