n = int(input())
a = [list(map(int,input().split())) for i in range(n)]
b = []
for i in range(n-1):
    b.append(abs(a[i][0]-a[i+1][0])+abs(a[i][1]-a[i+1][1]))

print(max(b),min(b))