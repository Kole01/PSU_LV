import matplotlib.pyplot as plt
import numpy as np
import skimage.io

img = skimage.io.imread('tiger.png', as_gray=True)
rows,  cols = img.shape
img_bright = img.copy()
img_rotate = np.zeros((cols,rows))
img_mirror = np.zeros((rows,cols))
img_resize = np.zeros((int(rows/10),int(cols/10)))
img_black = np.zeros((rows,cols))
check = cols/4

for i in range (rows):
    for j in range (cols):
        if (img[i,j] > 205):
            img_bright[i,j] = 255
        else:
            img_bright[i,j] += 50

for i in range (rows):
    img_rotate[:,rows-1-i]=img[i,:] 

for i in range (cols):
    img_mirror[:,i]=img[:,cols-1-i]

for i in range(0,rows,10):
    for j in range (0,cols,10):
        img_resize[int(i/10),int(j/10)]= img[i,j]


for i in range (cols):
    if i>(check-1) and i<((2*check)-1):
        img_black[:,i]=img[:,i]

plt.figure(1)
plt.imshow(img, cmap='gray', vmin=0, vmax=255)
plt.figure(2)
plt.imshow(img_bright, cmap='gray', vmin=0, vmax=255)
plt.figure(3)
plt.imshow(img_rotate, cmap='gray', vmin=0, vmax=255)
plt.figure(4)
plt.imshow(img_mirror, cmap='gray', vmin=0, vmax=255)
plt.figure(5)
plt.imshow(img_resize, cmap='gray', vmin=0, vmax=255)
plt.figure(6)
plt.imshow(img_black, cmap='gray', vmin=0, vmax=255)
plt.show()
