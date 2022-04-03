#!/usr/bin/env python3
import requests
import os

url = "http://localhost/upload/"

for images in os.listdir(os.path.join('supplier-data', 'images')):
    if "jpeg" not in images:
        continue
    with open(os.path.join('supplier-data', 'images', images), 'rb') as opened:
        r = requests.post(url, files={'file': opened})