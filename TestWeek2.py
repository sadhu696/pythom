a = int(input())
i = 1
cnt = 0
while cnt < a:
    for j in range(i):
        if cnt >= a:
            break
        print(i, end=' ')
        cnt += 1
    i += 1