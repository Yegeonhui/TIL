import xarray
import numpy as np
from glob import glob
import os

def getlonlat(ncfile):
    # lat : 33 ~ 39, lat : 125 ~ 130
    lat = ncfile['lat'].to_numpy()
    lat_arr = np.where((33 <= lat) & (lat <= 39))
    
    lon = ncfile['lon'].to_numpy()
    lon_arr = np.where((125 <= lon) & (lon <= 130))
    
    return lat_arr, lon_arr


def getcoordinate(ncfile, variable):
    minlat = lat_arr[0][0]
    maxlat = lat_arr[0][-1] + 1
    minlon = lon_arr[0][0]
    maxlon = lon_arr[0][-1] + 1

    info = ncfile[variable][:, : num_layer, minlat:maxlat, minlon:maxlon].to_numpy()
    return info

def getxarrayform():
    ncfile = xarray.Dataset({
                        "water_u": (["time", "depth", "lat", "lon"], n_water_u),
                        "water_v": (["time", "depth", "lat", "lon"], n_water_v),
                        "water_temp": (["time", "depth", "lat", "lon"], n_water_temp),
                        "salinity": (["time", "depth", "lat", "lon"], n_salinity)
                        },
                        coords={
                            "time": (['time'], uvfile['time'].to_numpy()),
                            "depth" : (['depth'], uvfile['depth'].to_numpy()),
                            "lat": (["lat"], newlat),
                            "lon": (["lon"], newlon),
                     })
    return ncfile

# option
num_layer = 40

file = glob('./*uv3z.nc')
os.makedirs('new', exist_ok=True)
#uv nc파일만 들고오기
for i in range(len(file)):
    uvname = file[i]
    
    # 저장이름
    name = os.path.splitext(uvname)[0][:-4]
    
    tsname = name + 'ts3z.nc'
    
    # uv파일, ts파일 따로 있음
    uvfile = xarray.open_dataset(uvname, decode_times=False)
    tsfile = xarray.open_dataset(tsname, decode_times=False)

    lat_arr, lon_arr = getlonlat(uvfile)
    
    # 자른 u,v,slinity, water_temp 가져오기 
    n_water_u = getcoordinate(uvfile, 'water_u')
    n_water_v = getcoordinate(uvfile, 'water_v')
    n_salinity = getcoordinate(tsfile, 'salinity')
    n_water_temp = getcoordinate(tsfile, 'water_temp')

    # 기존 time 그대로 들고오기
    time = uvfile['time']

    # 자른 위경도좌표
    newlon = uvfile['lon'][lon_arr].to_numpy()
    newlat = uvfile['lat'][lat_arr].to_numpy()
    
    newncfile = getxarrayform()
    newncfile.to_netcdf('new/' + name[:-1] + '.nc')

