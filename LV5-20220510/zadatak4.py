import scipy as sp
from sklearn import cluster, datasets
import numpy as np
import matplotlib.pyplot as plt
import skimage
import matplotlib.image as mpimg


imageNew = mpimg.imread('example.png')

X = imageNew.reshape((-1, 1)) # We need an (n_sample, n_feature) array
k_means = cluster.KMeans(n_clusters=2,n_init=1)
k_means.fit(X) 
values = k_means.cluster_centers_.squeeze()
labels = k_means.labels_
imageNew_compressed = np.choose(labels, values)
imageNew_compressed.shape = imageNew.shape
skimage.io.imsave("rez3.png",imageNew_compressed.astype('uint8'))

plt.figure(1)
plt.imshow(imageNew,  cmap='gray')
plt.show()

plt.figure(2)
plt.imshow(imageNew_compressed,  cmap='gray')
plt.show()