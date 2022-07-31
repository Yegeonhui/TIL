import os
from glob import glob
import cv2
import xml.etree.ElementTree as ET
import numpy as np

route=os.getcwd()
Image_list=glob(route+"/File/*.jpg")
Xml_list=glob(route+"/File/*.xml")

#make folder
os.makedirs(route+"/Augmentation",exist_ok=True)

#load dir 
for idx in range(len(Image_list)):
    Image_name=Image_list[idx][Image_list[idx].rfind("\\")+1:-4]

    Image=Image_list[idx]
    Xml=Xml_list[idx]
    
    xml=ET.parse(Xml)
    root=xml.getroot()
    object_tags=root.findall("object")
    
    Image=cv2.imread(Image)
    height,width,channel=Image.shape

    #mask 객체 개수만큼생성 
    count=len(object_tags)
    name_list=[[] for i in range(count)]

    masks=np.zeros((height,width,count))
    for n in range(count):
        mask=np.zeros((height,width))

        name=object_tags[n].find("name").text
        name_list[n]=name

        x_min=int(object_tags[n].find("bndbox").findtext("xmin"))
        y_min=int(object_tags[n].find("bndbox").findtext("ymin"))
        x_max=int(object_tags[n].find("bndbox").findtext("xmax"))
        y_max=int(object_tags[n].find("bndbox").findtext("ymax"))
        #print(x_min,y_min,x_max,y_max)
    
        point=[[x_min,y_min],[x_max,y_min],[x_max,y_max],[x_min,y_max]]
        point=np.array(point,np.int32)

        mask=cv2.fillConvexPoly(mask,point,255)
        masks[:,:,n]=mask[:,:]
    #print(name_list)
    
    #image 크기로 자르기 
    
    img_crop=0
    for h in range(0,height,500):
        for w in range(0,width,500):
            img_crop+=1
            #너비 1000, 높이 800
            if h<=height-800 and w<=width-1000:
                
                Image_crop=Image[h:h+800,w:w+1000,:]
                #Image_crop=Image[2000:2800,1000:2000,:]
                
                masks_crop=masks[h:h+800,w:w+1000,:]
                #masks_crop=masks[2000:2800,1000:2000,:]
                
                Objects=[]
    
                for obj in range(count):#count는 이미지에 있는 물체 수 
                    coordinate=np.where(masks_crop[:,:,obj]==255)
                    if len(coordinate[0])!=0:
                        y_min=coordinate[0][0]
                        x_min=coordinate[1][0]
                        y_max=coordinate[0][-1]
                        x_max=coordinate[1][-1]
                        Objects.append([x_min,y_min,x_max,y_max])
                
                if len(Objects)>=3:
                    cv2.imwrite(route+"/Augmentation/"+Image_name+"_"+str(img_crop)+".jpg",Image_crop)    
                    #print(Objects)

                    #objects : x_min,y_min,x_max,y_max
                    #name_list : 오브젝트 이름
                    
                    xml_copy=ET.parse(Xml)
                    root=xml_copy.getroot()
                    object=root.findall("object")
                    
                    cnt=0
                    for o_idx in range(len(object)):
                        cnt+=1
                        if cnt<=len(Objects):#len(Objects) : 자른이미지안에 객체수 
                            object[o_idx].find("name").text=name_list[o_idx]
                            object[o_idx].find("bndbox").find("xmin").text=str(Objects[o_idx][0])
                            object[o_idx].find("bndbox").find("ymin").text=str(Objects[o_idx][1])
                            object[o_idx].find("bndbox").find("xmax").text=str(Objects[o_idx][2])
                            object[o_idx].find("bndbox").find("ymax").text=str(Objects[o_idx][3])
                        else:
                            root.remove(object[o_idx])
                        
                        xml_copy.write(route+"/Augmentation/"+Image_name+"_"+str(img_crop)+".xml")
                    
                    
                    
                

        





