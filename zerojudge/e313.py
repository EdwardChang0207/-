n = int(input())
s = [] #string
result = []

for i in range(n):
    s.append(input())
s.sort()

for str in s:
    a = []
    r = 0
    for j in str:
        if j not in a:
            r += 1
            a.append(j)
    result.append(r)

print(s[result.index(min(result))])
