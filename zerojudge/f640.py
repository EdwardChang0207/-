def f(x):
    return 2*x-3

def g(x,y):
    return 2*x+y-7

def h(x,y,z):
    return 3*x-2*y+z

s = list(map(str, input().split()))
box = [] #Stack 堆疊

for i in range(len(s)-1, -1, -1):
    if s[i] not in ['f','g','h']:
        box.append(s[i])
    elif s[i] == 'f':
        x = int(box.pop())
        box.append(f(x))
    elif s[i] == 'g':
        x = int(box.pop())
        y = int(box.pop())
        box.append(g(x,y))
    elif s[i] == 'h':
        x = int(box.pop())
        y = int(box.pop())
        z = int(box.pop())
        box.append(h(x,y,z))
print(box[0])