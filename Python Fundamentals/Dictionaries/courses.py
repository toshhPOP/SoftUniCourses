courses = {}
while True:
    command = input()
    if command == "end":
        break
    course_name, student = command.split(" : ")
    if course_name not in courses:
        courses[course_name] = []
    courses[course_name].append(student)
courses = sorted(courses.items(), key=lambda x: -(len(x[1])))
for course, students in courses:
    print(f"{course}: {len(students)}")
    for s in sorted(students):
        print(f"-- {s}")
