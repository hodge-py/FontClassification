from PIL import Image, ImageOps
import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt

df = pd.DataFrame()

fontType = os.listdir("./fontPics")

names = []
files = os.listdir("./fontPics/"+fontType[0])

for x in fontType:
    names += [x[:-4]]

count = 0
for x in fontType:
    for y in os.listdir("./fontPics/"+x):
        im = Image.open(f'./fontPics/{x}/{y}')

        im2 = ImageOps.grayscale(im)

        arr = np.asarray(im2)

        arr = arr.reshape(1, -1)

        df = pd.concat([df, pd.DataFrame(arr)])


    if count == 1:
        break

    count += 1




"""
newPic = np.array(df.iloc[1]).reshape(32,32)
plt.figure(figsize=(5,5))
plt.imshow(newPic)
plt.colorbar()
plt.grid(False)
plt.show()
"""