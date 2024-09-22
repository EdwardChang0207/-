n = int(input())
p = [list(map(int,input().split())) for i in range(n)]
p.insert(0, [1,0])
turn = [0, 0, 0]
for i in range(1,len(p)):
    #迴轉
    if i == 1:
        lastX = 0
        lastY = 0
    else:
        lastX = p[i-2][0]
        lastY = p[i-2][1]

    x1 = p[i-1][0] - lastX
    y1 = p[i-1][1] - lastY
    x2 = p[i][0] - p[i-1][0]
    y2 = p[i][1] - p[i-1][1]
    if ((x1 > 0) and (x2 < 0)) or (x1 < 0) and (x2 > 0):
        turn[2] += 1

    elif ((y1 > 0) and (y2 < 0)) or ((y1 < 0) and (y2 > 0)):
        turn[2] += 1

    #if on x
    if p[i][0] == p[i-1][0] and p[i][0] > 0:
        if p[i][1] - p[i-1][1] > 0:
            #left
            turn[0] += 1
        elif p[i][1] - p[i-1][1] < 0:
            #right
            turn[1] += 1

    elif p[i][0] == p[i-1][0] and p[i][0] < 0:
        if p[i][1] - p[i-1][1] > 0:
            #right
            turn[1] += 1

        elif p[i][1] - p[i-1][1] < 0:
            #left
            turn[0] += 1

    #if on y
    elif p[i][1] == p[i-1][1] and p[i][1] > 0:
        if p[i][1] - p[i-1][1] > 0:
            #left
            turn[0] += 1

        elif p[i][1] - p[i-1][1] < 0:
            #right
            turn[1] += 1

    elif p[i][1] == p[i-1][1] and p[i][1] < 0:
        if p[i][1] - p[i-1][1] > 0:
            #left
            turn[0] += 1

        elif p[i][1] - p[i-1][1] < 0:
            #right
            turn[1] += 1

print(*turn)
