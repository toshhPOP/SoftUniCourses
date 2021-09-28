numbers = list(map(lambda x: int(x), input().split(" ")))
remover = [numbers.remove(min(numbers)) for _ in range(int(input()))]
print(numbers)
