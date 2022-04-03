#!/usr/bin/env python3

from PIL import Image
import subprocess
import os

for images in os.listdir(os.path.join('supplier-data', 'images')):
    if "tiff" not in images:
        continue
    im = Image.open(os.path.join('supplier-data', 'images', images)).convert('RGB')
    new_image_name = os.path.splitext(images)[0] + ".jpeg"
    im.rotate(90).resize((600,400)).save(new_image_name)
    subprocess.run(["mv", new_image_name, os.path.join('supplier-data', 'images', new_image_name)])