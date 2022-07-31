import os
import cv2

os.makedirs(os.getcwd() + "/PNG", exist_ok = True)
for idx, (root, dirs, files) in enumerate(os.walk("Image")):
    ImageList = [image for image in files if image.lower().endswith(".png")]
    
    for Image in ImageList:
        Imagename = Image[:-4]
        print(Imagename)
        Image = cv2.imread(os.path.join(root, Image))
        cv2.imwrite(os.getcwd() + "/PNG/" + Imagename + ".jpg", Image)
        
        