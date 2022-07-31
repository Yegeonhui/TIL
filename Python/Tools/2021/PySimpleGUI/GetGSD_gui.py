import PySimpleGUI as sg
import cv2
import numpy as np
import xml.etree.ElementTree as ET
import os

class GetGSD:
    def __init__(self, root, image, xml):
        self.root = root
        self.image = image
        self.xml = xml

    def mouse_event(self, event, x, y, flags, param): 
        if event == cv2.EVENT_LBUTTONDOWN:
            (self.ix, self.iy) = x, y
            print(x, y)
            self.x_y_list.append((x,y))
        elif event == cv2.EVENT_LBUTTONUP:
            cv2.line(self.image, (self.ix, self.iy), (x, y), (255, 255, 255), 2)    
            print(x,y)
            self.x_y_list.append((x,y))
    
    def getxml(self):
        xml = ET.parse(os.path.join(self.root, self.xml))
        root = xml.getroot()
        self.Object = root.findall("object")

    def getgsd(self):
        self.x_y_list = []
        self.ix, self.iy = (-1, -1)

        self.image = cv2.imread(os.path.join(self.root, self.image))
        h, w, c = self.image.shape
        
        flag = False
        while True:
            cv2.imshow("Image", self.image)
            #cv2.setMouseCallback(윈도우, 콜백 함수, 사용자 정의 데이터)
            cv2.setMouseCallback("Image", self.mouse_event, self.image)
            if len(self.x_y_list) >= 4:
                break
            key = cv2.waitKey(1)
            if key == 27:
                break
        left = self.x_y_list[0 : 2]
        right = self.x_y_list[2 : 4]

        points1 = np.array(left, np.int32)
        points2 = np.array(right, np.int32)
        laser = np.zeros((h,w))

        # cv2.polylines(Image, points, 닫힌모양, 색, 라인타입 )
        laser = cv2.polylines(laser, [points1], False, 255)
        laser = cv2.polylines(laser, [points2], False, 255)

        y = np.where(laser == 255)[0]
        x = np.where(laser == 255)[1]

        #레이저 포인트 정하기
        s_cnt = -1
        standard1 = -1
        for y_idx in range(len(y)):
            if standard1 == y[y_idx]:        
                break
            standard1 = y[y_idx]
            s_cnt +=1 

        e_cnt = -1
        standard2 = -1
        for y_idx in range(-1, -len(y)-1, -1):
            if standard2 == y[y_idx]:        
                break
            standard2 = y[y_idx]
            e_cnt += 1
      
        x = x[s_cnt : len(x) - e_cnt]

        self.getxml()
        xmin = int(self.Object[0].find('bndbox').find('xmin').text)
        ymin = int(self.Object[0].find('bndbox').find('ymin').text)
        xmax = int(self.Object[0].find('bndbox').find('xmax').text)
        ymax = int(self.Object[0].find('bndbox').find('ymax').text)
        
        # 불가사리 좌표 
        center_x = (xmax - xmin) // 2 
        center_y = (ymax - ymin) // 2 

        GSD_list=[0 for i in range(h)]
        
        for c_idx in range(len(x) // 2):  
            GSD_list[c_idx + standard1] = 7.5 / (x[c_idx * 2 + 1] - x[c_idx * 2]) 
    
        # 불가사리 y 좌표 : center_y, 불가사리 크기 
        GSD = GSD_list[center_y]
        print(xmax-xmin)
        print("불가사리 GSD", GSD)
        print("불가사리 가로 mm", GSD * (xmax - xmin))
        print("불가사리 세로 mm", GSD * (ymax - ymin))

        return GSD * (xmax - xmin)
    
class MakeGUI:
    def __init__(self, cm):
        self.cm = cm

    def makegui(self):
        sg.theme('Black')

        menu_def = [
                    ['&File', ['&Open', '&Save', '&Properties', 'E&xit']],
                    ['&Edit', ['&Paste', ['Special', 'Normal'], 'Undo']],
                    ['&Help', ['&About']]
                    ]
        layout = [
                [sg.Menu(menu_def, tearoff = False, pad = (20,1))],
                [sg.Text('Detection of Catch')],
                [sg.InputText(), sg.FolderBrowse('Select Folder'), sg.Button('GetGSD')],
                [sg.Text('', key = 'progress')],
                #[sg.Slider(orientation = 'horizontal', key = 'stSlider', range = (1, 100))],
                #[sg.ProgressBar(50, orientation = 'h', size = (20, 20), border_width = 4, key = 'progbar', bar_color = ['Red', 'Green'])],
                [sg.Button('Exit')],
                  ]

        window = sg.Window('Get GSD', layout, grab_anywhere = True)
        return window

    def getresult(self):
        sg.theme('Black')

        menu_def = [
                    ]

        layout = [
                [sg.Menu(menu_def, tearoff = False, pad = (20,1))],
                [sg.Text('result')],
                [sg.Text('불가사리 가로 cm : '), sg.InputText(self.cm)],
                [sg.Button('Exit')],                
                ]
                
        window = sg.Window('Get GSD', layout, grab_anywhere = True)
        return window

def main():
    M = MakeGUI(0)
    window = M.makegui()
    
    while True:
        event, values = window.read()
        print(event)

        if event in (None, 'Exit'):
            break 
        if event == 'GetGSD':
            print('you pressed the GetGSD')
            print(event, values)

            path = values['Select Folder']

            for idx, (root, dirs, files) in enumerate(os.walk(path)):
                Image_list = [img for img in files if img.lower().endswith(".jpg")]
                Xml_list = [xml for xml in files if xml.lower().endswith(".xml")]

                cnt = len(Image_list)
                for idx in range(len(Image_list)):
                    image = Image_list[idx]
                    xml = Xml_list[idx]
                    print(image)

                    G = GetGSD(root, image, xml)
                    cm = G.getgsd()

                    M1 = MakeGUI(cm)
                    window = M1.getresult()
                    event, values = window.read()
                    if event in (None, 'Exit'):
                        window.close()
                


    window.close()
    
if __name__ == "__main__":
    main()
