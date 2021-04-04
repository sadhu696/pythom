lst = [int(i) for i in input().split()]
res = []
cnt = 1
i = int(0)
lst.sort()
if len(lst) == 1:
    lst = lst
while i < len(lst):
    j = i+1
    if i >= len(lst) - 1:
        break
    while j < len(lst):
        if lst[i] == lst[j]:
            cnt += 1
            j += 1
        else:
            break
    if cnt > 1:
       res.append(lst[i])
    i += cnt
    cnt = 1
print(*res)



