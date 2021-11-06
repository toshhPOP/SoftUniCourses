def operate(operator, *args):
    if operator == '+':
        result = 0
        for i in range(len(args)):
            result += args[i]
        return result

    elif operator == '-':
        result = args[0]
        for i in args[1:]:
            result -= i
        return result

    elif operator == '*':
        result = 1
        for i in args:
            result *= int(i)
        return result
    elif operator == '/':
        result = args[0]
        for i in args[1:]:
            if int(i) != 0:
                result /= int(i)
        return result