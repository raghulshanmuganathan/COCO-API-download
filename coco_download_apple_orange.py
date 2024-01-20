#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 15:55:05 2024

@author: raghul
"""

from pycocotools.coco import COCO
import requests
import os

# Specify the COCO annotations file and the image directory
annotations_file = 'annotations/instances_train2014.json'  # Change to 'instances_val2014.json' for the validation set
image_directory_apple = 'images_apple'  
image_directory_orange = 'images_orange'  

# Initialize COCO API
coco = COCO(annotations_file)

# Get category information
categories = coco.loadCats(coco.getCatIds())
category_names = [category['name'] for category in categories]


# Find the category ID for 'indoor' supercategory
apple_cat_id = [category['id'] for category in categories if category['name'] == 'apple']
orange_cat_id = [category['id'] for category in categories if category['name'] == 'orange']


# Get image IDs for images in the desired categories
apple_image_ids = coco.getImgIds(catIds=apple_cat_id)
orange_image_ids = coco.getImgIds(catIds=orange_cat_id)

# Download images - Apple images
for image_id in apple_image_ids:
    image_info = coco.loadImgs(image_id)[0]
    image_url = image_info['coco_url']
    image_filename = os.path.join(image_directory_apple, image_info['file_name'])

    # Download the image
    response = requests.get(image_url, stream=True)
    with open(image_filename, 'wb') as image_file:
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:
                image_file.write(chunk)

    print(f"Downloaded image: {image_filename}")
    
# Download images - Orange images
for image_id in orange_cat_id:
    image_info = coco.loadImgs(image_id)[0]
    image_url = image_info['coco_url']
    image_filename = os.path.join(image_directory_orange, image_info['file_name'])

    # Download the image
    response = requests.get(image_url, stream=True)
    with open(image_filename, 'wb') as image_file:
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:
                image_file.write(chunk)

    print(f"Downloaded image: {image_filename}")