import re

pattern = r"(^|(?<=\s))-?\d+(\.\d+)?($|(?=\s))"

text = input()
valid_numbers = re.finditer(pattern, text)
valid_numbers = [num.group() for num in valid_numbers]
print(*valid_numbers)
