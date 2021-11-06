text = input()
times = input()
try:
    print(int(times) * text)
except ValueError:
    print("Variable times must be an integer")
