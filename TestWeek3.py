lst = [int(i) for i in input().split()]
x = int(input())
for i in range(len(lst)):
    if lst[i] == x:
        print(i, end=" ")
if lst.count(x) == 0:
    print('Отсутствует')