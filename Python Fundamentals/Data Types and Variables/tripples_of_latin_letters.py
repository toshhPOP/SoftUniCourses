number = int(input())
for i in range(number):
    for k in range(number):
        for m in range(number):
            print(f"{chr(i+97)}{chr(k+97)}{chr(m + 97)}")
