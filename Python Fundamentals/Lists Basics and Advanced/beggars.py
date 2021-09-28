numbers = list(map(lambda x: int(x), input().split(",")))
beggars = int(input())
beggars_list = [0] * beggars


for i in range(len(numbers)):
    if i == 0:
        beggars_list[0] = numbers[0]
    else:
        element = numbers[i]
        beggar_index = i % beggars
        beggars_list[beggar_index] += element
print(beggars_list)