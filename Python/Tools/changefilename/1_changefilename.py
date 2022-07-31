import os
import json 
import numpy as np
import shutil
import json
import random

def getjson(Json):
    with open(Json) as jsonFile:
        object = json.load(jsonFile)
        
    return object


start = 30000
total_image = 0
for idx, (root, dirs, files) in enumerate(os.walk("Image")):
    ImageList = [Image for Image in files if Image.lower().endswith("jpg")]
    total_image += len(ImageList)

num_array = random.sample(range(start, start + total_image), total_image)

cnt = 0
dir = 1
tie = 1000 # 폴더에 저장할 파일 갯수 
os.makedirs("new", exist_ok=True)
new_name = "FD_Polygon_"
for idx, (root, dirs, files) in enumerate(os.walk("Image")):
    ImageList = [Image for Image in files if Image.lower().endswith("jpg")]    
    JsonList = [Json for Json in files if Json.lower().endswith("json")]   
    for i in range(len(ImageList)):
        # tie기준으로 폴더 생성
        if cnt % tie == 0:
            os.makedirs('new/' + str(dir), exist_ok=True)
            dir += 1 
        Image_name = ImageList[i]
        print(Image_name)
        Json_name = os.path.splitext(Image_name)[0] + ".json"
        
        Image = os.path.join(root, Image_name)
        Json = os.path.join(root, Json_name)        
        
        shutil.copy2(Image, os.path.join("new", str(dir - 1),  new_name + str(num_array[cnt]) + ".jpg"))
        shutil.copy2(Json, os.path.join("new", str(dir - 1), new_name + str(num_array[cnt]) + ".json"))
        
        cnt += 1
        
        
        
        