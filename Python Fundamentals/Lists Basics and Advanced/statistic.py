num = int(input())
positive = 0
l1 = []
l2 = []
for i in range(num):
    counter = int(input())
    if counter > 0:
        l1.append(counter)
    else:
        l2.append(counter)
print(l1)
print(l2)
print(f'Count of positives: {len(l1)}. Sum of negatives: {sum(l2)}')