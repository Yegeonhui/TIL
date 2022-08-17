#3. 상속 
class Person:#학생 클래스
    eyes=2 #변수 
    nose=1
    mouth=1
    ears=2
    arms=2
    legs=2
    def eat(self): #메서드
        return "냠냠"
        
    def sleep(self):
        return "쿨쿨"
        
    def talk(self):
        return "주절주절"
        
class Student(Person):#Student 클래스는 Person클래스를 상속받음. 
    def study(self):
        return "열공열공"

yegeonhui=Person()
print(yegeonhui.mouth)
print(yegeonhui.talk())

guni=Student()
print(guni.mouth)
print(guni.talk())
print(guni.study())