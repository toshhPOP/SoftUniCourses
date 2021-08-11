number1 = int(input())
number2 = int(input())
operator = input()
if operator == "+":
    result = number1 + number2
elif operator == "-":
    result = number1 - number2
elif operator == "*":
    result = number1 * number2
elif operator == "/":
    if number2 == 0:
        print(f"Cannot divide {number1} by zero")
        exit()
    result = number1 / number2
elif operator == "%":
    if number2 == 0:
        print(f"Cannot divide {number1} by zero")
        exit()
    result = number1 % number2
if operator in ("+, -, *"):
    if result % 2 == 0:
        print(f"{number1} {operator} {number2} = {result} - even")
    else:
        print(f"{number1} {operator} {number2} = {result} - odd")
elif operator == "/":
    print(f"{number1} / {number2} = {result:.2f}")
elif operator == "%":
    print(f"{number1} % {number2} = {result}")
