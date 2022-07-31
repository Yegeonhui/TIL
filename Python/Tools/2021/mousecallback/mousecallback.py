import numpy as np
import cv2
import os

def draw(event, x, y, flags, param):
    global ix, iy, mode, radius 
    if mode == True:
        if event == cv2.EVENT_LBUTTONDOWN:
            (ix, iy) = x, y
            print(x, y)

        elif event == cv2.EVENT_LBUTTONUP:
            cv2.line(image, (ix, iy), (x, y), (255, 255, 255), 2)
    else:
        if event == cv2.EVENT_LBUTTONDOWN:
            cv2.circle(image, (x, y), radius, (255, 255, 255), 2)
        elif event == cv2.EVENT_MOUSEWHEEL:
            if flags > 0:
                radius += 1
            elif radius > 1:
                radius -= 1

radius = 3
ix, iy = (-1, -1)
mode = True
for idx, (root, dirs, files) in enumerate(os.walk("Image")):
    Image_list = [img for img in files if img.lower().endswith(".jpg")]
    for img in Image_list:
        image = cv2.imread(os.path.join(root, img))
        while True:
            cv2.imshow("image", image)
            cv2.setMouseCallback("image", draw, image)
            
            key = cv2.waitKey(1)
            if key == ord("m"):
                mode = not mode
            elif key == 27:
                break 
            
        cv2.destroyAllWindows()