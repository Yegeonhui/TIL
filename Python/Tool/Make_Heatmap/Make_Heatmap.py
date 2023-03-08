"""
2023-03-08
시각화 툴 : 히트맵
Code by YGH
"""

import pandas as pd
import warnings
import folium
from folium.plugins import HeatMap
from pyproj import Proj, transform
warnings.filterwarnings('ignore')

"""
히트맵 만드는 함수
point : 시각화 하는 맵에서 원하는 중심점 좌표 ex) [lat, lon]
total_center : 야적퇴비 위경도 중심점 [(lat, lon), (lat, lon), ...]
"""
def make_heatmap(
                point : list, 
                total_center : list):
    lat, lon  = point
    m = folium.Map(location=[lat, lon],
                   # 일반
                   # tiles = "http://mt0.google.com/vt/lyrs=m&hl=ko&x={x}&y={y}&z={z}",
                   # 위성
                   tiles = "http://mt0.google.com/vt/lyrs=s&hl=ko&x={x}&y={y}&z={z}",
                    #titles='Stamen Terrain',
                   zoom_start=13, 
                   attr = "Google")
    heatMap = HeatMap(total_center, min_opacity=0.05, max_opacity=100, radius=50, blur=50)
    m.add_child(heatMap)
    return m

df = pd.read_csv('jinyang_results.csv')

# 중심좌표
point : list = [df['lat'][340], df['lon'][340]]

for c in range(2, df.shape[1]):
    center_arr = []
    name = df.columns[c]
    print(name)
    for r in range(df.shape[0]):
        if df.iloc[r, c] == 0:
            continue
        center_arr += [[df.iloc[r, 0], df.iloc[r, 1]] for i in range(df.iloc[r, c])]

    m = make_heatmap(point, center_arr)
    m.save(name + '.html')
    
