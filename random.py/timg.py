import numpy as np
import imageio.v3 as iio
import matplotlib.pyplot as plt

def resize(i, c, r):
    new_r= (np.arange(r)*i.shape[0] / r).astype(np.int32)
    new_c= (np.arange(c)*i.shape[1] / c).astype(np.int32)
    return i[new_r][:,new_c]
 
img = iio.imread("fih.jpeg")

temp = np.flip(resize(img[40:350, 300:650]@[0.114, 0.587, 0.299], 200, 200), 1)
temp = np.flip(img, 1)

t = temp.astype(np.float32)/ 255
mean = np.array([0.485, 0.456, 0.406])
std  = np.array([0.229, 0.224, 0.225])
temp = (t - mean) / std
batch = np.stack([temp])
batch = batch.transpose(0, 3, 2, 1)

plt.imshow(temp, "gray")
plt.title("fih")
plt.show()

