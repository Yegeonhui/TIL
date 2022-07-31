import numpy as np
import os
import cv2
from glob import glob

route=os.getcwd()
image_list = glob(route + "/Image/*.jpg")

sharpening_mask1 = np.array([[-1,-1,-1],[-1,9,-1],[-1,-1,-1]]) 
sharpening_mask2 = np.array([[0,-1,0],[-1,5,-1],[0,-1,0]])


for image in image_list:
    name = image[-6 : image.rfind(".")]

    img = cv2.imread(image)
    gray = img
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    
    sharpening_out1 = cv2.filter2D(gray,-1,sharpening_mask1) 
    sharpening_out2 = cv2.filter2D(gray,-1,sharpening_mask2)

    cv2.imwrite(route + "/sharpening/" + name + "_1" + ".jpg", sharpening_out1)
    cv2.imwrite(route + "/sharpening/" + name + "_2" + ".jpg", sharpening_out2)

    


