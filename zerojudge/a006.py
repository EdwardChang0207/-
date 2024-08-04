a, b, c = list(map(int, input().split()))
d = b**2 - 4*a*c
if d > 0:
    print('Two different roots x1=%d , x2=%d' % (int((a+d**.5)/2*a), int((a-d**.5)/2*a)))
elif d == 0:
    print('Two same roots x=%d' % int((a+d**.5)/2*a))
else:
    print('No real root')