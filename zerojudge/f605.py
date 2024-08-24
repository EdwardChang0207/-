n, d = map(int,input().split())
amount, price = 0, 0

for i in range(n):
    p = list(map(int, input().split()))
    if d < (max(p) - min(p)):
        amount += 1
        price += sum(p) // 3

print(amount, price)