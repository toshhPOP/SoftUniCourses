from collections import deque

expression = deque(input().split())
numbers = deque()

while len(expression) >= 1:
    current = expression.popleft()
    if current not in ("*", "+", "-", "/"):
        numbers.append(int(current))
        if len(expression) == 0:
            break
    else:
        if current == "*":
            result = numbers.popleft()
            while numbers:
                result *= numbers.popleft()
            expression.appendleft(result)
        elif current == "-":
            result = numbers.popleft()
            while numbers:
                result -= numbers.popleft()
            expression.appendleft(result)
        elif current == "+":
            result = numbers.popleft()
            while numbers:
                result += numbers.popleft()
            expression.appendleft(result)
        elif current == "/":
            result = numbers.popleft()
            while numbers:
                result /= numbers.popleft()
            expression.appendleft(result)
print(''.join(str(a) for a in numbers))
