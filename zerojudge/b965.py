R, C, M = map(int,input().split())
B = [list(map(int,input().split())) for i in range(R)]
a = list(map(int,input().split()))

def filp(B):
    B.reverse()
    return B

def rotate(B):
    #R -> C
    A = [ ['' for j in range(len(B))] for i in range(len(B[0]))]

    # A = []
    # for i in range(len(b[0])):
    #     A.append(['' for i in range(len(B))])

    for i in range(len(B)):
        for j in range(len(B[0])):
            A[j][i] = B[i][j]

    #filp
    A = filp(A)
    return A

a.reverse()
for i in a:
    if i == 1:
        B = filp(B)
    else:
        B = rotate(B)

print(len(B), len(B[0]))
for i in B:
    print(*i)
