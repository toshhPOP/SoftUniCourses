number = int(input())
positive_list = []
negative_list = []
for i in range(1, number + 1):
    num = int(input())
    if num > 0:
        positive_list.append(num)
    elif num < 0:
        negative_list.append(num)
print(f"{positive_list}\n{negative_list}\nCount of positives: {len(positive_list)}. Sum of negatives: {sum(negative_list)}")
