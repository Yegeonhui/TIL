import os
import cv2
from matplotlib import pyplot as plt
import numpy as np

for idx, (root, dirs, files) in enumerate(os.walk('Image')):
    Image_list = [img for img in files if img.lower().endswith('.jpg')]
    for n in range(len(Image_list)):
        Image = cv2.imread(os.path.join(root, Image_list[n]))
        B, G, R = cv2.split(Image)
        
        Image_HSV = cv2.cvtColor(Image, cv2.COLOR_BGR2HSV)
        H, S, V = cv2.split(Image_HSV)

        Image_Lab = cv2.cvtColor(Image, cv2.COLOR_BGR2Lab)
        L, a, b = cv2.split(Image_Lab)
        
        Image_YUV = cv2.cvtColor(Image, cv2.COLOR_BGR2YUV)
        y, u, v = cv2.split(Image_YUV)

        # X_list = [554,705,728,1087,1128,1084]
        # Y_list = [799,109,9,636,813,613]  

        # X_list = [712,695,658,550,511,1157]
        # Y_list = [36,105,249,685,832,818]

        X_list = [695,585,1157,520,603]
        Y_list = [86,526,832,779,458]

        r_values = []
        g_values = []
        b_values = []
        
        h_values = []
        s_values = []
        v_values = []
        
        L_values = []
        A_values = []
        B_values = []
        
        Y_values = []
        U_values = []
        V_values = []
        
        for idx in range(len(X_list)):
            X = X_list[idx]
            Y = Y_list[idx]
            
            r_values.append(R[Y][X])
            g_values.append(G[Y][X])
            b_values.append(B[Y][X])
            
            h_values.append(H[Y][X])
            s_values.append(S[Y][X])
            v_values.append(V[Y][X])
            
            L_values.append(L[Y][X])
            A_values.append(a[Y][X])
            B_values.append(b[Y][X])
            
            Y_values.append(y[Y][X])
            U_values.append(u[Y][X])
            V_values.append(v[Y][X])
        # print(r_values)
        # print(g_values)
        # print(b_values)
        # print(h_values)
        # print(s_values)
        # print(v_values)
        # print(L_values)
        # print(A_values)
        # print(B_values)
        print(Y_values)
        print(U_values)
        print(V_values)

    
        # Image_HSV = cv2.resize(Image_HSV, dsize = (480, 480))
    

        # cv2.imshow("Image_HSV", Image_HSV)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()


r_values = [91, 123, 144, 18, 0, 29, 39, 52, 18, 22, 17, 0,133, 77, 8, 84, 117]
g_values = [137, 152, 175, 79, 131, 120, 129, 147, 121, 170, 118, 104,175, 197, 113, 159, 160]
b_values = [126, 148, 167, 100, 144, 139, 127, 143, 120, 172, 128, 133,165, 198, 145, 154, 151]

h_values = [83, 86, 82, 98, 93, 95, 89, 89, 90, 90, 93, 97,83, 90, 97, 88, 84]
s_values = [86, 49, 45, 209, 255, 202, 178, 165, 217, 222, 221, 255,61, 156, 241, 120, 69]
v_values = [137, 152, 175, 100, 144, 139, 129, 147, 121, 172, 128, 133,175, 198, 145, 159, 160]

L_values = [137, 155, 176, 79, 127, 118, 125, 142, 117, 161, 115, 103, 174, 187, 113, 155, 160]
A_values = [110, 117, 116, 117, 103, 109, 102, 100, 101, 94, 105, 114, 112, 95, 114, 103, 111]
B_values = [129, 127, 129, 110, 112, 110, 121, 122, 121, 117, 115, 105, 129, 118, 103, 123, 128]

Y_values = [122, 143, 165, 63, 93, 95, 102, 118, 90, 126, 89, 76, 161, 161, 85, 136, 146]
U_values = [130, 130, 129, 146, 153, 150, 140, 140, 143, 151, 147, 156, 130, 146, 158, 137, 130]
V_values = [101, 110, 110, 89, 46, 70, 73, 70, 65, 37, 65, 61,103, 54, 60, 82, 103]

x_values = [n for n in range(len(r_values))]

plt.plot(x_values, r_values, color = "red")
plt.plot(x_values, g_values, color = "green")
plt.plot(x_values, b_values, color = "blue")
plt.plot(x_values, h_values, color = "purple")
plt.plot(x_values, s_values, color = "yellow")
plt.plot(x_values, v_values, color = "orange")
# # plt.plot(x_values, L_values, color = "gray")
# # plt.plot(x_values, A_values, color = "pink")
# # plt.plot(x_values, B_values, color = "navy")
plt.plot(x_values, Y_values, color = "gray")
plt.plot(x_values, U_values, color = "pink")
plt.plot(x_values, V_values, color = "navy")
plt.show()
