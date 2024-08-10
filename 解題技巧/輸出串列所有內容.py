x = [1, 2, 3, 4, 5, 6, 7, 8]

#sol.1
print(x[0],x[1],x[2])

#sol.2
for i in x:
    print(i, end=' ')
print()

#sol.3
[print(i, end=' ') for i in x]
print()

#sol.4 <- use this !!!!!!
print(*x) 

print(*x[0:5])