n = int(input())
r = []
for i in range(2, n+1):
    while n % i == 0:
        r.append(i)
        n = int(n/i)
        print(n)
        print(r)

now = -1
for i in r:
    if now != i:
        now = i
        a = r.count(i)
        if a > 2: 
            print("%d^%d"%(i, a), end=' ')
        else:
            print(i, end=' ')
        if i == r[-1]: break
        print('*', end= ' ')