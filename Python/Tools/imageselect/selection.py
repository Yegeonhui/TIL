from PIL import Image
from PIL.ExifTags import TAGS
import shutil
import os

class selection:
    def __init__(self,JPGName,route2,route):
        self.JPGName=JPGName
        self.route2=route2
        img=Image.open(self.route2+"/"+self.JPGName)
        self.info=img._getexif()
        self.route=route

    def getEXIF(self):
        taglabel={}
        for tag,value in self.info.items():
            decoded=TAGS.get(tag,tag)
            taglabel[decoded]=value
        
        if float(taglabel["GPSInfo"][4][0])==0:
            src=self.route2+"/"+self.JPGName
            dir=self.route+"/nonGPS/"+self.JPGName
            shutil.move(src,dir)


new_networked_directory = r'\\server\share\folder'
os.chdir(new_networked_directory)
print(os.getcwd())

# route=os.getcwd()
# folder_list=os.listdir(route)
# try:
#     os.makedirs(route+"/nonGPS")
# except:
#     pass
# for folder in folder_list:
#     if folder!="nonGPS":
#         flag=True
#         for i in folder:
#             if i==".":
#                 flag=False
#                 break
#         if not flag:
#             continue
#         route1=route+"/"+folder #C:\Users\user\Desktop\직박구리\Geonhui\이미지추출\LW11 
#         file_list=os.listdir(route1) #안에파일        
#         for dir in file_list:
#             route2=route1+"/"+dir #C:\Users\user\Desktop\직박구리\Geonhui\이미지추출\LW11\LW11-1
#             JPG_list=os.listdir(route2)
#             for file in JPG_list:
#                 if len(file)<=3:
#                     continue
#                 if file[-1:-4:-1]=="gpj":
#                     img=selection(file,route2,route)
#                     img.getEXIF()



