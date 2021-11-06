def even_odd(command, args):
    if command == 'Even':
        result = sum((list(filter(lambda x: (int(x) % 2 == 0), args))))
        result *= len(nums)
    elif command == 'Odd':
        result = sum((list(filter(lambda x: (int(x) % 2 != 0), args))))
        result *= len(nums)
    return result


def value(command):
    result = even_odd(command, nums)
    return result


command = input()
nums = [int(x) for x in input().split()]

print(value(command))
