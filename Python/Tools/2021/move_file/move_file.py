import os
import shutil
os.makedirs('new_dir', exist_ok=True)
for idx, (root, dirs, files) in enumerate(os.walk("Image")):
    image_file = [image for image in files if image.lower().endswith("tif")]
    for image in image_file:
        json_name = os.path.splitext(image)[0] + ".json" 
        image_name = image
        
        Json = os.path.join(root, json_name)
        image = os.path.join(root, image_name)
        
        shutil.move(image, 'new_dir/' + image_name)
        shutil.move(Json, 'new_dir/' + json_name)
