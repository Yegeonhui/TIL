#객체지향
class Student:
    def __init__(self,korean,math,english):
        self.korean=korean
        self.math=math
        self.english=english
    def getkorean(self):
        return self.korean 
    def getmath(self):
        return self.math
    def getenglish(self):
        return self.english
    def getsum(self):
        return self.korean+self.math+self.english
    