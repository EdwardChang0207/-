a, b = map(int,input().split())
n = int(input())
result = 0
for i in range(n):
    cart = list(map(int, input().split()))

    while -a in cart or -b in cart:
            if -a in cart:
                cart.remove(a)
                cart.remove(-a)
            else:
                cart.remove(b)
                cart.remove(-b)

    if (a in cart) and (b in cart):
         result += 1

print(result)