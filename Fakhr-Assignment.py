import numpy as np
import os
from PIL import Image
import matplotlib.pylab as plt

for path, folder, files in os.walk('photos'):
    pass
len(files)


img_arr = np.zeros([len(files), 150, 200, 3])
new_shape = (200, 150)


def resize_image():
    if os.path.exists('resize_photos') == False:
        os.mkdir('resize_photos')
    i = 0
    for img in files:
        im = Image.open('photos\\'+img)
        resize_img = im.resize(new_shape)
        resize_img.save('resize_photos'+'\\'+img,"JPEG")
        resize_arr = plt.imread('resize_photos'+'\\'+img)
        v = img_arr[i] = resize_arr
        i += 1
def checker():
    try:
        for img in files:
            image = plt.imread('photos\\'+img)
    except OSError as e:
        print(f"{e} : Error occurred because other extension file exits in this folder : {os.getcwd()}\\photos")

if __name__ == "__main__":
    checker()
    resize_image()