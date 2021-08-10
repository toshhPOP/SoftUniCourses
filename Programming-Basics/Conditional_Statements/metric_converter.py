number = float(input())
first_metric = input()
second_metric = input()
result = 0
if first_metric == "mm" and second_metric == "m":
    result = number / 1000
elif first_metric == "mm" and second_metric == "cm":
    result = number / 10
if first_metric == "cm" and second_metric == "m":
    result = number / 100
elif first_metric == "cm" and second_metric == "mm":
    result = number * 10
if first_metric == "m" and second_metric == "mm":
    result = number * 1000
elif first_metric == "m" and second_metric == "cm":
    result = number * 100
print(f"{result:.3f}")
