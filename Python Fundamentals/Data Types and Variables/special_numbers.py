num = int(input())
for i in range(1, num + 1):
    is_special = False
    summ = 0
    for k in str(i):
        summ += int(k)
        if summ == 5 or summ == 7 or summ == 11:
            is_special = True
    if is_special:
        print(f"{i} -> True")
    else:
        print(f"{i} -> False")
