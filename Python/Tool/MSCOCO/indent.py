import json 
from glob import glob

# 들여쓰기
json_arr = glob('annotations/*.json')
for j in json_arr:
    with open(j) as jsonFile:
        objects = json.load(jsonFile)

    with open(j, 'w') as jsonFile:
        json.dump(objects, jsonFile, indent=2)

# json_arr = glob('annotations/*.json')
# j = json_arr[3]
# with open(j) as jsonFile:
#     objects = json.load(jsonFile)
# #print(objects['info'])
# # 5000
# print(len(objects['info']))
# print(len(objects['licenses']))
# print(len(objects['images']))
# print(len(objects['annotations']))
# print(len(objects['categories']))
#print(objects['images'][0])

# # 36781
# print(len(objects['annotations']))
#print(objects['annotations'][0])
# 80
#print(len(objects['categories']))
#print(objects['categories'][0])