import sys
from io import StringIO

test_input = '''
7
Peter 5.20
Mark 5.50
Peter 3.20
Mark 2.50
Alex 2.00
Mark 3.46
Alex 3.00
'''
num = int(input())
sys.stdin = StringIO(test_input)
students = {}
for _ in range(num):
    name, grade_string = input().split(' ')
    grade = float(grade_string)

    if name not in students:
        students[name] = []
    students[name].append(grade)

for name, grades in students.items():
    average_grade = sum(grades)/len(grades)
    print(f"{name} -> {' '.join(str(f'{a:.2f}') for a in grades)} (avg: {average_grade:.2f})")