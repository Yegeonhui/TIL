import cv2
import numpy as np
import os
from glob import glob

route=os.getcwd()
image_list=glob(route+"/Image/*.jpg")
for image in image_list:
    name=image[-6:image.rfind(".")]
    img = cv2.imread(image)
    edges = cv2.Canny(img, 50, 200)
    # 결과 출력

    cv2.imwrite(route + "/cannyedge/" + name + "_1" + ".jpg", edges)
    