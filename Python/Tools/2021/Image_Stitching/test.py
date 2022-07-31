import cv2
import os

route=os.getcwd()
img=cv2.imread(route+"/Stitching_image.jpg")
print(img.shape)