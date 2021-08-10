from math import pi
figure = input()
area = 0
if figure == "square":
    side = float(input())
    area = side*side
elif figure == "rectangle":
    a = float(input())
    b = float(input())
    area = a * b
elif figure == "circle":
    r = float(input())
    area = pi*(r*r)
elif figure == "triangle":
    a = float(input())
    h = float(input())
    area = a*h/2
print(f'{area:.3f}')