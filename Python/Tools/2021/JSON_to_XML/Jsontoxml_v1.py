import json
import os
import numpy as np
import xml.etree.ElementTree as ET
import cv2

for idx, (root, dirs, files) in enumerate(os.walk('File')):
    Imagelist = [Image for Image in files if Image.lower().endswith(".jpg")]
    Jsonlist = [Json for Json in files if Json.lower().endswith(".json")]
    
    for num in range(len(Imagelist)):
        Image = Imagelist[num]
        Json = Jsonlist[num]
        print(Image)
        with open(os.path.join(root, Json)) as jsonFile:
            Objects = json.load(jsonFile)
        
            # makeXml     
            xml_root = ET.Element('annotation')
            ET.SubElement(xml_root, 'folder').text = root
            ET.SubElement(xml_root, 'filename').text = Image
            ET.SubElement(xml_root, 'path').text = os.path.join(os.getcwd(), root, Image)
            
            source = ET.SubElement(xml_root, 'source')
            ET.SubElement(source, 'database').text = 'Unknown'
            
            height, width, depth = cv2.imread(os.path.join(root, Image)).shape
            size = ET.SubElement(xml_root, 'size')
            ET.SubElement(size, 'width').text = str(width)
            ET.SubElement(size, 'height').text = str(height)
            ET.SubElement(size, 'depth').text = str(depth)
            
            ET.SubElement(xml_root, 'segmented').text = '0'
            
            
            
            #xmin, ymin, xmax, ymax
            total_object = len(Objects['shapes'])
            for object_idx in range(total_object):
                object = ET.SubElement(xml_root, 'object')
                
                ET.SubElement(object, 'name').text = Objects['shapes'][object_idx]['label']
                ET.SubElement(object, 'pose').text = 'Unspectified'
                ET.SubElement(object, 'truncated').text = '0'
                ET.SubElement(object, 'difficult').text = '0'
                
                points = Objects['shapes'][object_idx]['points']
                points = np.array(points)
                x = points[:, 0]
                y = points[:, 1]
                
                x_min = int(min(x))
                x_max = int(max(x))
                
                y_min = int(min(y))
                y_max = int(max(y))
                
                
                bndbox = ET.SubElement(object, 'bndbox')
                ET.SubElement(bndbox, 'xmin').text = str(x_min)
                ET.SubElement(bndbox, 'ymin').text = str(y_min)
                ET.SubElement(bndbox, 'xmax').text = str(x_max)
                ET.SubElement(bndbox, 'ymax').text = str(y_max)
        
            tree = ET.ElementTree(xml_root)
            tree.write(os.path.join(os.getcwd(), root, Image[:-4] + '.xml'))   
                
        
        
        
        