result = 0 #比賽結果 主隊贏：1 客隊贏：-1 平手：0
for i in range(2):#兩場->repeat 2 times
    #一場比賽
    a = sum([int(i) for i in input().split()])#主隊
    b = sum([int(i) for i in input().split()])#客隊
    print('%d:%d'%(a,b)) #輸出比數
    if a > b: result += 1
    elif a < b: result -= 1

#輸出比賽結果
if result > 0: print('Win')
elif result < 0: print("Lose")
else: print('Tie')