from PIL import Image
from PIL.ExifTags import TAGS
import shutil
import os
import PySimpleGUI as sg
from glob import glob

def main():
    sg.theme('Dark Blue 3')

    layout=[
        [sg.Text('NonGPS Image selector')],
        [sg.InputText(),sg.FolderBrowse('Select Folder')],
        [sg.Button('Ok'),sg.Button('Exit')]
    ]

    window=sg.Window('IREM tech.',layout)

    while True:
        event,values=window.read()
        if event==sg.WIN_CLOSED or event=='Exit':
            break
        if event=="Ok":
            path=values['Select Folder']
            
            os.makedirs(path+"/NonGPS",exist_ok=True)

            Jpg_List=glob(path+"/*.jpg")

            n=len(Jpg_List)
            imglist=[]
            for idx in range(n):
                jpg=Jpg_List[idx]
                print(jpg)
                # p=jpg.rfind("\\")
                # name=jpg[p+1:]
                
                img=Image.open(jpg)
                info=img._getexif()
                
                taglabel={}
                for tag,value in info.items():
                    decoded=TAGS.get(tag,tag)
                    taglabel[decoded]=value
               
                if float(taglabel['GPSInfo'][4][0])==0:
                    img.close()
                    shutil.copy2(jpg,path+"/NonGPS")
                    os.remove(jpg)
                    
                    #shutil.move(jpg,path+"/NonGPS")
    # l=len(imglist)
    # print(imglist)
    # for i in range(l):
    #     os.remove(imglist[i])

if __name__=='__main__':
    main()

