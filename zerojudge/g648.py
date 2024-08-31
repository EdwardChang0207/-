t = int(input())
n = ['0','1','2','3','4','5','6','7','8','9']
for i in range(t):
    s = input()
    a = ''
    r = 1
    for i in range(len(s)):
        if s[i] not in n: #operator
            if s[i] != '-': #not '-'
                a += '*'
            else: #'-'
                if i != 0:
                    if s[i-1] not in n:
                        a += s[i]
                    else: a += '*'
                else:
                    a += s[i]
        else:#numbers
            a += s[i]

    a = a.split('*')
    for i in a:
        try:
            r *= int(i)
        except:
            pass
    print(r)
