#1. 변수와 메서드 
class character:
    age=26 #변수
    weight=85
    height=180
    power=1000
    def dog(self): #메서드 
        return "mingming"
    def exercise(self):
        self.weight-=1
        self.power+=10
        
yegeonhui=character()
print(yegeonhui.age)
print(yegeonhui.weight)
print(yegeonhui.height)
print(yegeonhui.power)
print(yegeonhui.dog())

yegeonhui.exercise()
print(yegeonhui.age)
print(yegeonhui.weight)
print(yegeonhui.height)
print(yegeonhui.power)


