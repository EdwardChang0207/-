'''
Level 1
a = input().split()
M = int(a[0])
D = int(a[1])
S = (M*2+D)%3

if S == 0:
    print('普通')
elif S == 1:
    print('吉')
else:
    print('大吉')

Level 2
M, D = input().split() *宣告多個變數：變數之間用','隔開，等號右邊可以是多個值(Value)或串列(List)
S = (int(M)*2+int(D))%3

if S == 0:
    print('普通')
elif S == 1:
    print('吉')
else:
    print('大吉')
'''