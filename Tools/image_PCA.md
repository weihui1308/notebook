### 1. 对image的color进行主成分分析，画出相应的颜色板以及对应比例
````python
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from sklearn.cluster import KMeans
from collections import Counter


def show_img_compar(img_1, img_2):
    f, ax = plt.subplots(1, 2, figsize=(10,10))
    ax[0].imshow(img_1)
    ax[1].imshow(img_2)
    ax[0].axis('off')
    ax[1].axis('off')
    f.tight_layout()
    img = Image.fromarray(img_2)
    img.save("5.png")
    plt.show()


img = cv.imread('../dataset/style/0005.png')
img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
img_2 = cv.imread('../dataset/style/0001.png')
img_2 = cv.cvtColor(img_2, cv.COLOR_BGR2RGB)
#show_img_compar(img, img_2)
print("1")

dim = (300, 300)
# resize image
img = cv.resize(img, dim, interpolation = cv.INTER_AREA)
img_2 = cv.resize(img_2, dim, interpolation = cv.INTER_AREA)

clt = KMeans(n_clusters=10)
clt.fit(img.reshape(-1, 3))

def palette(clusters):
    width=300
    palette = np.zeros((50, width, 3), np.uint8)
    steps = width/clusters.cluster_centers_.shape[0]
    for idx, centers in enumerate(clusters.cluster_centers_):
        palette[:, int(idx*steps):(int((idx+1)*steps)), :] = centers
    return palette


def palette_perc(k_cluster):
    width = 300
    palette = np.zeros((50, width, 3), np.uint8)

    n_pixels = len(k_cluster.labels_)
    counter = Counter(k_cluster.labels_)  # count how many pixels per cluster
    perc = {}
    for i in counter:
        perc[i] = np.round(counter[i] / n_pixels, 2)
    perc = dict(sorted(perc.items()))

    # for logging purposes
    print(perc)
    print(k_cluster.cluster_centers_)

    step = 0

    for idx, centers in enumerate(k_cluster.cluster_centers_):
        palette[:, step:int(step + perc[idx] * width + 1), :] = centers
        step += int(perc[idx] * width + 1)

    return palette

clt_1 = clt.fit(img.reshape(-1, 3))
show_img_compar(img, palette_perc(clt_1))
````

### 2. 获取图像的饱和度
````python
img = Image.open('../dataset/style/0001.png')
colors = img.convert('RGB').getcolors(maxcolors=img.size[0]*img.size[1])
print(len(colors))

image = cv2.imread('../dataset/style/0006.png')
hsv = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)
H, S, V = cv2.split(hsv)
#print(H, S, V)

s = S.ravel()[np.flatnonzero(S)]
average_s  = sum(s)/len(s)
print(average_s)
````