class Fridge:
    #초기화 메서드: 어떤 클래스의 객체가 만들어 질때 자동으로 호출되어서 그 객체가 갖게 될 여러 가지 성질을 정해주는 일
    def __init__(self):
        self.isOpened=False
        self.foods=[]
    def open(self):
        self.isOpened=True 
        return "냉장고 문을 열었어요"
    def put(self,thing):
        if self.isOpened:
            self.foods.append(thing)
            return "냉장고 속에 음식이 들어갔네..."
        else:
            return "냉장고 문이 닫혀있어서 못넣겠어요.."
    def close(self):
        self.isOpened=False
        return "냉장고 문을 닫았어요"

class Food:
    pass 

#냉장고 클래스의 객체를 f라는 것을 만들고 음식 클래스의 객체는 apple과 elephant를 만듬         
f=Fridge()
print(f.isOpened)
print(f.foods)
apple=Food()
elephant=Food()
#foods리스트는 음식 클래스의 사과와 코끼리 객체를 갖고 있습니다. 
#냉장고 객체는 다른 객체들을 갖고 있다고도 할수 있다. 
#객체는 또 다른 객체를 포함 할수 있다. 객체지향프로그래밍에서는 composition이라고 한다. 
print(f.open())
print(f.put(apple))
print(f.put(elephant))
print(f.foods)