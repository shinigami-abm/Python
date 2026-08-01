import imageio.v3 as iio
import matplotlib.pyplot as plt
import numpy as np

def resize(i, r, c):
    new_c = (np.arange(c)*i.shape[1] / c).astype(int)
    new_r = (np.arange(r)*i.shape[0] / r).astype(int)
    return i[new_r][:,new_c]

img = iio.imread("fih.jpeg")
img1 = iio.imread("fih1.jpeg") 
img2 = iio.imread("fih2.jpeg")
temp = img.copy()
#temp = resize(temp, 400, 100)

temp_f = temp.astype(np.float32) / 255
mean = np.array([0.485, 0.456, 0.406])
std  = np.array([0.229, 0.224, 0.225])
temp = (temp_f - mean) / std

img = resize(img, 200, 200)
img1 = resize(img1, 200, 200)
img2 = resize(img2, 200, 200)
batch = np.stack([img, img1, img2])
print(batch.shape)
batch = batch.transpose(0, 3, 2, 1)
print(batch.shape)

plt.imshow(img)
plt.title("Fihs")
#plt.axis('off')
plt.show()

plt.imshow(img1)
plt.title("Fihs")
#plt.axis('off')
plt.show()

plt.imshow(img2)
plt.title("Fihs")
#plt.axis('off')
plt.show()
