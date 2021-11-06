numbers = [0, 1]


def create_sequence(n):
    global numbers
    for i in range(2, n):
        numbers.append(numbers[i - 1] + numbers[i - 2])
    return numbers


def locate(x):
    if x not in numbers:
        raise IndexError(f"The number {x} is not in the sequence")
    else:
        return numbers.index(x)
