#Operator 運算子
'''
#1. Operators for Numbers: Number & Number -> Number
3    print(3+1)
3    print(3-1)
2    print(3*1)
2    print(3/1) #always float
2    print(3//1) #商
2    print(3%1) #＊餘＊
1    print(3**2) #指數
0    print(-1) #負號

#2. Logic Operators for Numbers: Number & Number -> Bool (關係)
print(1 > 2)
print(1 < 2)
print(1 >= 2)
print(1 <= 2)
print(1 == 2) # = -> assign, == -> equal
print(1 != 2)

#3. Operators for Booling: bool & bool -> bool

#not 否定
# 不錯喔！ -> True
# 不 not 錯 False -> True
# 不行 -> False
# not True -> False
print(not True)

#or 或
Math or English -> 3000
a          b         c
真值表
T or F -> T
F or T -> T
T or T -> T
F or F -> F

#and 且
BlackTea and Milktea -> 滿意？
T and F -> F
F and T -> F
T and T -> T
F and F -> F

#xor (excursive or) 斥或閘
珍奶 xor 烏龍 -> 滿意？
T xor F -> T
F xor T -> T
T xor T -> F
F xor F -> F
'''
a = False
b = False
print((a or b) and not(a and b))

