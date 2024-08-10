#List 串列
'''
空串列
l = [[]]
print(bool(l)) -> True

串列取值
l = [1, 2, 3]
print(l[0],l[1],[2])
print(l[-1],l[-2],l[-3])
l = [1, 2, 3, 4, ..., n]
print(l[len(l)-1])

快速建立串列
l = []
for i in range(1,10001):
    l.append(i)

l = [i for i in range(1, 10001)]

平均
l = [29, 83, 12]
sum(l)/len(l)

l = [0, 0, 1, 1, 1, 2, 2]
c = l.count(5)
print(c)

l = [1, 2, 3]
print(l.index(2))

l = [1,2,3]
l.insert(1, 5)
print(l)

l = [1,2,3]
x = l.pop()
print(l)
print(x)

l = [1,2,3]
l.remove(2)
print(l)

l=[1,2,3]
l.reverse()
print(l)

[start:end:interval]

l = [1,2,3]
del l[0:2]
print(l)

l = [i for i in range(1, 101)]
print(l[0:len(l):2])
'''
l = [24,23, 1982, 182]
l.sort()
l.reverse()
print(l)