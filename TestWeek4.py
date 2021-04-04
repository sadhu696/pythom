lst = []
while 1 == 1:
    b = ''
    a = [i for i in input().split()]
    for i in range(len(a)):
        b += str(a[i])
    if b == 'end':
        break
    else:
        lst.append(a)
st = len(lst)
col = len(lst[0])
res = [[0 for i in range(col)] for j in range(st)]
if st == 1 and col == 1:
    res[0][0] = int(lst[0][0])*4
elif st == 1 and col == 2:
    res[0][0] = 4*int(lst[0][1])
    res[0][1] = 4*int(lst[0][0])
elif st == 2 and col == 1:
    res[0][0] = 4*int(lst[1][0])
    res[1][0] = 4*int(lst[0][0])
elif st == 1 and col > 1:
    for i in range(col):
        if i == 0:
            res[0][i] = int(lst[0][-1]) + int(lst[0][i + 1]) + 2 * int(lst[0][i])
        if i == col-1:
            res[0][i] = int(lst[0][-2]) + int(lst[0][0]) + 2 * int(lst[0][i])
        else:
            res[0][i] = int(lst[0][i-1]) + int(lst[0][i+1]) + 2*int(lst[0][i])
elif st > 1 and col == 1:
    for i in range(st):
        if i == 0:
            res[i][0] = int(lst[-1][0]) + int(lst[i+1][0]) + 2 * int(lst[i][0])
        if i == st-1:
            res[i][0] = int(lst[-2][0]) + int(lst[0][0]) + 2 * int(lst[i][0])
        else:
            res[i][0] = int(lst[i-1][0]) + int(lst[i+1][0]) + 2*int(lst[i][0])
else:
    for i in range(st):
        for j in range(col):
            if i == 0 and j == 0:
                res[i][j] = int(lst[-1][j]) + int(lst[i + 1][j]) + int(lst[i][-1]) + int(lst[i][j + 1])
            elif i == 0 and 0 < j < col-1:
                res[i][j] = int(lst[-1][j]) + int(lst[i + 1][j]) + int(lst[i][j - 1]) + int(lst[i][j + 1])
            elif i == 0 and j == col-1:
                res[i][j] = int(lst[-1][j]) + int(lst[i + 1][j]) + int(lst[i][j - 1]) + int(lst[i][0])
            elif i == st-1 and j == 0:
                res[i][j] = int(lst[i-1][j]) + int(lst[0][j]) + int(lst[i][-1]) + int(lst[i][j + 1])
            elif i == st - 1 and 0 < j < col-1:
                res[i][j] = int(lst[i-1][j]) + int(lst[0][j]) + int(lst[i][j - 1]) + int(lst[i][j + 1])
            elif i == st - 1 and j == col-1:
                res[i][j] = int(lst[i-1][j]) + int(lst[0][j]) + int(lst[i][j - 1]) + int(lst[i][0])
            elif 0 < i < st-1 and j == 0:
                res[i][j] = int(lst[i - 1][j]) + int(lst[i + 1][j]) + int(lst[i][-1]) + int(lst[i][j + 1])
            elif 0 < i < st-1 and j == col-1:
                res[i][j] = int(lst[i - 1][j]) + int(lst[i+1][j]) + int(lst[i][j - 1]) + int(lst[i][0])
            else:
                res[i][j] = int(lst[i-1][j]) + int(lst[i+1][j]) + int(lst[i][j-1]) + int(lst[i][j+1])
for i in range(len(lst)):
    for j in range(len(lst[0])):
        print(res[i][j], end=" ")
    print()

