lst = [int(i) for i in input().split()]
res = []
if len(lst) == 1:
    print(lst[0])
else:
    for i in range(len(lst)):
        if (i-1) < 0:
            res.append(lst[1] + lst[-1])
        elif (i+1) == len(lst):
            res.append(lst[i-1] + lst[0])
        else:
            res.append(lst[i-1] + lst[i+1])
for i in range(len(res)):
    print(res[i], end=" ")