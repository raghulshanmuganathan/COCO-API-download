#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 16:45:37 2024

@author: raghul
"""

from pycocotools.coco import COCO
import numpy as np
import skimage.io as io
import matplotlib.pyplot as plt
import pylab
import shutil
import os

dataDir='images'
dataType='train2014'
annFile='annotations/instances_train2014.json'

coco=COCO(annFile)

# Get category information
categories = coco.loadCats(coco.getCatIds())
category_names = [category['name'] for category in categories]


# Find the category ID for 'indoor' supercategory
desired_categories = []
desired_categories += [category['id'] for category in categories if category['supercategory'] == 'indoor']
desired_categories += [category['id'] for category in categories if category['supercategory'] == 'appliance']
desired_categories += [category['id'] for category in categories if category['supercategory'] == 'electronic']
desired_categories += [category['id'] for category in categories if category['supercategory'] == 'furniture']
desired_categories += [category['id'] for category in categories if category['supercategory'] == 'kitchen']

# Get image IDs for images in the desired supercategory
image_ids = []
for cat_id in desired_categories:
    image_ids += coco.getImgIds(catIds=[cat_id])
    
img = coco.loadImgs(image_ids[np.random.randint(0,len(image_ids))])[0]

I = io.imread(img['coco_url'])
plt.axis('off')
plt.imshow(I)
plt.show()

annIds = coco.getAnnIds(imgIds=img['id'], catIds=desired_categories ,iscrowd=None)
anns = coco.loadAnns(annIds)
bbox=anns['bbox']