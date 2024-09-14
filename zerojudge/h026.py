F = input()
N = int(input())
a = input().split()
b = []

for i in range(N):
    b.append(F)

    if a[i] == '0':
        if F == '2':
            print(*b, end=' ')
            print(': Lost at round', i+1)
            break
        elif F == '5':
            print(*b, end=' ')
            print(': Won at round', i+1)
            break

    elif a[i] == '2':
        if F == '0':
            print(*b, end=' ')
            print(': Won at round', i+1)
            break
        elif F == '5':
            print(*b, end=' ')
            print(': Lost at round', i+1)
            break

    else: #i == '5'
        if F == '0':
            print(*b, end=' ')
            print(': Lost at round', i+1)
            break
        elif F == '2':
            print(*b, end=' ')
            print(': Won at round', i+1)
            break

    if i != 0:
        if a[i] == a[i-1]:
            if a[i] == '0':
                F = '5'
            elif a[i] == '2':
                F = '0'
            else: #a[i] == 5
                F = '2'
        else:
            F = a[i]
    else:
        F = a[i]

    if i == N-1:
        print(*b, end=' ')
        print(': Drew at round', N)