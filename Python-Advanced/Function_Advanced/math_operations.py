from collections import deque


def math_operations(*args, **math_dict):
    args = deque(args)
    while args:
        for key in math_dict:
            if args:
                el = args.popleft()
                if key == 'a':
                    math_dict[key] += el
                elif key == 's':
                    math_dict[key] -= el
                elif key == 'd':
                    if not el == 0:
                        math_dict[key] /= float(el)
                    else:
                        zero_division = True
                        if zero_division:
                            continue
                elif key == 'm':
                    math_dict[key] *= el
    return math_dict


print(math_operations(2, 12, 0, -3, 6, -20, -11, a=1, s=7, d=33, m=15))
# print(math_operations(-1, 0, 1, 0, 6, -2, 80, a=0, s=0, d=0, m=0))
# print(math_operations(6, a=0, s=0, d=0, m=0))
