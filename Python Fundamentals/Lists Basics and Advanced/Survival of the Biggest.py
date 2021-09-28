collection = input().split()
number = int(input())
new = []
index = 0
for i in collection:
    new.append(int(i))
for k in range(number):
    new.remove(min(new))
    len(new)
for _ in new:
    index += 1
    if index == len(new):
        print(f"{_}", end="")
    else:
        print(f"{_}",end=", ")
