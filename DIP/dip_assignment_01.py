import numpy as np
import matplotlib.pyplot as plt

from skimage import data
from skimage.color import rgb2gray

# load the image into a varaible and show that image in a pop-up window
image = data.imread(r"C:\Users\Atif\Pictures\Saved Pictures\abc.jpg")
grey_scale_image = rgb2gray(image)
plt.imshow(grey_scale_image)
plt.waitforbuttonpress()
print(grey_scale_image)

(total_rows, total_columns) = np.shape(grey_scale_image)

row = 0

while row < total_rows:
    col = 0
    while col < total_columns:
        if grey_scale_image[row, col] == 1:
            grey_scale_image[row, col] = 0

        else:
            grey_scale_image[row, col] = 0

        col = col + 1

    print('hi')

    row = row + 1

plt.imshow(grey_scale_image)
plt.waitforbuttonpress()
print(grey_scale_image)