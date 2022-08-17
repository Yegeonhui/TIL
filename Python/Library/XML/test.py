import os
import xml.etree.ElementTree as ET

# #
# node=ET.Element("first")
# node.text="안녕"
# ET.dump(node)

# #
# root=ET.Element("information")

# name=ET.Element("name")
# name.text="yegeonhui"
# root.append(name)

# age=ET.Element("age")
# age.text="26"
# root.append(age)

# def indent(elem,level=0): 
#     i="\n"+level*"  "
#     if len(elem):
#         if not elem.text or not elem.text.strip():
#             elem.text=i+"  "
#         if not elem.tail or not elem.tail.strip():
#             elem.tail=i
#         for elem in elem:
#             indent(elem,level+1)
#         if not elem.tail or not elem.tail.strip():
#             elem.tail=i
#     else:
#         if level and (not elem.tail or not elem.tail.strip()):
#             elem.tail=i

# route=os.getcwd()
# indent(root)
# root=ET.ElementTree(root)
# #root.write(route+"/note.xml")
# #
# route=os.getcwd()
# xml=route+"/xml_test.xml"
# xml=ET.parse(xml)
# root=xml.getroot()
# object=root.findall("object")

# for idx in range(len(object)):
#     name=object[idx].find("name").text
#     xmin=object[idx].find("bndbox").find("xmin").text
#     ymin=object[idx].find("bndbox").find("ymin").text
#     xmax=object[idx].find("bndbox").find("xmax").text
#     ymax=object[idx].find("bndbox").find("ymax").text
#     if name=="(11)PET_Bottle":
#         object[idx].find("name").text="yegeonhui"
#         object[idx].find("bndbox").tag="info"

#         object[idx].find("info").find("xmin").tag="age"
#         object[idx].find("info").find("ymin").tag="height"
#         object[idx].find("info").find("xmax").tag="weight"
#         object[idx].find("info").find("ymax").tag="address"
        
#         object[idx].find("info").find("age").text="26"
#         object[idx].find("info").find("height").text="180"
#         object[idx].find("info").find("weight").text="85"
#         object[idx].find("info").find("address").text="Busan"
    
#         hobby=ET.Element("hobby")
#         hobby.text="exercise"
#         object[idx].find("info").append(hobby)


#         age=object[idx].find("info").find("age").text
#         height=object[idx].find("info").find("height").text
#         weight=object[idx].find("info").find("weight").text
#         address=object[idx].find("info").find("address").text
#         hobby=object[idx].find("info").find("hobby").text
    
#         print(name,age,height,weight,address,hobby)

# xml.write(route+"/test.xml")

# for name in root.iter('name'):
#     print(name.text)
#
route=os.getcwd()

annotation=ET.Element("annotation")

folder=ET.Element("folder")
folder.text="XML"

filename=ET.Element("filename")
filename.text="xml_test"

path=ET.Element("path")
path.text="None"

source=ET.Element("source")

database=ET.Element("database")
database.text="Unknown"

annotation.append(folder)
annotation.append(filename)
annotation.append(path)
annotation.append(source)
source.append(database)

annotation=ET.ElementTree(annotation)
annotation.write(route+"/note.xml")

