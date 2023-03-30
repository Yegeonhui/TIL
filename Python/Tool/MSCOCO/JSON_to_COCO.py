"""
2022-09-13
json -> cocodataset으로 바꾸는 코드
Code by YGH
"""

import os
import json
from coco_foam import coco_foam
from datetime import datetime
import numpy as np

def handle_JSON(JSON, option, objects):
    if option == 'r':
        with open(JSON) as jsonFile:
            objects = json.load(jsonFile)
            return objects

    elif option == 'w':
        with open(JSON, 'w') as jsonFile:
            json.dump(objects, jsonFile, indent=2)


def make_image_dict(name, objects):
    image = {}
    image['license'] = 0
    image['file_name'] = name + '.jpg'
    image['coco_url'] = ""
    image['height'] = objects['imageHeight']
    image['width'] = objects['imageWidth']
    image['date_captured'] = datetime.now().strftime('%Y-%m-%d')
    image['flickr_url'] = ""
    image['id'] = image_cnt
    return image


def make_annotations_dict(cnt, points, label):
    annotation = {}
    x_arr = points[0, :, 0]
    y_arr = points[0, :, 1]
    min_y = min(y_arr)
    max_y = max(y_arr)
    min_x = min(x_arr)
    max_x = max(x_arr)
    width = max_x - min_x
    height = max_y - min_y
    annotation['segmentation'] = [points[0, :, :].reshape(-1).tolist()]
    annotation['area'] = width * height
    annotation['iscrowd'] =  0
    annotation['image_id'] = image_cnt
    annotation['bbox'] = [min_x, min_y, width, height]
    annotation['category_id'] = name_dict[label]
    annotation['id'] = cnt
    return annotation


def make_name_dict():
    name_arr = []
    for idx, (root, dirs, files) in enumerate(os.walk(dir)):
        json_arr = [JSON for JSON in files if JSON.lower().endswith('.json')]
        for j in json_arr:
            JSON = os.path.join(root, j)
            objects = handle_JSON(JSON, 'r', None)
            for o in range(len(objects['shapes'])):
                label = objects['shapes'][o]['label']
                if label in name_arr:
                    continue
                name_arr.append(label)

    name_dict = {}
    for n in range(len(name_arr)):
        name_dict[name_arr[n]] = n + 1
    return name_dict

dir = 'Sea_Polygon_sample'
supercategory = dir
name_dict = make_name_dict()
print(name_dict)
categories = [{} for _ in range(len(name_dict))]
for key, value in name_dict.items():
    categories[value - 1]['supercategory'] = supercategory
    categories[value - 1]['id'] = value
    categories[value - 1]['name'] = key

foam = coco_foam()
new_coco = {}
new_coco['info'] = foam['info']
new_coco['licenses'] = foam['licenses']
cnt = 1
image_cnt = 1
for idx, (root, dirs, files) in enumerate(os.walk(dir)):
    json_arr = [JSON for JSON in files if JSON.lower().endswith('.json')]
    images = []
    annotations = []
    
    for j in json_arr:
        name = os.path.splitext(j)[0]
        print(name)
        JSON = os.path.join(root, j)
        objects = handle_JSON(JSON, 'r', None)
        image = make_image_dict(name, objects)
        images.append(image)
        
        for o in range(len(objects['shapes'])):
            label = objects['shapes'][o]['label']
            points = objects['shapes'][o]['points']
            # make_annotations_dict(cnt, points, name)
            points = np.array([points])
            annotation = make_annotations_dict(cnt, points, label)
            annotations.append(annotation)
            cnt += 1
        image_cnt += 1

new_coco['images'] = images
new_coco['annotations'] = annotations
new_coco['categories'] = categories
# save json
handle_JSON(supercategory + '.json', 'w', new_coco)




        

