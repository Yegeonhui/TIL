import cv2
import os

for idx, (root, dirs, files) in enumerate(os.walk('Image')):
    Image_list = [img for img in files if img.lower().endswith('.jpg')]
    for img in Image_list:
        Image = cv2.imread(os.path.join(root, img))

        height, width = Image.shape[:2]

        # H : 색상, S : 채도, V : 명도
        Image_hsv = cv2.cvtColor(Image, cv2.COLOR_BGR2HSV) 

        # for n in range(30, 70, 5):

        # 1
        lower_filter1 = (60, 40, 40)    #1(60, 40, 40)
        upper_filter1 = (90, 255, 255)  # (90, 255, 255)
        
        dst1 = cv2. inRange(Image_hsv, lower_filter1, upper_filter1)
        
        # 2
        lower_filter2 = (30, 110, 110)
        upper_filter2 = (100, 255, 255)

        dst2 = cv2.inRange(Image_hsv, lower_filter2, upper_filter2) 
        
        # def weight(x):
        #     pass

        # cv2.namedWindow('Image')
        # cv2.createTrackbar('Weight', 'Image', 0, 100, weight)

        # while True:
        #     cv2.getTrack
        #     weight = cv2.getTrackbarPos('Weight','image')
        #     addWeight = cv2.addWeighted(dst1, float(100-weight) * 0.01, dst2, float(weight) * 0.01, 0)
        #     cv2.imshow('image',addWeight)

        #     if cv2.waitKey(1) & 0XFF ==27:
        #         break;
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()

        # 3
        # dst3 = cv2.bitwise_and(Image, Image, mask = dst2)
        # 검은색 : 0
        # dst3 = cv2.addWeighted(dst1, 1.0, dst2, 1.0, 0.0)
        dst3 = cv2.bitwise_or(dst2, dst1)
        

        # resize
        dst1 = cv2.resize(dst1, dsize = (480, 480))
        dst2 = cv2.resize(dst2, dsize = (480, 480))
        dst3 = cv2.resize(dst3, dsize = (480, 480))

        cv2.imshow('dst1',dst1)
        cv2.imshow('dst2',dst2)
        cv2.imshow('dst3',dst3)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    #

# 색 반전 dst1 = cv2.bitwise_not(dst1)