s = input()
k = -7
r = ''
for i in s:
    r += chr(ord(i) + k) 
print(r)