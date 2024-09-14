a = list(map(int,input().split()))
a.sort()
b = []
for i in a:
    if i not in b:
        b.append(i)
print(max([a.count(i) for i in b]), end=' ')
b.reverse()
print(*b)