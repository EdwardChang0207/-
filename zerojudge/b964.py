n = input()
s = list(map(int, input().split()))

s.sort()
print(*s)

#case1 : best case
if s[0] >= 60:
    print('best case')
    print(s[0])
#case2 : worst case
elif s[-1] < 60:
    print(s[-1])
    print('worst case')
#case3 : both
else:
    for i in range(len(s)):
        if s[i] >= 60:
            print(s[i-1])
            print(s[i])
            break