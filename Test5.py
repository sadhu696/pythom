s = int(input())
res = s

if 100 <= s <= 1000:
    s = s%100
if s == 0 or 5 <= s <= 20 or 5 <= s%10 <= 9 or s%10 == 0:
    print(res, 'программистов')
elif s == 1 or (s > 20 and s%10 == 1):
    print(res, 'программист')
elif 2 <= s <= 4 or (s > 20 and 2 <= s%10 <=4):
    print(res, 'программиста')