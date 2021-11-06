def even_odd(*args):
    command = args[-1]
    if command == 'even':
        num_list = [int(x) for x in args[:-1] if int(x) % 2 == 0]
    else:
        num_list = [int(x) for x in args[:-1] if int(x) % 2 != 0]
    return num_list
print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))