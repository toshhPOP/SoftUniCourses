from collections import deque


def best_list_pureness(nums, k):
    data = {}
    nums = deque(nums)
    for rotation in range(k + 1):
        result = sum([index * number for index, number in enumerate(nums)])
        data.update({rotation: result})
        nums.rotate(1)
    max_pureness = max(data.values())
    for key, value in data.items():
        if max_pureness == value:
            return f"Best pureness {value} after {key} rotations"

test = (('what',4, 3, 2, 6), 4)
result = best_list_pureness(*test)
print(result)

test = ([7, 9, 2, 5, 3, 4], 3)
result = best_list_pureness(*test)
print(result)

test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)
