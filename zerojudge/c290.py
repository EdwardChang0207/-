x = input() #str, eg.'123456'
odd, even = 0, 0
for i in range(len(x)-1): #i -> 0,1,2,...
    if i % 2 == 0: #odd
        odd += int(x[i])
    else:
        even += int(x[i])
print(abs(odd-even))

'''
解題思路：
Step1.I/O
    1.Input -> 一行, '數字'
    2.Output -> 一行, |odd-even|

    from Step1:
        "x = input()"
        |...something...|
        "print(abs(odd-even))"

Step2.Variable
    1.odd -> 奇數位總和 -> starts from 0
    2.even -> 偶數位總和 -> starts from 0

    from Step2:
    x = input()
    "odd, even = 0, 0"
    |...something...|
    print(abs(odd-even))

Step3.cal sum for odd & even
    1.using for loop for assign index which stands for current position:
        for i in range(len(x)-1) -> index: 0 ~ len(x)-2 (x[-1] -> '/r') *Note. len() -> length(int)
    2.using index to identify odd or even: 
        if i can be 2*A, A is int -> odd, else -> even
    3.sum

    from Step3:
    x = input()
    odd, even = 0, 0
    "
    for i in range(len(x)):
        if i % 2 == 0: odd += int(x[i])
        else: even += int(x[i])
    "
    print(abs(odd-even))
'''