#Varian 1
tasks = [int(x) for x in input().split(', ')]

searched_index = int(input())
executed_task = 0
cycles = sorted([(tasks[index], index) for index in range(len(tasks))])
for el in cycles:
    if el[1] == searched_index:
        executed_task += el[0]
        break
    executed_task += el[0]
print(executed_task)

#Variant 2
# from collections import deque
#
# tasks = [int(x) for x in input().split(', ')]
#
# searched_index = int(input())
# executed_task = 0
# cycles = deque(sorted([(tasks[index], index) for index in range(len(tasks))]))
# while cycles:
#     number, index = cycles.popleft()
#     executed_task += number
#     if index == searched_index:
#         print(executed_task)
#         break