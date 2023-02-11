import os
from PIL import Image

COMPRESSED_PATH = 'compressed'
for filename in os.listdir('to-compress'):
    f = os.path.join('to-compress', filename)
    # checking if it is a file
    if os.path.isfile(f):
      img = Image.open(f).convert('RGB')
      # img = img.convert("P", palette=Image.ADAPTIVE, colors=256)
      img.save(os.path.join(COMPRESSED_PATH, filename), optimize=True, compress_level=9)