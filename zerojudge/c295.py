N, M = map(int, input().split())
l = [list(map(int,input().split())) for i in range(N)]
num = []
ans = []
s = 0

for i in l:
    s += max(i)
    num.append(max(i))

print(s)

for i in num:
    if s % i == 0:
        ans.append(i)

if ans:
    print(*ans)
else:
    print(-1)