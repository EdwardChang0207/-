n, D = map(int, input().split())
p = list(map(int,input().split()))
x = p[0]#t[0]買進
k = 1
result = 0
for y in p[1:]:
    if k: #持有股票
        if y >= x+D: #賣出
            result += y-x
            x = y
            k = 0
    else:
        if y <= x-D: #買進
            x = y
            k = 1
print(result)