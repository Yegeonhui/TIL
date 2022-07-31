# Code by YGH.
# v4.0 -> 폴더 읽어오는 부분 수정 
import os
import cv2
import xml.etree.ElementTree as ET
import numpy as np

from itertools import product
import time
from PIL import Image
import piexif

class Augmentation: 
    def __init__(self,                                                                                                                                                                                                                              
                 root,
                 Img,
                 Xml,
                 n,
                 crop_h,
                 crop_w,
                 gap,
                 min_object,
                 criteria):
        self.root = root
        self.Image_name = Img[Img.rfind("\\") + 1:-4]
        print(self.Image_name)
        self.Image = Image.open(os.path.join(self.root,Img))
        
        EXIF_dict = piexif.load(self.Image.info["exif"])
        self.EXIF=piexif.dump(EXIF_dict)

        self.width, self.height = self.Image.size
        self.Xml = os.path.join(self.root,Xml)

        self.n = n
        
        self.crop_h=crop_h
        self.crop_w=crop_w
        self.gap=gap
        self.min_object=min_object

        self.criteria=criteria

        # Output 파일의 이름(확장자 미포함)
        self.NewFileRoute = os.path.join(self.root, 'split', self.Image_name)
        
    # xml파싱
    def xml_parsing(self):
        xml = ET.parse(self.Xml)
        root = xml.getroot()
        self.object_tags = root.findall("object")
        
        #오브젝트당 사이즈 리스트 
        self.object_size = [[0] for i in range(len(self.object_tags))]
        for n in range(len(self.object_tags)):
            x_min = int(self.object_tags[n].find("bndbox").findtext("xmin"))
            y_min = int(self.object_tags[n].find("bndbox").findtext("ymin"))
            x_max = int(self.object_tags[n].find("bndbox").findtext("xmax"))
            y_max = int(self.object_tags[n].find("bndbox").findtext("ymax"))
            cnt=((x_min,y_min),(x_max,y_min),(x_max,y_max),(x_min,y_max))
            cnt=np.array(cnt)
            self.object_size[n] = cv2.contourArea(cnt)
        return len(self.object_tags)

    def cut_image_mask(self):
        listH = np.arange(0, self.height-self.crop_h, self.gap)
        listW = np.arange(0, self.width-self.crop_w, self.gap)
        items = [listH, listW]
        prod = list(product(*items))
        for h,w in prod:
            if h <= self.height - self.crop_h and w <= self.width - self.crop_w:
                Image_crop = self.Image.crop((w,h,w+self.crop_w,h+self.crop_h))
                self.check_object(Image_crop,h,w)
                self.n+=1

    def check_object(self,Image_crop,h,w):#cropimage 좌상단 좌표
        total_object=len(self.object_tags)
        Objects_list=[]
        for n in range(total_object):
            object_name=self.object_tags[n].find("name").text
            x_min = int(self.object_tags[n].find("bndbox").findtext("xmin"))
            y_min = int(self.object_tags[n].find("bndbox").findtext("ymin"))
            x_max = int(self.object_tags[n].find("bndbox").findtext("xmax"))
            y_max = int(self.object_tags[n].find("bndbox").findtext("ymax"))
            #네꼭지점이 cropimage안에잇는지 check 
            left_top=(h<=y_min<=h+self.crop_h and w<=x_min<=w+self.crop_w)
            right_bottom=(h<=y_max<=h+self.crop_h and w<=x_max<=w+self.crop_w)
            left_bottom=(h<=y_max<=h+self.crop_h and w<=x_min<=w+self.crop_w)
            right_top=(h<=y_min<=h+self.crop_h and w<=x_max<=w+self.crop_w)
            if left_top or right_bottom or left_bottom or right_top:
                #우하단 좌표가 cropimage밖에 있으면 최대 h, 최대 w 값으로 x_max,y_max 대입 
                if y_max>=h+self.crop_h: 
                    y_max=h+self.crop_h
                if x_max>=w+self.crop_w:
                    x_max=w+self.crop_w
                if y_min<=h:
                    y_min=h
                if x_min<=w:
                    x_min=w

                x_Min=x_min-w
                y_Min=y_min-h
                x_Max=x_max-w
                y_Max=y_max-h

                cnt=((x_Min,y_Min),(x_Max,y_Min),(x_Max,y_Max),(x_Min,y_Max))
                cnt=np.array(cnt)
                if self.object_size[n] * self.criteria / 100 <= cv2.contourArea(cnt):
                    Objects = [object_name, x_Min, y_Min, x_Max, y_Max]
                    Objects_list.append(Objects)

        if len(Objects_list)>=self.min_object:
            #format : 파일 형식 재정의, 생략하면 파일 이름 확장자에 의해 결정됨
            # Image_crop.save(self.route+self.save_folder+"/"+self.Image_name+"_"+str(self.n)+".jpg",format=None,optimize=False,exif=self.EXIF)
            Image_crop.save(self.NewFileRoute + "_" + str(self.n) + ".jpg",
                            format=None, optimize=False, exif=self.EXIF)
            self.make_xml(Objects_list)

    def make_xml(self,Objects_list):
        Objects=Objects_list #cropimage안에 object개수  
      
        xml_copy=ET.parse(self.Xml)
        croot=xml_copy.getroot()
        object=croot.findall("object")
        # root.find("filename").text=self.Image_name+"_"+str(self.n)+".jpg"
        croot.find('filename').text = os.path.split(self.NewFileRoute)[1] + "_"+str(self.n) + '.jpg'

        cnt=0 #총 객체가 10개, cropimage 의 object가 7개이면 xml의 object가 7개가 수정되어야됨. 
        for o_idx in range(len(object)):
            cnt+=1
            if cnt<=len(Objects): #cropimage 안에 object 수 
                object[o_idx].find("name").text=Objects[o_idx][0]
                object[o_idx].find("bndbox").find("xmin").text=str(Objects[o_idx][1])
                object[o_idx].find("bndbox").find("ymin").text=str(Objects[o_idx][2])
                object[o_idx].find("bndbox").find("xmax").text=str(Objects[o_idx][3])
                object[o_idx].find("bndbox").find("ymax").text=str(Objects[o_idx][4])
            else:
                croot.remove(object[o_idx])
            
            # xml_copy.write(self.route+self.save_folder+"/"+self.Image_name+"_"+str(self.n)+".xml")
            xml_copy.write(self.NewFileRoute + "_" + str(self.n) + ".xml")
        


