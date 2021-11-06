nums = [int(x) for x in input().split()]
first = nums[0]
second = nums[1]
set1 = set()
set2 = set()
for i in range(first):
    set1.add(int(input()))
for _ in range(second):
    set2.add(int(input()))
[print(a) for a in (set1 & set2)]
'''
first, second = input().split()
set1 = set(int(input()) for x in range(int(first)))
set2 = set(int(input()) for a in range(int(second)))
[print(a) for a in (set1 & set2)]
'''
