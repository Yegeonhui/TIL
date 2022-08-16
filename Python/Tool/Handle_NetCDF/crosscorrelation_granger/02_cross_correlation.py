import pandas as pd
import numpy as np
import statsmodels.tsa.stattools as stattools
from statsmodels.graphics.tsaplots import plot_acf
import matplotlib.pyplot as plt

def cross_correlation(mask1, mask2, x, y):
    _, _, c = mask1.shape

    # 위경도 좌표 빼고 
    x1 = pd.DataFrame(mask1[y, x, :c-2])
    y1 = pd.DataFrame(mask2[y, x, :c-2])
    
    # 선형으로 비례하는 방식으로 결측값 보간
    x1 = x1.interpolate(method='values')
    y1 = y1.interpolate(method='values')
    
    # 차분적용 
    x1 = x1.diff(1).dropna()
    y1 = y1.diff(1).dropna()

    #교차상관관계 계산
    ccs = stattools.ccf(x1, y1, unbiased=False)[:c-2]
    nlags = len(ccs)

    # /* Compute the Significance level */
    conf_level = 2 / np.sqrt(nlags)

    # /* Draw Plot */
    plt.figure()

    plt.hlines(0, xmin=0, xmax=c-2, color='gray')  # 0 axis
    plt.hlines(conf_level, xmin=0, xmax=c-2, color='gray')
    plt.hlines(-conf_level, xmin=0, xmax=c-2, color='gray')

    plt.bar(x=np.arange(len(ccs)), height=ccs, width=.3)

    plt.xlim(0, len(ccs))
    plt.show()
    #plt.savefig('image.png')

# 자기상관함수 확인 (비정상 여부 판단)
def acf(mask, x, y):
    data = pd.DataFrame(mask[y, x, :-2])
    data = data.interpolate(method='values')
    print(data.diff(1))
    
    # 차분 적용, lags : 개수, alpha : 95% 신뢰구간으로 추정된 표준편차
    fig = plot_acf(data.diff(1).dropna(), lags=118, alpha=0.05)
    # 차분 적용 x
    fig = plot_acf(data, lags=118, alpha=0.05)
    plt.show()

# load npy
mask0 = np.load('SST.npy')
mask1 = np.load('speed.npy')

# 비교를 원하는 좌표 
coor_arr = [(328, 606), (375, 650), (669, 545)]

# 교차상관관계
for x, y in coor_arr:
    cross_correlation(mask0, mask1, x, y)
    #acf(mask0, x, y)
