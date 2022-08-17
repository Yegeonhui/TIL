#객체지향
class character:
    age=26 #변수
    weight=85
    height=180
    power=1000
    intel=30
    def programming(self): #메서드 : 클래스 내부에 정의된 함수
        self.intel+=10
        return self.intel
    def eat(self):
        return "냠냠"
    def sleep(self):
        return "쿨쿨"
    def tal(self):
        return "주절주절"

class son(character):
    def cry(self):
        return "응애~"

#객체지향
# yegeonhui=character() #yegeonhui라는 객체생성 
# yegeonhui.programing()
# print(yegeonhui.intel)

# #절차지향
# yegeonhui_intel=30
# Programming=True
# if Programming: 
#     yegeonhui_intel+=10
#     print(yegeonhui_intel)
# else:
#     print(yegeonhui_intel)