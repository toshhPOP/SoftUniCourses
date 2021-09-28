n1 = int(input())
n2 = int(input())
list = []
for i in range(n1,n2*n1+1):
    if i % n1 == 0:
        list.append(i)
print(list)



