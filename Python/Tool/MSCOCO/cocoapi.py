from pycocotools.coco import COCO
import numpy as np
import skimage.io as io
import matplotlib.pyplot as plt
import pylab

datadir = 'Sea_Bbox_sample'
#datadir = 'Sea_Polygon_sample'
coco=COCO(datadir + '.json')
# cats = coco.loadCats(coco.getCatIds())
# print(cats)
if datadir == 'Sea_Bbox_sample':
    catIds = coco.getCatIds(catNms=["Heliocidaris_crassispina", 'Turbo_cornutus', 
                                    "Asterina_pectinifera", "Asterias_amurensis",
                                    "Conch", "Sea_hare", "Hemicentrotus"
                                    ])
else:
    catIds = coco.getCatIds(catNms=["Sargassum", 'Ecklonia_cava'
                                    ])
# print(catIds)
# #imgIds = coco.getImgIds(catIds=catIds)
# #print(imgIds)
# imgIds = coco.getImgIds(imgIds = catIds)
# print(imgIds)
for i in range(1, 101):
    img_info = coco.loadImgs(i)[0]
    I = io.imread(datadir + '/' + img_info['file_name'])
    plt.imshow(I)
    plt.axis('off')
    #print(img_info['id'])
    #print(catIds)
    annIds = coco.getAnnIds(imgIds=img_info['id'], catIds=catIds, iscrowd=0)
    #print(annIds)
    anns = coco.loadAnns(annIds)
    #print(anns)
    if datadir == 'Sea_Bbox_sample':
        coco.showAnns(anns, draw_bbox=True)
    else:
        coco.showAnns(anns)
    plt.show()
    
