first = {int(x) for x in input().split()}
second = {int(x) for x in input().split()}
n = int(input())
for i in range(n):
    action, collection, *content = input().split()
    if action == "Add" and collection == "First":
        content = set(int(a) for a in content)
        first = (first | content)
    elif action == "Add" and collection == 'Second':
        content = set(int(a) for a in content)
        second = (second | content)
    elif action == "Remove":
        if collection == "First":
            content = set(int(a) for a in content)
            first -= content
        elif collection == "Second":
            content = set(int(a) for a in content)
            second -= content
    elif action == "Check":
        if first.issubset(second) or second.issubset(first):
            print("True")
        else:
            print("False")
print(', '.join(str(a) for a in sorted(first)))
print(', '.join(str(a) for a in sorted(second)))
