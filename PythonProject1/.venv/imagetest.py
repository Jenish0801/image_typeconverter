import sys
import os
from PIL import Image

#getting path as arguments

source_folder = sys.argv[1]
target_folder = sys.argv[2]

#checking if folder exist

if not os.path.exists(target_folder):
    os.mkdir(target_folder)

for files in os.listdir(source_folder):
    img = Image.open(f"{source_folder}/{files}")
    img.save(f"{target_folder}/{files}.png", 'PNG')
