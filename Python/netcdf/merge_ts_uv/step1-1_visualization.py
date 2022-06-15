import xarray
import numpy as np
import pandas as pd
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt 

def get_coord_info(ncfile):
    m = Basemap(projection='cyl', 
            lat_ts=10, 
            llcrnrlon = ncfile['lon'][0], 
            urcrnrlon = ncfile['lon'][-1], 
            llcrnrlat = ncfile['lat'][0], 
            urcrnrlat = ncfile['lat'][-1], 
            resolution='h') 
    m.drawcoastlines() 
    m.drawcountries() 
    m.drawmapboundary() ## 위경도표시 
    parallels = np.arange(30.,45.,2.) 
    m.drawparallels(parallels,labels=[True,False,False,False]) #True=1, False =0 으로 표현가능 
    meridians = np.arange(120.,150.,5.) 
    m.drawmeridians(meridians,labels=[True,False,False,True]) ## 등압선 그리기 
    plt.show()

   
ncfile = xarray.open_dataset('new/hycom_glby_930_2021010112_t000.nc', decode_times=False)
get_coord_info(ncfile)