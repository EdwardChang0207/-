a, b, c = map(int, input().split()) 

if (a + b) <= c: print('No')
elif a**2+b**2 < c**2: print('Obtuse')
elif a**2+b**2 == c**2: print('Right')
elif a**2+b**2 > c**2: print('Acute')