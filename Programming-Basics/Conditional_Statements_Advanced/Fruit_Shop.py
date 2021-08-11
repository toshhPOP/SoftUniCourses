fruit = input()
day_of_week = input()
quantity = float(input())
if not day_of_week in ("Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday"):
    print("error")
    exit()
if day_of_week in ("Monday, Tuesday, Wednesday, Thursday, Friday"):
    if fruit == "banana":
        price = quantity * 2.50
    elif fruit == "apple":
        price = quantity * 1.20
    elif fruit == "orange":
        price = quantity * 0.85
    elif fruit == 'grapefruit':
        price = quantity * 1.45
    elif fruit == "kiwi":
        price = quantity * 2.7
    elif fruit == "pineapple":
        price = quantity * 5.50
    elif fruit == "grapes":
        price = quantity * 3.85
    else:
        print('error')
        exit()
    print(f"{price:.2f}")
    exit()
if day_of_week in ("Saturday, Sunday"):
    if fruit == "banana":
        price = quantity * 2.70
    elif fruit == "apple":
        price = quantity * 1.25
    elif fruit == "orange":
        price = quantity * 0.9
    elif fruit == 'grapefruit':
        price = quantity * 1.60
    elif fruit == "kiwi":
        price = quantity * 3
    elif fruit == "pineapple":
        price = quantity * 5.60
    elif fruit == "grapes":
        price = quantity * 4.20
    else:
        print('error')
        exit()
    print(f"{price:.2f}")
    exit()
