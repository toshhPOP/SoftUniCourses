divisor = int(input())
bound = int(input())
greatest = 0
for n in range(bound, 0, -1):
    if n % divisor == 0 and n <= bound:
        print(n)
        break


# divisor = int(input())
# bound = int(input())
# max = 0
# for i in range(divisor,bound+1):
#     if i % divisor == 0:
#         if i > max:
#             max = i
# print(max)