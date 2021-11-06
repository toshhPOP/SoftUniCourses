

# Version 1
def numbers_searching(*numbers):
    final = []
    duplicate = []
    for i in range(min(numbers), max(numbers) + 1):
        if i not in numbers:
            final.append(i)
        if numbers.count(i) > 1:
            numbers = list(filter(lambda x: x != i, numbers))
            duplicate.append(i)
    final.append(sorted(duplicate, reverse=False))
    return final

# Version 2
# def numbers_searching(*numbers):
#     missing = int(''.join([str(a) for a in range(min(numbers), max(numbers) + 1) if a not in numbers]))
#     duplicate = sorted(list(set([x for x in numbers if numbers.count(x) > 1])))
#     return [missing, duplicate]
print(numbers_searching(1, 2, 4, 2, 5, 4))
print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))
print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))
