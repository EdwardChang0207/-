a, b, c = map(int, input().split())
r = []

#AND
if (a and b) == c: r.append('AND')
#OR
if (a or b) == c: r.append('OR')
#XOR
if ((a or b) and not(a and b)) == c: r.append('XOR')

if r: print(*r,sep='\n')
else: print('IMPOSSIBLE')