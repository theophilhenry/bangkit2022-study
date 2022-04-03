#! /usr/bin/env python3

import os
import requests

for file in os.listdir(os.path.join('supplier-data', 'descriptions')):
    with open(os.path.join('supplier-data', 'descriptions', file)) as fruit_file:
        fruit = {}
        fruit['name'] = fruit_file.readline().strip()
        fruit['weight'] = int(fruit_file.readline().strip().split()[0])
        fruit['description'] = fruit_file.readline().strip()
        fruit['image_name'] = os.path.splitext(file)[0] + '.jpeg'
        print(fruit)
        
        response = requests.post("http://localhost/fruits/", json=fruit)
        if response.ok:
            print("Data succesfully stored.")
        else:
            print("Operation Failed.")