class Book:
    def __init__(self,title,price,author):
        self.title=title
        self.price=price
        self.author=author
    def printData(self):
        print("제목:",self.title)
        print("가격:",self.price)
        print("저자:",self.author)

