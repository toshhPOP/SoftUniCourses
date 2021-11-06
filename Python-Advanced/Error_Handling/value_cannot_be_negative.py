class ValueCannotBeNegative(Exception):
    pass


for num in range(5):
    x = int(input())
    if x < 0:
        raise ValueCannotBeNegative
