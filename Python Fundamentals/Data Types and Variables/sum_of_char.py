n = int(input())
summ = 0
for i in range(1, n + 1):
    letter = input()
    summ += ord(letter)
print(f"The sum equals: {summ}")
