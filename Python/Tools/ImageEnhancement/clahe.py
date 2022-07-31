import os
import cv2
from glob import glob

route = os.getcwd() 
Imagelist = glob(route + "/Image/" + "*.jpg")


# 윈도우 사이즈 8, r,g,b 따로 clahe 적용

# R, G, B
#61 131 61
#68 140, 67
#59 120, 53
def lab_Contrast(img):
    lab = cv2.cvtColor(img,cv2.COLOR_BGR2LAB)
    l, a, b = cv2.split(lab)
    clahe = cv2.createCLAHE(clipLimit=3.0,tileGridSize=(8,8))
    cl = clahe.apply(l)
    limg = cv2.merge((cl,a,b))
    final = cv2.cvtColor(limg,cv2.COLOR_LAB2BGR)
    return final

def bgr_Contrast(img):
    b, g, r = cv2.split(img)
    clahe = cv2.createCLAHE(clipLimit=3.0,tileGridSize=(8,8))
    cl_b = clahe.apply(b)
    cl_g = clahe.apply(g)
    cl_r = clahe.apply(r)
    cl_img = cv2.merge((cl_b, cl_g, cl_r))
    return cl_img

for idx, (root, dirs, files) in enumerate(os.walk('Image')):
    ImageList = [img for img in files if img.lower().endswith(".jpg")]
    for n in range(len(ImageList)):
        name = ImageList[n][:-4]
        print(name)
        img = cv2.imread(os.path.join(root, ImageList[n]))
        img = bgr_Contrast(img)
        #img=cv2.resize(img,dsize=(300,550))
        cv2.imwrite(route + "/clahe/"+ name + ".jpg", img)
    
    
