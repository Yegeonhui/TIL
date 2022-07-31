import os 
import cv2
import json
import numpy as np
import xml.etree.ElementTree as ET


class GetGSD:
    def __init__(self, root, Img, Json, xml):
        self.root = root 
        self.Img = Img
        self.Image = cv2.imread(os.path.join(root, Img), 0)
        self.Json = Json
        self.xml = xml
        
    def getxml(self):
        xml = ET.parse(os.path.join(self.root, self.xml))
        root = xml.getroot()
        self.Object = root.findall("object")

    def getjson(self):
        with open(os.path.join(self.root, self.Json)) as jsonFile:
            self.Objects = json.load(jsonFile)

    def getgsd(self):
        h, w = self.Image.shape

        self.getxml()
        xmin = int(self.Object[0].find('bndbox').find('xmin').text)
        ymin = int(self.Object[0].find('bndbox').find('ymin').text)
        xmax = int(self.Object[0].find('bndbox').find('xmax').text)
        ymax = int(self.Object[0].find('bndbox').find('ymax').text)
    
        # 불가사리 좌표 
        center_x = (xmax - xmin) // 2 
        center_y = (ymax - ymin) // 2 

        # GetGSD
        self.getjson()
        mask = np.zeros((h,w))
        for Obj_num in range(len(self.Objects['shapes'])):
            points = self.Objects['shapes'][Obj_num]['points']
            points = np.array(points, np.int32)

            #cv2.polylines(Image, points, 닫힌모양, 색, 라인타입 )
            laser = cv2.polylines(mask, [points], False, 255)
        
        # cv2.imshow("laser",laser)
        # cv2.waitKey(0)
    
        x = np.where(laser == 255)[1]
        y = np.where(laser == 255)[0]

        GSD_list=[0 for i in range(h)]
        
        for c_idx in range(h):  
            GSD_list[c_idx] = 7.5 / (x[c_idx * 2 + 1] - x[c_idx * 2]) 
        
        # 불가사리 y 좌표 : center_y, 불가사리 크기 
        GSD = GSD_list[center_y]
        print("불가사리 GSD", GSD)
        print("불가사리 가로 cm", GSD * (xmax - xmin))
        print("불가사리 세로 cm", GSD * (ymax - ymin))
        

def main():
    for idx, (root, dirs, files) in enumerate(os.walk("Image")):
        Image_list = [img for img in files if img.lower().endswith(".jpg")]
        Json_list = [Json for Json in files if Json.lower().endswith(".json")]
        xml_list = [xml for xml in files if xml.lower().endswith(".xml")]
        for idx in range(len(Image_list)):
            Img = Image_list[idx]
            Json = Json_list[idx]
            xml = xml_list[idx]
            print(Img)

            G = GetGSD(root, Img, Json, xml)
            G.getgsd()

if __name__ == "__main__":
    main()