def main(crop_h, crop_w, gap, total_object, min_object, criteria):
    for idx,(root,dirs,files) in enumerate(os.walk('RawData')):
        if len(files) !=0 and os.path.split(root)[1] != "야장" and os.path.split(root)[1]!='split':
            if 'split' in dirs:
                pass
            else:
                print(root)

                ListImg=[img for img in files if img.lower().endswith('jpg')]
                ListXml=[xml for xml in files if xml.lower().endswith('xml')]
                
                print(ListImg)
                
                for idx in range(len(ListImg)):
                    try:
                        os.makedirs(root+"/split",exist_ok=True)
                        A = Augmentation(root=root,
                             Img=ListImg[idx], Xml=ListXml[idx], n=0,
                             crop_h=crop_h,
                             crop_w=crop_w,
                             gap=gap,
                             min_object=min_object,
                             criteria=criteria)
                        
                        A.xml_parsing()
                        if A.xml_parsing() >= total_object:
                            print("5개 이상입니다.")
                        print(A.xml_parsing())
                        
                        A.cut_image_mask()
                    
                    except Exception as e:
                        print(ListImg[idx],e)


if __name__ == "__main__":
    start = time.time()
    main(crop_h=800, crop_w=1200, gap=400, total_object=3, min_object=3, criteria=10)
    print("실행시간", time.time()-start)
