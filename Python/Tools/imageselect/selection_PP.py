from PIL import Image
from PIL.ExifTags import TAGS
import shutil
import os

def getEXIF(JPGName):
    img = Image.open(JPGName)
    info = img._getexif()
    img.close()

    taglabel = {}
    for tag, value in info.items():
        decoded = TAGS.get(tag, tag)
        taglabel[decoded] = value

    if float(taglabel['GPSInfo'][4][0])==0:
        src="C:/Users/admin/Desktop/IREM_Assignment2021/Geonhui/이미지추출/"
        dir="C:/Users/admin/Desktop/IREM_Assignment2021/Geonhui/이미지추출/0/"
        shutil.move(src+JPGName,dir+JPGName)


src=str(input("경로를 넣어주세요"))
file_list=os.listdir(src)
for i in file_list:
    if len(i)<=3:
        continue
    if i[-1:-4:-1]=="gpj":
        longitude=getEXIF(i)
#de=int(longitude)
# mi=int((longitude-de)*60)
# se=(longitude-de)*3600-mi*60
# print("도",de)
# print("분",mi)
# print("초",se)

    