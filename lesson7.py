#Loop 迴圈
'''
1.For Loop (計次的迴圈)
- 知道執行範圍
- 我知道執行幾次

usage: for [index] in ___範圍___

範圍：
1.List:
Ex.
for i in ['鮭魚','鮪魚','玉子燒']:
    print(i)

2.String:
Ex.
for i in 'hello': #['h','e','l','l','o']
    print(i)

3.數字範圍：range(start[起始值], end[終止值], interval[間隔值])
從 start 開始到 end-1(前一個)
每一次 加上interval

Ex. range(5) -> end -> 0 ~ 4

Ex. range(1,5) -> start, end -> 1 ~ 4

Ex. range(1,5,2) -> start, end, interval -> 1, 3

Ex. 等差級數：輸入a0(首項), d(公差), n(項數)，求級數總和
Sol.a0, d, n = int(input()), int(input()), int(input())
    sum = 0
    for i in range(a0, a0+n*d, d):
        sum += i
    print(sum)

2.While Loop (條件的迴圈)
- 不知執行範圍
- 不知道執行幾次

while ___條件(bool)___:
[TAB]條件達成要幹嘛
Ex.把a除2直到a < 1
a = 10
while a > 1:
    a /= 2
print(a)
'''
# print([i for i in range(1,11)])

#continue -> skip
#break -> stop
for i in range(10):
    if i == 3: continue
    if i == 5: break
    print(i)