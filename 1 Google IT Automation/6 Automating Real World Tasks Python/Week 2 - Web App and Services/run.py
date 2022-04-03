#! /usr/bin/env python3

import os
import requests

for file in os.listdir(os.path.join(os.sep, 'data', 'feedback')):
    with open(os.path.join(os.sep, 'data', 'feedback', file)) as feedback_file:
        feedback = {}
        feedback['title'] = feedback_file.readline().strip()
        feedback['name'] = feedback_file.readline().strip()
        feedback['date'] = feedback_file.readline().strip()
        feedback['feedback'] = feedback_file.readline().strip()
        
        response = requests.post("http://34.66.71.5/feedback/", json=feedback)
        if response.ok:
            print("Data succesfully stored.")
        else:
            print("Operation Failed.")
