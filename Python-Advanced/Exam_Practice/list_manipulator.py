def list_manipulator(nums, *args):
    action = args[0]
    range = args[1]
    if action == 'add':
        additional = args[2:]
        if range == 'beginning':
            for i in additional[::-1]:
                nums.insert(0, i)
        elif range == 'end':
            for i in additional:
                nums.append(i)
    if action == 'remove':
        if range == 'beginning':
            if len(args) > 2:
                nums = nums[int(args[-1]):]
            else:
                nums = nums[1:]
        elif range == 'end':
            if len(args) > 2:
                nums = nums[:len(nums)-args[-1]]
            else:
                nums = nums[:-1]
    return nums

print(list_manipulator([1,2,3], "remove", "end"))
print(list_manipulator([1,2,3], "remove", "beginning"))
print(list_manipulator([1,2,3], "add", "beginning", 20))
print(list_manipulator([1,2,3], "add", "end", 30))
print(list_manipulator([1,2,3], "remove", "end", 2))
print(list_manipulator([1,2,3], "remove", "beginning", 2))
print(list_manipulator([1,2,3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1,2,3], "add", "end", 30, 40, 50))
