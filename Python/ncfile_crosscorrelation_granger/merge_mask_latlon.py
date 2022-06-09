from mpl_toolkits.basemap import Basemap
import numpy as np
import xarray

# 위경도좌표가 주어지지 않는 경우 만드는 코드
def get_coord_info(info):
    if info['grid_mapping_name'] == 'lambert_conformal_conic':
        projection='lcc'

    m = Basemap(width=info['upper_left_easting'] * 2, 
                height=info['upper_left_easting'] * 2,
                #rsphere=(6378137.00,6356752.3142),
                ellps='WGS84',
                #l, h, c
                resolution='l',area_thresh=1000.,
                projection=projection,
                lat_1=info['standard_parallel1'],
                lat_2=info['standard_parallel2'],
                lat_0=info['origin_latitude'],
                lon_0=info['central_meridian'])
    lat, lon = m.makegrid(900, 900)

    # numpy배열과 지도 lat, lon이 뒤집혀있음. 
    lat = np.flip(lat, axis=1)
    lon = np.flip(lon, axis=1)

    coordinate = np.stack((lat, lon), axis=2)
    
    return coordinate

# 천리안 2A 자료 mask만드는 코드
def makemask(ncfile_path, product, info):
    dim = info['image_width'] 
    # +2 는 위경도 좌표 
    mask = np.zeros((dim, dim, len(ncfile_path) + 2))
    
    cnt = 0
    for ncfileroute in ncfile_path:
        ncfile = xarray.open_dataset(ncfileroute)
        # proj 정보
        info = ncfile['gk2a_imager_projection'].attrs
        # 위경도 좌표 가져오기 
        coordinate = get_coord_info(info)

        ncfile = xarray.open_dataset(ncfileroute)
        productmask = ncfile[product][:].to_numpy()
        mask[:, :, cnt] = productmask
        cnt += 1

    mask[:, :, -2:] = coordinate[:, :, :]
    return mask, coordinate

# hycom 자료 mask만드는 코드
def make_hycommask(ncfile_path, layer, time):
    # load ncfile
    ncfile = xarray.open_dataset(ncfile_path[0])
    
    _, depth, height, width = ncfile[layer].shape
    
    # +2 는 위경도 좌표, 위경도 좌표는 mask 끝단에 위치
    mask = np.zeros((height, width, len(ncfile_path) + 2))
    
    cnt = 0
    for ncfileroute in ncfile_path:
        ncfile = xarray.open_dataset(ncfileroute)

        # layer 값을 마스크에 붙이기
        mask[:, :, cnt] = ncfile[layer][time][:, :, :].to_numpy()
        cnt += 1

    # 위경도 좌표 가져오기 
    lat = ncfile['lat'][:]
    lon = ncfile['lon'][:]
    
    lon, lat = np.meshgrid(lon, lat)

    mask[:, :, -2] = lat
    mask[:, :, -1] = lon

    return mask



