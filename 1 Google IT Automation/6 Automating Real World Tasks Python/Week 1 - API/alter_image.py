#/usr/bin/env python3

from PIL import Image
import subprocess
import os

for images in os.listdir('images'):
    im = Image.open(os.path.join('images', images)).convert('RGB')
    new_image_name = images + ".jpeg"
    im.rotate(90).resize((128,128)).save(new_image_name)
    subprocess.run(["mv", new_image_name, os.path.join(os.sep, "opt", "icons", new_image_name)])    