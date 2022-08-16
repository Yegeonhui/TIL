import numpy as np
from glob import glob 
import xarray 
from merge_mask_latlon import make_hycommask       
import os

# setting value
layer = 'water_temp'
# 12, 15, 18, 21 
time = 12
time = time // 3 - 4
# load ncfile
ncfile_path = glob('ncfile/*.nc', recursive=True)

# layer value + lat, lon
mask = make_hycommask(ncfile_path, layer, time)

# save mask
np.save(layer + '.npy', mask)