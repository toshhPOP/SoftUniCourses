age = float(input())
gender = input()
title = ""
if gender == "m":
    if age >= 16:
        title = "Mr."
    elif age < 16:
        title = "Master"
elif gender == 'f':
    if age >= 16:
        title = "Ms."
    elif age < 16:
        title = "Miss"
print(title)