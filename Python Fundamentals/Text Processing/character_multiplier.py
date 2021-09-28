strings = input().split()
total_sum = 0
first = strings[0]
second = strings[1]
remaining = ''
if len(first) > len(second):
    remaining = first[len(second):]
    first = first[:len(second)]
elif len(second)> len(first):
    remaining = second[len(first):]
    second = second[:len(first)]
for i in range(len(first)):
    total_sum += ord(first[i]) * ord(second[i])
for a in range(len(remaining)):
    total_sum += ord(remaining[a])
print(total_sum)