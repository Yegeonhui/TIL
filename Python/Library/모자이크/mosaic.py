import cv2 
class Mosaic:
	#초기화함수 선언
	def __init__(self,rate,x,y,w,h):
		self.rate=rate
		self.x=x
		self.y=y
		self.w=w
		self.h=h
	#모자이크하는 함수 
	def modify(self,image):
		roi=image[self.y:self.y+self.h,self.x:self.x+self.w]
		#cv2.resize(입력이미지,절대크기,상대크기,보간법)
		#축소
		roi=cv2.resize(roi,None,fx=self.rate,fy=self.rate,interpolation=cv2.INTER_AREA)
		#확대
		roi=cv2.resize(roi,(self.w,self.h),interpolation=cv2.INTER_AREA)
		#
		image[self.y:self.y+self.h,self.x:self.x+self.w]=roi
		return image