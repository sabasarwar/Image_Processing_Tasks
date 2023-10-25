# You can use imread from scipy to read images

# from scipy import misc
# img = misc.imread("img/flower_01.jpeg")
# print(type(img))   #numpy array

# gives a message about scipy.misc is depreciated
# let's use skimage which also gives a numpy array.

from skimage import io, img_as_ubyte
import matplotlib.pyplot as plt
import numpy as np
from scipy import ndimage

img = io.imread("img/flower_01.jpeg")
# numpy array
print(type(img))


# img_as_ubyte converts image to 8 bit unsigned int
img = img_as_ubyte(io.imread("img/flower_01.jpeg", as_gray=True))
print(type(img))
print(img.shape, img.dtype)
# plt.imshow(img)
# plt.savefig("img/Gray_Image.jpg")
# individual pixel values : reports pixel value at 0,0
print("Pixel values at [0,0] :", img[0, 0])

# pixel values from a slice
print("Pixel values from a slice : \n", img[10:15, 20:25])
mean_grey = img.mean()
max_value = img.max()
min_value = img.min()
print("Mean, Min and Max values : ", mean_grey, min_value, max_value)
# plt.imshow(img)

# Geometric Transformation : flipped

flipped_img_LR = np.fliplr(img)
flipped_img_UD = np.flipud(img)
plt.subplot(2, 1, 1)
plt.imshow(img, cmap="Greys")
plt.subplot(2, 2, 3)
plt.imshow(flipped_img_LR, cmap="Blues")
plt.subplot(2, 2, 4)
plt.imshow(flipped_img_UD, cmap="hsv")
plt.savefig("img/Flipped_Img_plots.jpg")

# Rotation
rotated_img = ndimage.rotate(img, 45)
plt.subplot(2, 2, 1)
plt.imshow(rotated_img)
rotated_img_noreshape = ndimage.rotate(img, 45, reshape=False)
plt.subplot(2, 2, 2)
plt.imshow(rotated_img_noreshape)

# Filtering
# Local filters: replace the value of pixels by a function of the values of neighboring pixels.
uniform_filtered_img = ndimage.uniform_filter(img, size=9)
# plt.imshow(uniform_filtered_img)

# Gaussian filter: from scipy.ndimage
# Gaussian filter smooths noise but also edges

blurred_img = ndimage.gaussian_filter(img, sigma=3)  # also try 5, 7
# plt.imshow(blurred_img)

# Median filter is better than gaussian. A non-local means is even better
median_img = ndimage.median_filter(img, 3)
# plt.imshow(median_img)

# Edge detection
sobel_img = ndimage.sobel(img, axis=0)  # Axis along which to calculate sobel
# plt.imshow(sobel_img)

plt.show()
