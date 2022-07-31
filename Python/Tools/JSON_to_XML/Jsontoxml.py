import json
from json2xml import json2xml
from json2xml.utils import readfromurl, readfromstring, readfromjson 
import os
import xmltodict

# https://json2xml.readthedocs.io/en/latest/


for idx, (root, dirs, files) in enumerate(os.walk('File')):
    Imagelist = [Image for Image in files if Image.lower().endswith(".jpg")]
    Jsonlist = [Json for Json in files if Json.lower().endswith(".json")]
    
    for num in range(len(Imagelist)):
        Image = Imagelist[num]
        Json = Jsonlist[num]
        
        with open(os.path.join(root, Json)) as f:
            jsonString = f.read()
            data = readfromstring(jsonString)
        print(json2xml.Json2xml(data, wrapper = "all", pretty = True, attr_type = False).to_xml())
        
        #json_string = str(data).replace("'", '"')
        # from_string = readfromstring(json_string)
        # xml_string = json2xml.Json2xml(from_string, indent = 8).to_xml()
        
        #print(xml_string)

#with open()