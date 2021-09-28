string = input()
dictionary = {}
for char in string:
    if char not in dictionary and char != " ":
        dictionary[char] = 0
    if char != " ":
        dictionary[char] += 1
for key, value in dictionary.items():
    print(f"{key} -> {value}")