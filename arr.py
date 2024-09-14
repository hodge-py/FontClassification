from PIL import Image, ImageOps
import numpy as np
import pandas as pd
import os

df = pd.DataFrame()

fontType = os.listdir("./fontPics")

names = []
print(os.listdir("./fontPics/"+fontType[0]))
for x in fontType:
    names += [x[:-4]]

for x in fontType:
    for y in os.listdir("./fontPics/"+x):
        pass

im = Image.open('./fontPics/Arial.ttf/Arial.ttf520.jpg')

im2 = ImageOps.grayscale(im)

arr = np.asarray(im2)

arr = arr.reshape(1,-1)

print(arr.shape,arr)
