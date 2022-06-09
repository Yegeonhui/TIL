import statsmodels.api as sm
import pandas as pd
import numpy as np

# 1단계에서 만든 npy파일 load
mask0 = np.load('SST.npy')
mask1 = np.load('speed.npy')

# 비교를 원하는 좌표 설정 
coor_arr = [(669, 545)]

#그레인저 인과관계
for x, y in coor_arr:
    x1 = pd.DataFrame(mask0[y, x, :-2])
    y1 = pd.DataFrame(mask1[y, x, :-2])

    # 선형 보간
    x1 = x1.interpolate(method='values')
    y1 = y1.interpolate(method='values')
    
    # x1, y1 합침
    df = pd.concat([x1, y1], axis=1)
    print(df.iloc[:, [1,0]])
    # maxlag=지연단계, verbose=true인 경우 결과 인쇄
    #sm.tsa.stattools.grangercausalitytests(df.diff(1).dropna().iloc[:, [1,0]].values, maxlag=25, verbose=True)
    #sm.tsa.stattools.grangercausalitytests(df.diff(1).dropna().iloc[:, :].values, maxlag=25, verbose=True)