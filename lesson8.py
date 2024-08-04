# def Computer(cpu, gpu, memory):
#     .....
#     return game

# def oven(chicken):
#     return cooked chicken

# def add(a,b):
#     return a+b

# print(add('3','4'))

# def add(a:int, b:int) -> int:
#     return a+b
# print(add(3, 4))

import random
ans = random.randint(1,100)
upper, lower = 100, 1
guess = -1
while ans != guess:
    print("%d ~ %d"%(lower, upper))
    guess = int(input())
    if guess < upper and guess > lower:
        if guess > ans:
            print('too big!')
            upper = guess
        elif guess < ans:
            print('too small')
            lower = guess
    else:
        print('error out of range')
print('correct')