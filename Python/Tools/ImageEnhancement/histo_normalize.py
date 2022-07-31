import numpy as np
import os
import cv2
from glob import glob
import matplotlib.pylab as plt 

route = os.getcwd()
image_list = glob(route+"/Image/*.jpg")
for image in image_list:
    name = image[-6:image.rfind(".")]
    img = cv2.imread(image)
    
    b, g, r = cv2.split(img)

    # #수동 계산 
    # img_f=img.astype(np.float32)
    # img_norm=((img_f-img_f.min())*(255)/(img_f.max()-img_f.min()))
    # img_norm=img_norm.astype(np.uint8)

    #########################################
    
    #cv2.normalize()함수사용 
    #NORM_MINMAX,cv2.NORM_L1,cv2.NORM_L2,cv2.NORM_INF
    
    # img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    # img_norm2=cv2.normalize(img,None, 50, 150,cv2.NORM_MINMAX)
    # cv2.imwrite(route+"/histo_normalize/"+name+".jpg",img_norm2)

    #######################################

    b = cv2.normalize(b, None, 40, 80, cv2.NORM_MINMAX)
    g = cv2.normalize(g, None, 90, 150, cv2.NORM_MINMAX)
    r = cv2.normalize(r, None, 40, 80, cv2.NORM_MINMAX)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.normalize(gray , None, 120, 130, cv2.NORM_MINMAX)
    
    img_norm2=cv2.merge((g, g, g))
    #cv2.imwrite(route + "/histo_normalize/" + name + "_gray" + ".jpg",img_norm2)
    cv2.imwrite(route + "/histo_normalize/" + name + "_1" + ".jpg",img_norm2)

    #hist=cv2.calcHist([img],[0],None,[256],[0,255])

    # cv2.imshow('before',img)
    # cv2.imshow('Manual',img_norm)
    # cv2.imshow('cv2.normalize()',img_norm2)

