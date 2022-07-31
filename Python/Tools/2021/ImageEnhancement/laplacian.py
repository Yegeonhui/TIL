import cv2
import os
from glob import glob

route = os.getcwd()
image_list = glob(route+"/Image/*.jpg")
for image in image_list:
    name = image[-6:image.rfind(".")]
    img = cv2.imread(image, cv2.IMREAD_GRAYSCALE)
    Laplacian = cv2.Laplacian(img, -1)
    sobelx = cv2.Sobel(img, 3, 1, 1, ksize = 1)
    
    cv2.imwrite(route + "/Laplacian/" + name + "_soble" + ".jpg", sobelx)
    cv2.imwrite(route + "/Laplacian/" + name + "_laplacian" + ".jpg", Laplacian)
    