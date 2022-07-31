import cv2
import os

os.makedirs(os.getcwd() + "/frame", exist_ok = True)
for idx, (root, dirs, files) in enumerate(os.walk("video")):
    Video_list = [video for video in files if video.lower().endswith(".mp4")]
    for video in Video_list:
        cap = cv2.VideoCapture(os.path.join(root, video))
        print(cap.get(cv2.CAP_PROP_FPS))
        print(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        fps = 30
        cap.set(cv2.CAP_PROP_POS_FRAMES, 300)
        
        while True:
            frame = cap.get(cv2.CAP_PROP_POS_FRAMES)
            print(frame)
            
            success, image = cap.read()
            #총 프레임 수 
            
            if cap.get(cv2.CAP_PROP_FRAME_COUNT) == frame :
                break 
            
            if frame % (fps * 3) == 0:
                if success == False:
                    print("프레임 추출 실패") 
                if os.path.split(root)[1] == "L":
                    image = cv2.rotate(image, cv2.ROTATE_90_COUNTERCLOCKWISE)
                elif os.path.split(root)[1] == "R":
                    image = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
                try:
                    cv2.imwrite(os.getcwd() + "/frame/" + video + "_" + str(int(frame / fps / 3)) + ".jpg", image)
                    print("saved imaged" + video + "_" + str(int(frame / fps / 3)) + ".jpg")
                except:
                    print("오류")
            
            if cv2.waitKey(10) == 27:
                break
            
