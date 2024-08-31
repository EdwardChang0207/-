n = int(input())
a = list(map(int, input().split()))
s = 0

for i in range(len(a)):
    if a[i] == 0:
        if i == 0:#1st
            s += a[1]
        elif i == len(a)-1:#last one
            s += a[-2]
        else:
            s += min(a[i+1], a[i-1])

print(s)