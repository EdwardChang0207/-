t = int(input())
for i in range(t):
    a = list(map(int,input().split()))
    if a[1]-a[0] == a[2]-a[1]:
        a.append(a[3]+(a[1]-a[0]))
    if a[1]/a[0] == a[2]/a[1]:
        a.append(a[3]*int(a[1]/a[0]))

    print(*a) #*a -> a[0], a[1], ..., a[n]