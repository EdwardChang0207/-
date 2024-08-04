#1.迴圈法
x = input().split()
for i in range(len(x)):
    x[i] = int(x[i])
print(x)
#2.串列法
x = [int(i) for i in input().split()]
print(x)
#3.map()
x = list(map(int,input().split()))
print(x)