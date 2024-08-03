x = input() #str, eg.'123456'
odd, even = 0, 0
for i in range(len(x)-1): #i -> 0,1,2,...
    if i % 2 == 0: #odd
        odd += int(x[i])
    else:
        even += int(x[i])
print(abs(odd-even))