# car : color, a, top speed

class car: #類別 CLASS
    def __init__(self, color, a, top_speed): #初始化函式
        self.color = color #屬性
        self.a = a
        self.top_speed = top_speed
        self.x = 0
        self.y = 0
    
    def foward(self):
        self.y += 1

c = car('red', 3, 200) #物件 OBJECT

# print(c.color)
# print(c.a)
# print(c.top_speed) #. -> 的
print(c.x, c.y)
c.foward()
print(c.x, c.y)

