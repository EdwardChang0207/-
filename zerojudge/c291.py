n = int(input())
f = list(map(int, input().split()))
visit = [False for i in range(n)]
group = 0
for i in range(n):
    if not visit[i]: #節點尚未被拜訪
        visit[i] = True
        now = f[i]
        while i != now:
            visit[now] = True
            now = f[now]
        group += 1
print(group)