import os
import cv2
import numpy as np
import xml.etree.ElementTree as ET
from glob import glob

def MakeXml():
    xml_root = ET.Element('annotation')
    ET.SubElement(xml_root, 'folder').text = root
    ET.SubElement(xml_root, 'filename').text = imagename[ : -4]
    ET.SubElement(xml_root, 'path').text = os.path.join(os.getcwd(), root, imagename)
    
    
    source = ET.SubElement(xml_root, 'source')
    ET.SubElement(source, 'database').text = 'Unknown'

    height, width, depth = cv2.imread(os.path.join(root, imagename)).shape
    size = ET.SubElement(xml_root, 'size')
    ET.SubElement(size, 'width').text = str(width)
    ET.SubElement(size, 'height').text = str(height)
    ET.SubElement(size, 'depth').text = str(depth)
    
    ET.SubElement(xml_root, 'segmented').text = '0'
    
    total_object = len(Object_arr)
    for object_idx in range(total_object):
        object = ET.SubElement(xml_root, 'object')
        
        ET.SubElement(object, 'name').text = Object_arr[object_idx][0]
        ET.SubElement(object, 'pose').text = 'Unspectified'
        ET.SubElement(object, 'truncated').text = '0'
        ET.SubElement(object, 'difficult').text = '0'
        
        
        x_min = random_x[object_idx]
        x_max = x_min + w_list[object_idx]
        
        y_min = random_y[object_idx]
        y_max = y_min + h_list[object_idx]
        
        bndbox = ET.SubElement(object, 'bndbox')
        ET.SubElement(bndbox, 'xmin').text = str(x_min)
        ET.SubElement(bndbox, 'ymin').text = str(y_min)
        ET.SubElement(bndbox, 'xmax').text = str(x_max)
        ET.SubElement(bndbox, 'ymax').text = str(y_max)

    tree = ET.ElementTree(xml_root)
    return tree


os.makedirs("FIRA",exist_ok=True)

Object_img = glob("Echi/*.jpg")
    
for idx, (root, dirs, files) in enumerate(os.walk("Image")):
    if len(files) != 0:
        image_list = [img for img in files if img.lower().endswith(".jpg")]
        for img in image_list:
            Object_arr = []
            h_list = []
            w_list =[]
            rand = np.random.randint(len(Object_img), size = 1)
            for idx in rand:
                objectname = Object_img[idx]
                objectname = objectname.split("_")[0][-4 : ]
                print(objectname)
                
                object = Object_img[idx]
                object = cv2.imread(object)
                
                h, w, c = object.shape
                
                h_list.append(h)
                w_list.append(w)
                
                Object_arr.append((objectname, object))
                
            imagename = img
            print(imagename)
            
            img = cv2.imread(os.path.join(root, img))
            Height, Width, _ = img.shape
            
            random_x = np.random.randint(Width, size=len(Object_arr))
            random_y = np.random.randint(Height, size=len(Object_arr))
        
            for idx in range(len(Object_arr)):
                x = random_x[idx]
                y = random_y[idx]
                h = h_list[idx]
                w = w_list[idx]
                
                if x + w > Width:
                    x = Width - w
                    random_x[idx] = x
                
                if y + h > Height:
                    y = Height - h
                    random_y[idx] = y
                
                
                
                img[y : y + h, x : x + w, :] = Object_arr[idx][1][:, :, :]

            tree = MakeXml()

            # xml 저장
            tree.write("FIRA/FIRA_" + imagename[ : -4] + ".xml")
            # 이미지 저장
            cv2.imwrite("FIRA/FIRA_" + imagename[ : -4] + ".jpg", img)
            
        


