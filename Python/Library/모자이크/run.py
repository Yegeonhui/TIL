import cv2
from mosaic import Mosaic
rate=float(input("모자이크에 사용할 축소 비율?"))
image=cv2.imread("cafe.jpg")
x,y,w,h=cv2.selectROI("cafe",image,False)
mos=Mosaic(rate,x,y,w,h)
image=mos.modify(image)
cv2.imshow("cafe",image)
cv2.waitKey(0)
cv2.destroyAllWindows(