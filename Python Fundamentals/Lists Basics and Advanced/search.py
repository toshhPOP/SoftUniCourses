number = int(input())
word = input()
list = [input() for i in range(number)]
print(list)
for j in range(len(list) -1, -1,-1):
    element = list[j]
    if not word in element:
        list.remove(element)
print(list)




