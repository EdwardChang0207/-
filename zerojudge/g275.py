n = int(input())
for i in range(n):
    a = list(map(int, input().split()))
    b = list(map(int, input().split())) 
    result = ''
    #A
    if (a[1] == a[3]) or (b[1] == b[3]) or (a[1] != a[5]) or (b[1] != b[5]):
        result += 'A'
    #B
    if (a[-1] != 1) or (b[-1] != 0):
        result += 'B'
    #C
    if (a[1] == b[1]) or (a[3] == b[3]) or (a[5] == b[5]):
        result += 'C'

    if result: print(result)
    else: print('None')
