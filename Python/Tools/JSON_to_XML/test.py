import json 
import os

route = os.getcwd()

with open(route + "/File" + "/cafe.json") as jsonFile:
    Objects = json.load(jsonFile)
    print(Objects['shapes'][0]['points'])