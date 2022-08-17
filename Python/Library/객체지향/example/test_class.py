class Person:
    def __init__(self,age,height,weight):
        self.age=age
        self.height=height
        self.weight=weight
    def character(self):
        print(self.age,self.height,self.weight)
    def printHello(self):
        print("Hello!",self)


