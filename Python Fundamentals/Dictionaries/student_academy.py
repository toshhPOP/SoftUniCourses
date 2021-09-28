number = int(input())
students_dictionary = {}
for i in range(number):
    student_name = input()
    grade = float(input())
    if not student_name in students_dictionary:
        students_dictionary[student_name] = []
    students_dictionary[student_name].append(grade)

for key, value in students_dictionary.items():
    students_dictionary[key] = sum(value) / len(value)

students_dictionary = sorted(students_dictionary.items(), key=lambda x: -x[1])
for name, grade in students_dictionary:
    if grade >= 4.50:
        print(f"{name} -> {grade:.2f}")
