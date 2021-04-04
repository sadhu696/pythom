s = input()
cnt = 1
i = 0
j = i+1
res = ''

while i < len(s):
    if len(s) == 1:
        res += s[i] + "1"
        break
    while s[i] == s[j]:
        if j == len(s)-1:
            cnt += 1
            break
        cnt += 1
        j += 1
    res += s[i]+str(cnt)
    i += cnt
    j = i+1
    cnt = 1
    if i == len(s)-1:
        res += s[i] + "1"
        break
print(res)